from lib2to3.pgen2.token import OP
import click
from tabulate import tabulate
from . import pybis
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys


def login_options(func):
    options = [
        click.argument("hostname"),
        click.option("-u", "--username", help="Username"),
        click.option(
            "--verify-certificate",
            is_flag=True,
            default=True,
            help="Verify SSL certificate of openBIS host",
        ),
    ]
    # we use reversed(options) to keep the options order in --help
    for option in reversed(options):
        func = option(func)
    return func


def get_openbis(hostname=None, session_token_needed=False, **kwargs):
    """Order of priorities:
    1. direct specification via --hostname https://openbis.domain
    2. Environment variable: OPENBIS_HOST=https://openbis.domain
    3. local pybis configuration (hostname.pybis.json)
    4. local obis configuration (in .obis)
    5. global pybis configuration (~/.pybis/hostname.pybis.json)
    6.
    """

    config = pybis.get_local_config()

    if not hostname:
        hostname = config.get("hostname")
        if not hostname:
            hostname = click.prompt("openBIS hostname:")

    token = pybis.get_token_for_hostname(
        hostname, session_token_needed=session_token_needed
    )
    openbis = pybis.Openbis(
        url=hostname,
        verify_certificates=kwargs.get("verify_certificate", True),
    )
    if token:
        try:
            openbis.set_token(token)
            return openbis
        except Exception:
            pass

    if not kwargs.get("username"):
        kwargs["username"] = click.prompt("Username")
    if not kwargs.get("password"):
        kwargs["password"] = click.prompt("Password", hide_input=True)
    try:
        openbis.login(
            username=kwargs["username"],
            password=kwargs["password"],
            save_token=True,
        )
        return openbis
    except ValueError as exc:
        click.echo(f"Failed to login to {hostname}")


@click.group()
def cli():
    """pybis - command line access to openBIS"""


@cli.command("sample")
@click.argument("identifier", required=True)
def get_sample(identifier):
    """get a sample by its identifier or permId"""


@cli.command("dataset")
@click.argument("identifier", required=True)
@click.option("--download", "-l", is_flag=True, help="download the dataset")
def get_sample(identifier, download):
    """get a dataset by its identifier or permId"""


@cli.command("local", context_settings=dict(ignore_unknown_options=True))
@click.argument("hostname", required=False)
@click.argument("token", required=False, type=click.UNPROCESSED)
@click.option("--info", is_flag=True, help="get more detailed information")
def get_set_hostname(hostname, token, info):
    """show or set hostname and token that is used locally."""
    if hostname:
        if token and token.startswith("-"):
            token = "$pat" + token
        pybis.set_local_config(hostname=hostname, token=token)
    else:
        # get hostname and token stored in .pybis.json
        config = pybis.get_local_config()
        if info:
            o = pybis.Openbis(url=config.get("hostname", ""))
            session_info = o.get_session_info(token=config.get("token"))
            click.echo(session_info)
        else:
            click.echo(
                tabulate(
                    [[config.get("hostname", ""), config.get("token", "")]],
                    headers=["openBIS hostname", "token"],
                )
            )


@cli.group()
@click.pass_obj
def token(ctx):
    """manage openBIS tokens"""
    pass


@token.command("pats")
@click.argument("hostname", required=False)
@click.argument("session-name", required=False)
@click.pass_obj
def get_pats(ctx, hostname, session_name=None):
    """list stored openBIS Personal Access Tokens (PAT)"""
    tokens = pybis.get_saved_pats(hostname=hostname, sessionName=session_name)
    headers = ["hostname", "permId", "sessionName", "validToDate"]
    token_list = [[token[key] for key in headers] for token in tokens]
    click.echo(
        tabulate(
            token_list,
            headers=[
                "openBIS hostname",
                "personal access token",
                "sessionName",
                "valid until",
            ],
        )
    )


@token.command("session")
@click.pass_obj
def new_token(ctx, **kwargs):
    """create new openBIS Session Token"""
    click.echo("new_token()")


@token.command("sessions")
@click.pass_obj
def get_tokens(ctx, **kwargs):
    """list stored openBIS Session Tokens"""
    tokens = pybis.get_saved_tokens()
    token_list = [[key, tokens[key]] for key in tokens]
    click.echo(tabulate(token_list, headers=["openBIS hostname", "session token"]))


@token.command("pat")
@login_options
@click.argument("session-name")
@click.option("--validity-days", help="Number of days the token is valid")
@click.option("--validity-weeks", help="Number of weeks the token is valid")
@click.option("--validity-months", help="Number of months the token is valid")
@click.pass_obj
def new_pat(ctx, hostname, session_name, **kwargs):
    """create new openBIS Personal Access Token"""
    validTo = datetime.now()
    if kwargs.get("validity_months"):
        validTo += relativedelta(months=int(kwargs.get("validity_months")))
    elif kwargs.get("validity_weeks"):
        validTo += relativedelta(weeks=int(kwargs.get("validity_weeks")))
    elif kwargs.get("validity_days"):
        validTo += relativedelta(days=int(kwargs.get("validity_days")))
    else:
        validTo += relativedelta(years=1)
    o = get_openbis(hostname, session_token_needed=True, **kwargs)
    try:
        new_pat = o.new_personal_access_token(sessionName=session_name, validTo=validTo)
    except Exception as exc:
        raise click.ClickException(
            f"Creation of new personal access token failed: {exc}"
        )
    click.echo(new_pat)
    o.get_personal_access_tokens(save_to_disk=True)


if __name__ == "__main__":
    cli()
