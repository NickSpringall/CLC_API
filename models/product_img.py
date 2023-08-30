from init import db, ma
from marshmallow import fields

class ProductImg(db.Model):
    __tablename__= "product_images"

    id = db.Column(db.Integer, primary_key=True)
    pair = db.Column(db.Boolean, nullable=False)
    img_link = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    alt_text = db.Column(db.String(100))

    finish_id = db.Column(db.Integer,db.ForeignKey('finishes.id'))
    finish = db.relationship('Finish',back_populates='product_images', cascade='all, delete') 

    material_id = db.Column(db.Integer,db.ForeignKey('materials.id'))
    material = db.relationship('Material',back_populates='product_images', cascade='all, delete')

    fixture_id = db.Column(db.Integer,db.ForeignKey('fixtures.id'))
    fixture = db.relationship('Fixture', back_populates='product_images', cascade='all, delete')
    


class ProductImageSchema(ma.Schema):
    finish = fields.Nested('FinishSchema')
    material = fields.Nested('MaterialSchema')
    fixture = fields.Nested('Fixture')
    
    class Meta:
        fields = ('id', 'pair', 'image_link', 'description', 'alt_text', 'finish', 'material', 'fixture')

product_image_schema= ProductImageSchema()
product_images_schema=ProductImageSchema(many=True)