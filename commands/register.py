import database as db
import peewee as pw


def enter(data: dict) -> None:
    """
    Creates a new user
    """
    try:
        db.User().create_new(
            guild_id=data["guild_id"],
            discord_id=data["discord_id"],
            login=input("login: "),
            password=input("password: ")
        )
        print('You created a new user! type "login" to login into it')
    except pw.IntegrityError:
        print("This login is already taken")
