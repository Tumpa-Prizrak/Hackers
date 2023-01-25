from typing import Optional
import peewee as pw
from random import randint

db = pw.SqliteDatabase("database\\mysqldb.db")  # type: ignore


class User(pw.Model):
    """
    Encapsulate the behaviour of User.

    Attributes
    ----------
    id_: int
    guild_id: int
    discord_id: int
    ip: str
    login: str
    password: str

    Methods
    -------
    create_new(self, guild_id: int, discord_id: int, login: str, password: str, ip: Optional[str] = None)
        Creates new user in database.
    """
    id_ = pw.PrimaryKeyField(column_name="id")
    guild_id = pw.IntegerField(column_name="guild_id")
    discord_id = pw.IntegerField(column_name="discord_id", unique=True)
    ip = pw.TextField(column_name="ip", unique=True)
    login = pw.TextField(column_name="login", unique=True)
    password = pw.TextField(column_name="password")

    def create_new(self, guild_id: int, discord_id: int, login: str, password: str, ip: Optional[str] = None) -> None:
        """
        Creates new user in database.

        Parameters
        ----------
        guild_id: int
            Guild ID of user.
        discord_id: int
            Discord ID of user.
        login: str
            Login of user.
        password: str
            Password of user.
        ip: Optional[str]
            IP of user.

        Returns
        -------
        None
        """
        egg = 100
        while True:
            try:
                spam = randint(0, len(str(guild_id)))
                ip_ = f"1.1.{str(guild_id)[spam:spam + 3]}.{randint(2, egg)}" if ip is None else ip
                self.create(
                    guild_id=guild_id,
                    discord_id=discord_id,
                    ip=ip_,
                    login=login,
                    password=password
                )
                self.save()
                break
            except pw.IntegrityError as e:
                print(e)
                if e.args[0].endswith("discord_id"):
                    raise e
                egg += 100
                continue

    class Meta:
        database: pw.SqliteDatabase = db
        table_name: str = "users"


class FileManagerObject(pw.Model):
    previous = pw.TextField(column_name="previous")
    name = pw.TextField(column_name="name", unique=True)
    is_file = pw.BooleanField(column_name="isfile")

    def create_new(self, previous: str, name: str, is_file: bool):
        self.create(
            previous=previous,
            name=name,
            is_file=is_file,
        )
        self.save()

    def __str__(self) -> str:
        return "" if self.previous is None else "/" + self.name

    class Meta:
        database: pw.SqliteDatabase = db
        table_name: str = "directories"

