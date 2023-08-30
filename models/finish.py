from init import db, ma

class Finish(db.Model):
    __tablename__= "finishes"

    id = db.Column(db.Integer, primary_key=True)
    finish_name = db.Column(db.String(50))

    product_images = db.relationship('ProductImage', back_populates='finishes',cascade='all, delete')

class FinishSchema(ma.Schema):
    
    class Meta:
        fields = ('id', 'finish_name')

finish_schema= FinishSchema()
finishes_schema=FinishSchema(many=True)