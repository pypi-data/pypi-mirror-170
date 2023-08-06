_R='curses'
_Q='Format (curses, rich, json).'
_P='--format'
_O='--strategy'
_N='[red]No such inject strategy.[/red]'
_M='--version'
_L='--message'
_K='--local'
_J='--services'
_I='[red]Error:[/red] Input the services as a comma-delimited list'
_H=None
_G='-s'
_F='name'
_E='Name of the Cloud Pod.'
_D=True
_C='--name'
_B='-n'
_A=False
import os,sys,traceback
from typing import Dict,List,Optional,Set
import click,requests
from click import Context
from localstack import config
from localstack.cli import console
from localstack.utils.analytics.cli import publish_invocation
from localstack_ext.bootstrap.pods.pods_api_types import DEFAULT_MERGE_STRATEGY,GetStatusResponse,GetStatusVerboseResponse,MergeStrategy
from localstack_ext.bootstrap.pods.utils.common import is_comma_delimited_list
from localstack_ext.cli.click_utils import clean_command_dict,command_require_at_least_open_option,print_table,required_if_not_cached
from localstack_ext.cli.cloud_pods_pretty import MergeStrategyPretty,_normalise_status_response,_normalise_status_response_verbose
from localstack_ext.cli.tree_view import TreeRenderer
class PodsCmdHandler(click.Group):
	def invoke(self,ctx):
		try:return super(PodsCmdHandler,self).invoke(ctx)
		except Exception as exc:
			if isinstance(exc,click.exceptions.Exit):raise
			click.echo(f"Error: {exc}")
			if ctx.parent and ctx.parent.params.get('debug'):click.echo(traceback.format_exc())
			ctx.exit(1)
def _cloud_pod_initialized(pod_name):
	from localstack_ext.bootstrap import pods_client
	if not pods_client.is_initialized(pod_name=pod_name):console.print(f"[red]Error:[/red] Could not find local CloudPods instance '{pod_name}'");return _A
	return _D
def _is_host_reachable():
	is_up=_A
	try:_=requests.get(config.get_edge_url());return _D
	except requests.ConnectionError:console.print('[red]Error:[/red] Destination host unreachable.')
	return is_up
def api_key_configured():A='LOCALSTACK_API_KEY';return _D if os.environ.get(A)and os.environ.get(A).strip()else _A
@click.group(name='pod',help='Manage the state of your instance via Cloud Pods.',cls=PodsCmdHandler,context_settings=dict(max_content_width=120))
def pod():
	from localstack_ext.bootstrap.licensing import is_logged_in
	if not is_logged_in():console.print('[red]Error:[/red] not logged in, please log in first');sys.exit(1)
@pod.command(name='config',help='Configure a set of parameters for all Cloud Pods commands.',cls=command_require_at_least_open_option())
@click.option(_B,_C,help=_E)
@click.option(_G,_J,help='Comma-delimited list of services or `all` to enable all (default).')
@publish_invocation
def cmd_pod_config(name,services):
	from localstack_ext.bootstrap import pods_client
	if services and not is_comma_delimited_list(services):console.print(_I);return _A
	options=clean_command_dict(options=dict(locals()),keys_to_drop=['pods_client']);pods_client.save_pods_config(options=options)
@pod.command(name='delete',help='Delete a Cloud Pod.')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@click.option('-l',_K,help='Delete only the local Cloud Pod, leaving the remote copy intact',is_flag=_D,default=_A)
@publish_invocation
def cmd_pod_delete(name,local):
	from localstack_ext.bootstrap import pods_client;result=pods_client.delete_pod(pod_name=name,remote=not local)
	if result:console.print(f"Successfully deleted {name}")
	else:console.print(f"[yellow]Could not delete Cloud Pod {name}[/yellow]")
@pod.command(name='commit',help='Commit a snapshot of the LocalStack running instance.')
@click.option('-m',_L,help='Add a comment describing the snapshot.')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@click.option(_G,_J,help='Comma-delimited list of services to push in the pods (all, by default).')
@publish_invocation
def cmd_pod_commit(message,name,services):
	from localstack_ext.bootstrap import pods_client
	if not _is_host_reachable():return
	if services and not is_comma_delimited_list(services):console.print(_I);return _A
	service_list=[x.strip()for x in services.split(',')]if services else _H;pods_client.commit_state(pod_name=name,message=message,services=service_list);console.print('Successfully committed the current state')
@pod.command(name='push',help='Create a new version of a Cloud Pod from the latest snapshot.\nA snapshot is created if it does not exists yet.')
@click.option(_K,'-l',default=_A,is_flag=_D,help='Create the Cloud Pod version only locally, without pushing to remote')
@click.option('-m',_L,help='Add a comment describing the version.')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@click.option(_G,_J,help='Comma-delimited list of services to push in the pods (all by default).')
@click.option('--overwrite',help='Overwrite a version with the content from the latest snapshot of the selected version.',type=bool,default=_A)
@click.option('-v',_M,help='Version to overwrite. Works with `--overwrite`.',type=int)
@click.option('--visibility',help='Set the visibility of the Cloud Pod [`public` or `private`]. Does not create a new version.')
@publish_invocation
def cmd_pod_push(message,name,local,services,overwrite,version,visibility=_H):
	A='public';from localstack_ext.bootstrap import pods_client
	if not _is_host_reachable():return
	if services and not is_comma_delimited_list(services):console.print(_I);return _A
	if visibility:
		if visibility not in[A,'private']:console.print('[red]Error:[/red] Possible values for visibility are `public` and `private`');return
		result=pods_client.set_public(pod_name=name,public=visibility==A)
		if result:console.print(f"Cloud Pod {name} made {visibility}")
		else:console.print('[red]Error:[/red] Visibility change failed')
		return
	service_list=[x.strip()for x in services.split(',')]if services else _H
	if overwrite:
		result=pods_client.push_overwrite(version=version,pod_name=name,comment=message,services=service_list)
		if result:console.print('Successfully overwritten state of version ')
		return
	result=pods_client.push_state(pod_name=name,comment=message,register=not local,services=service_list);console.print('Successfully pushed the current state')
	if not local:
		if result:console.print(f"Successfully registered {name} with remote!")
		else:console.print(f"[red]Error:[/red] Pod with name {name} is already registered")
@pod.command(name='inject',help='Inject the state from a locally available Cloud Pod version into the application runtime.')
@click.option('-v',_M,default='-1',type=int,help='Version to inject (most recent one by default).')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@click.option(_G,_O,help=MergeStrategyPretty.help_message(),default=MergeStrategyPretty.from_merge_strategy(DEFAULT_MERGE_STRATEGY))
@publish_invocation
def cmd_pod_inject(version,name,strategy):
	from localstack_ext.bootstrap import pods_client
	if not _is_host_reachable():return
	if not _cloud_pod_initialized(pod_name=name):return
	merge_strategy=MergeStrategyPretty.to_merge_strategy(strategy)
	if merge_strategy is _H:console.print(_N);return
	result=pods_client.inject_state(pod_name=name,version=version,merge_strategy=merge_strategy)
	if result:console.print('[green]Successfully Injected Pod State[/green]')
	else:console.print('[red]Failed to Inject Pod State[/red]')
@pod.command(name='pull',help='Incorporate the state of a Cloud Pod into the application runtime.')
@click.option(_B,_C,help='Name of the Cloud Pod',cls=required_if_not_cached(_F))
@click.option(_G,_O,help=MergeStrategyPretty.help_message(),default=MergeStrategyPretty.from_merge_strategy(DEFAULT_MERGE_STRATEGY))
@publish_invocation
def cmd_pod_pull(name,strategy):
	from localstack_ext.bootstrap import pods_client
	if not _is_host_reachable():return
	merge_strategy=MergeStrategyPretty.to_merge_strategy(strategy)
	if merge_strategy is _H:console.print(_N);return
	pods_client.pull_state(pod_name=name,merge_strategy=merge_strategy)
@pod.command(name='list',help='List all available Cloud Pods.')
@click.option(_K,'-l',help='List also locally available Cloud Pods.',is_flag=_D,default=_A)
@click.option('--public','-p',help='List all public Cloud Pods.',is_flag=_D,default=_A)
@publish_invocation
def cmd_pod_list_pods(local,public=_A):
	from localstack_ext.bootstrap import pods_client
	if local and public:console.print('[red]Error:[/red]Select only one option between `local` and `public`');return _A
	if public:public_pods=pods_client.list_public_pods();print_table(column_headers=['Cloud Pod'],columns=[public_pods]);return
	pods=pods_client.list_pods(local=local)
	if not pods:console.print(f"[yellow]No pods available {'locally'if local else''}[/yellow]")
	print_table(column_headers=['local/remote','Name'],columns=[['local+remote'if len(locations)>1 else list(locations)[0]for locations in list(pods.values())],list(pods.keys())])
@pod.command(name='versions',help='List all available versions for a Cloud Pod.')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@publish_invocation
def cmd_pod_versions(name):
	from localstack_ext.bootstrap import pods_client
	if not _cloud_pod_initialized(pod_name=name):return
	version_list=pods_client.get_version_summaries(pod_name=name);result='\n'.join(version_list);console.print(result)
@pod.command(name='inspect',help='Inspect the contents of a Cloud Pod.')
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@click.option('-f',_P,help=_Q,default=_R)
@publish_invocation
def cmd_pod_inspect(name,format):
	from localstack_ext.bootstrap import pods_client
	if not _cloud_pod_initialized(pod_name=name):return
	result=pods_client.get_version_metamodel(pod_name=name,version=-1);skipped_services=['cloudwatch']
	for (account,details) in result.items():result[account]={k:v for(k,v)in details.items()if k not in skipped_services}
	TreeRenderer.get(format).render_tree(result)
@pod.command(name='status',help="Lists what Cloud Pods have contributed to each service's current in-memory state.")
@click.option('-v','--verbose',help='Include sequence of state changing Cloud Pod operations in the output.',is_flag=_D,default=_A)
@click.option('-f',_P,help=_Q,default=_R)
@publish_invocation
def cmd_pod_status(verbose,format):from localstack_ext.bootstrap import pods_client;status_response=pods_client.get_status(verbose);norm_status_response=_normalise_status_response_verbose(status_response)if verbose else _normalise_status_response(status_response);TreeRenderer.get(format).render_tree(norm_status_response)
@click.option(_B,_C,help=_E,cls=required_if_not_cached(_F))
@click.option('-t','--target',help='Target directory to export the pod content to.',default='')
@pod.command(name='export',help='Export the Cloud Pod content to a file that can be shared publicly')
@publish_invocation
def cmd_pod_export(name,target):from localstack_ext.bootstrap import pods_client;pods_client.export_pod(pod_name=name,target_dir=target)