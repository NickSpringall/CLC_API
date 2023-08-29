from flask import Blueprint
from init import db, bcrypt
from models.material import Material

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables Created")


@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print('Tables Dropped')

# @db_commands.cli.command('seed')
# def seed_db():