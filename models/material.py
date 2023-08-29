from init import db, ma

class Material(db.Model):
    __tablename__= "materials"

    id = db.Column(db.Integer, primary_key=True)
    material_name = db.Column(db.String(50))


class MaterialSchema(ma.Schema):
    
    class Meta:
        fields = ('id', 'material_name')

material_schema= MaterialSchema()
materials_schema=MaterialSchema(many=True)