from flask.cli import AppGroup
from .users import seed_users, undo_users
from .portfolio_stocks import seed_portfolio_stocks, undo_portfolio_stocks
from .watchlist_stocks import seed_watchlist, undo_watchlist
# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_portfolio_stocks()
    seed_watchlist()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_portfolio_stocks()
    undo_watchlist()
    # Add other undo functions here
