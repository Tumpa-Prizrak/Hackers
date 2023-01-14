import database as db
import peewee as pw


def enter(data):
    try:
        login=input("login: ")
        password=input("password: ")
        accaunt = db.User.select().where(db.User.login==login, db.User.password==password, db.User.guild_id==data["guild_id"], db.User.discord_id==data["discord_id"]).dicts().execute()[0]
        if not accaunt:
            raise pw.IntegrityError
        data.update({"user": accaunt, "logged": True})
    except (pw.IntegrityError, IndexError) as e:
        print("Incorect login or password")
