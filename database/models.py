from typing import Optional
import peewee as pw
from random import randint

db = pw.SqliteDatabase("database\\mysqldb.db")  # type: ignore


class User(pw.Model):
    id_ = pw.AutoField(column_name="id")
    guild_id = pw.IntegerField(column_name="guild_id")
    discord_id = pw.IntegerField(column_name="discord_id", unique=True)
    ip = pw.TextField(column_name="ip", unique=True)
    login = pw.TextField(column_name="login", unique=True)
    password = pw.TextField(column_name="password")

    def create_new(self, guild_id: int, discord_id: int, login: str, password: str, ip: Optional[str] = None):
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
