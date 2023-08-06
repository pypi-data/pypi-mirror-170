_A=False
import logging,os,re,tempfile,threading,traceback
from typing import List
from localstack import config,constants
from localstack.config import dirs
from localstack.constants import MAVEN_REPO_URL
from localstack.services.install import ARTIFACTS_REPO,INSTALL_DIR_STEPFUNCTIONS,INSTALL_PATH_STEPFUNCTIONS_JAR,JAR_URLS,SFN_PATCH_URL_PREFIX,Installer,InstallerRepository,add_file_to_jar,download_and_extract_with_retry,log_install_msg,update_jar_manifest
from localstack.utils.files import file_exists_not_empty
from localstack.utils.http import download
from localstack.utils.run import run
from localstack.utils.time import now
from localstack_ext.bootstrap.installer import mariadb_installer,mosquitto_installer,postgres_installer,redis_installer,timescaledb_installer
from localstack_ext.bootstrap.licensing import api_key_configured,is_enterprise,prepare_environment
from localstack_ext.constants import ACTIVE_MQ_URL
LOG=logging.getLogger(__name__)
RULE_ENGINE_INSTALL_URL='https://github.com/whummer/serverless-iot-offline'
H2_DOWNLOAD_URL='http://www.h2database.com/h2-2019-10-14.zip'
SSL_CERT_URL=f"{ARTIFACTS_REPO}/raw/master/local-certs/server.key"
SSL_CERT_URL_FALLBACK='{api_endpoint}/proxy/localstack.cert.key'
POSTGRES_LIB_FOLDER='/usr/lib/postgresql/11/lib'
SFN_PATCH_PRO_CLASS1='cloud/localstack/PersistenceAspect.class'
SFN_PATCH_PRO_CLASS2='cloud/localstack/PersistenceContext.class'
SFN_PATCH_PRO_CLASS3='cloud/localstack/PersistenceState.class'
SFN_PATCH_PRO_CLASS4='cloud/localstack/PersistenceRegionState.class'
SFN_PATCH_PRO_FILE_METAINF='META-INF/aop-pro.xml'
URL_KRYO=f"{MAVEN_REPO_URL}/com/esotericsoftware/kryo/5.2.0/kryo-5.2.0.jar"
URL_OBJENESIS=f"{MAVEN_REPO_URL}/org/objenesis/objenesis/3.2/objenesis-3.2.jar"
URL_MINLOG=f"{MAVEN_REPO_URL}/com/esotericsoftware/minlog/1.3.1/minlog-1.3.1.jar"
URL_REFLECTASM=f"{MAVEN_REPO_URL}/com/esotericsoftware/reflectasm/1.11.9/reflectasm-1.11.9.jar"
PRO_JAR_URLS=[URL_KRYO,URL_OBJENESIS,URL_MINLOG,URL_REFLECTASM]
INSTALL_LOCK=threading.RLock()
INSTALL_DIR_MQ_ACTIVE_MQ=os.path.join(dirs.var_libs,'mq','active-mq')
INSTALL_PATH_MQ_ACTIVE_MQ_DIR=os.path.join(INSTALL_DIR_MQ_ACTIVE_MQ,'apache-activemq-5.16.5')
def install_libs():install_iot_rule_engine();postgres_installer.install(raise_on_error=_A);timescaledb_installer.install(raise_on_error=_A);redis_installer.install(raise_on_error=_A);mosquitto_installer.install(raise_on_error=_A);install_stepfunctions()
def install_iot_rule_engine():
	A=config.dirs.static_libs;B=os.path.join(A,'node_modules','serverless-iot-offline','query.js')
	if not os.path.exists(B):LOG.info('Installing IoT rule engine. This may take a while.');run(['npm','install','--prefix',A,RULE_ENGINE_INSTALL_URL])
	return B
def install_stepfunctions():
	D='StepFunctionsLocal.jar'
	if not os.path.exists(INSTALL_PATH_STEPFUNCTIONS_JAR):LOG.warning('StepFunctions JAR not available - skipping installation');return
	E=[SFN_PATCH_PRO_CLASS1,SFN_PATCH_PRO_CLASS2,SFN_PATCH_PRO_CLASS3,SFN_PATCH_PRO_CLASS4,SFN_PATCH_PRO_FILE_METAINF]
	for A in E:F=f"{SFN_PATCH_URL_PREFIX}/{A}";add_file_to_jar(A,F,target_jar=INSTALL_PATH_STEPFUNCTIONS_JAR)
	update_jar_manifest(D,INSTALL_DIR_STEPFUNCTIONS,re.compile('Main-Class: com\\.amazonaws.+'),'Main-Class: cloud.localstack.StepFunctionsStarter');G=' '.join([os.path.basename(A)for A in[*(PRO_JAR_URLS),*(JAR_URLS)]]);update_jar_manifest(D,INSTALL_DIR_STEPFUNCTIONS,re.compile('Class-Path: .+ \\. '),f"Class-Path: {G} . ")
	for B in PRO_JAR_URLS:
		C=os.path.join(INSTALL_DIR_STEPFUNCTIONS,os.path.basename(B))
		if not file_exists_not_empty(C):download(B,C)
def install_amazon_mq():
	if not os.path.exists(INSTALL_PATH_MQ_ACTIVE_MQ_DIR):log_install_msg('Amazon MQ - Active MQ');A=os.path.join(tempfile.gettempdir(),'localstack.active.mq.tar.gz');download_and_extract_with_retry(ACTIVE_MQ_URL,A,INSTALL_DIR_MQ_ACTIVE_MQ)
def setup_ssl_cert():
	from localstack.services import generic_proxy as C;A=C.get_cert_pem_file_path()
	if os.path.exists(A):
		if is_enterprise():LOG.debug('Avoiding to update SSL certificate.');return
		D=6*60*60;E=os.path.getmtime(A)
		if E>now()-D:LOG.debug('Using cached SSL certificate (less than 6hrs since last update).');return
	LOG.debug('Attempting to download local SSL certificate file');F=3;G=5
	try:return download_github_artifact(SSL_CERT_URL,A,timeout=F)
	except Exception:
		B=SSL_CERT_URL_FALLBACK.format(api_endpoint=constants.API_ENDPOINT)
		try:return download(B,A,timeout=G)
		except Exception as H:LOG.info('Unable to download local test SSL certificate from %s to %s (using self-signed cert as fallback): %s',B,A,H);raise
def download_github_artifact(url,target_file,timeout=None):
	B=target_file;A=url
	def C(url,print_error=_A):
		try:download(url,B,timeout=timeout);return True
		except Exception as A:
			if print_error:LOG.info('Unable to download Github artifact from from %s to %s: %s %s'%(url,B,A,traceback.format_exc()))
	D=C(A)
	if not D:A=A.replace('https://github.com','https://cdn.jsdelivr.net/gh');A=A.replace('/raw/master/','@master/');C(A,True)
def install_azure():from localstack_ext.services.azure import api_specs as A;A.download_api_specs()
def install_ecr():from localstack_ext.services.ecr import registry as A;A.get_registry_binary()
def install_pysiddhi():from localstack_ext.services.kinesisanalytics import query_utils as A;A.setup_siddhi()
def install_neptune():from localstack_ext.services.neptune import neptune_api as A;A.install_graphdb()
def install_qldb():from localstack_ext.services.qldb import partiql as A;A.install_partiql()
def install_k3d():from localstack_ext.services.eks import k8s_utils as A;A.KubeProviderK3S().initialize()
def install_kafka():from localstack_ext.services.kafka.provider import download_kafka as A;A()
class ExtInstallerRepository(InstallerRepository):
	name='ext'
	def should_load(A):return api_key_configured()
	def load(A,*B,**C):
		LOG.debug('Preparing Pro environment for LocalStack Package Manager.')
		with prepare_environment():LOG.debug('Pro environment has successfully been prepared.')
	def get_installer(A):return[('iot-rule-engine',install_iot_rule_engine),('postgres',postgres_installer.install),('timescaledb',timescaledb_installer.install),('redis',redis_installer.install),('mqtt',mosquitto_installer.install),('azure',install_azure),('ecr',install_ecr),('mysql',mariadb_installer.install),('pysiddhi',install_pysiddhi),('neptune',install_neptune),('qldb',install_qldb),('k3d',install_k3d),('kafka',install_kafka),('stepfunctions',install_stepfunctions),('amazon-mq',install_amazon_mq)]