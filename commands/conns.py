import database as db


def enter(data: dict):
    """
    Print the list of users ip at local network.
    Usage: conns
    """
    users = list(db.User.select(db.User.ip).where(db.User.guild_id == data['guild_id']).tuples().execute())
    print("List of ip's at local network:")
    for i in users:
        print(i[0])
