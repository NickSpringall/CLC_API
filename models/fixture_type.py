from init import db, ma

class Fixture(db.Model):
    __tablename__= "fixture_type"

    id = db.Column(db.Integer, primary_key=True)
    fixture_type = db.Column(db.String(50))


class FixtureSchema(ma.Schema):
    
    class Meta:
        fields = ('id', 'fixture_type')

fixture_schema= FixtureSchema()
fixture_schema=FixtureSchema(many=True)