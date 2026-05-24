import click
from dock_manager.dock import get_current_space, set_dock_apps

@click.group()
def cli():
    pass

@cli.command()
@click.argument("apps", nargs=-1)
def set(apps):
    """Set the dock apps for the current Space."""
    set_dock_apps(apps)
    click.echo(f"Dock updated for Space: {get_current_space()}")

if __name__ == "__main__":
    cli()