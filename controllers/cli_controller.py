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

@db_commands.cli.command('seed')
def seed_db():
    materials = [
        Material(
            material_name="Blackwood"
        ),
        Material(
            material_name="QLD Walnut"
        ),
        Material(
            material_name="Maple"
        ),
        Material(
            material_name="Blue Gum"
        ),
         Material(
            material_name="Cotton"
         ),
    ]
    
    db.session.add_all(materials)
    db.session.commit()

    print('Tables Seeded')