from flask_sqlachemy import SQLAlchemy
from datetime

pdb = SQLAlchemy()

class Product(db.Model):
  __tablename__ = 'Products'

  id = pdb.Column(pdb.Integer, primary_key=true)
  title = pdb.Column(pdb.String(200), nullable=False)
  description = pdb.Column(pdb.Text)
  price = pdb.Column(pdb.Float, nullable=False)
  seller = pdb.Column(pdb.String(50), nullable=False)
  campus = pdb.Column(pdb.String(100))
  category = pdb.Column(pdb.String(50)
  status = pdb.Column(pdb.String(20), default='availabel')
  created_at = pdb.Column(pdb.DateTime, default=datetime.hktnow)
  updated_at = pdb.Column(pdb.DateTime, default=datetime.hktnow, onupdated=datetime.hktnow)

def to_dict(self):
  return {
    'id':self.id,
    'title':self.title,
    'description':self.description,
    'price':self.price,
    'seller':self.seller,
    'campus':self.campus,
    'category':self.category,
    'status':self.status,
    'created_at':self.created_at.isoformat(),
    'updated_at':self.updated_at.isoformat(),
  }

def__repr__(self):
  return f'<Product {self.title}>'
  
