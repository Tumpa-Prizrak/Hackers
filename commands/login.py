import database as db
import peewee as pw
from typing import Optional


def _login(login: Optional[str] = None, password: Optional[str] = None) -> tuple[str, str]:
    """
    Takes login and password from input or from parameters.

    Parameters
    ----------
    login: str
        User login.
    password: str
        User password.

    Returns
    -------
    tuple[str, str]
        User login and password.

    """
    if not all((login, password)):
        login = input("login: ")
        password = input("password: ")

    return login, password  # type: ignore


def enter(data, login: Optional[str] = None, password: Optional[str] = None):
    """
    Check user login and password.
    Usage: login [login] [password]
    """
    try:
        login, password = _login(login, password)

        account = db.User.select().where(db.User.login == login, db.User.password == password,
                                         db.User.guild_id == data["guild_id"],
                                         db.User.discord_id == data["discord_id"]).dicts().execute()[0]
        if not account:
            raise pw.IntegrityError
        data.update({"user": account, "logged": True})
    except (pw.IntegrityError, IndexError):
        print("Incorrect login or password")
