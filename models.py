import peewee
from datetime import datetime
from peewee import *
db = SqliteDatabase("sqlite3.db")
class Message(Model):
    create_at = DateTimeField(default=datetime.now)
    text = CharField()
    class Meta:
        database = db
db.connect()
db.create_tables([Message])
