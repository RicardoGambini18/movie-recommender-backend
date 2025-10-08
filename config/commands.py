import click
from flask.cli import with_appcontext
from commands import seed, data_download, data_update


@click.command('seed')
@with_appcontext
def seed_command():
    seed()


@click.command('data:download')
@with_appcontext
def data_download_command():
    data_download()


@click.command('data:update')
@with_appcontext
def data_update_command():
    data_update()


def register_commands(app):
    app.cli.add_command(seed_command)
    app.cli.add_command(data_update_command)
    app.cli.add_command(data_download_command)
