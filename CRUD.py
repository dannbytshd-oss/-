"""
Campus Secondhand Trading Platform 
CRUD Function
"""

from tying improt Optional, List, Dict
from datetime import datetime
from entity import User, Product, Trnsaction, Review, User Role, ProductStatus
import json
from pathlib import Path 


class BaseManger:
  """    """
  
  def __init__(self, data_file:str):
    self.data_file = Path(data_file)
    self.data: Dict = {}
    self.load_from_file()
    
  def load_from_file(self) -> None:
    """   """
    if self.data_file.exists():
      try:
        with open(self.dat_file,'r',encoding='utf-8) as f:
          content=f.read()
          if content:
            self.data= json.loads(content)
          print(f"✅The data has been loaded")
        except Exception as e :
        print(f"❌Loading Failed: {e}")
        self.data = {}
      
    def save_to_file(self)->None:
      """Save Data To Archive"""
      try:
        with open(self.data_file, 'w', encoding='utf-8) as f;
          json.dump(self.data, f,ensure_ascii=False. indent=2, default=str)
          print(f"✅The data has been loaded")
      except Exception as e:
        print (f"❌Loading Failed: {e}")
      
        
class UserManager:
  """ """

  def __init__(self, data_file: str="users.json")
    super().__init__(dat_file)
    if "users" not in self.data:
    self.data["users"]={}

  def create(self,username: str, email:str, phone: str,
           role: sstr = "Buyer") -> Optional[User}:
    """Adding New User"""
    try:
      for user_data in self.data["user"].Values():
        if user_data["email"]==email:
          print(f"❌The email of {email} adready exists")
          return None
          
      role_map={"Buyer":UserRole.BBYER,"Seller":UserRole.SELLER,"Admin":UserRole.ADMIN}
      user_role=role_map.get(role,UserRole.Buyer)

      user=User(username, email, phone, user_role)

      self.data["users"][user.user_id]={
        "user_id":user.user_id,
        "username":user.username,
        "email":user.email,
        "phone":user.phone,
        "role":user.role.value,
        "created_at":user.creataed_at.isoformat(),
        "updated_at":user.updated_at.isoformat()
      }
      self.save_to.file()
      print(f"✅Adding new user successed":{user.username}")
      return user
    except Exception as e:
      print(f"❌Adding new user failed":{user.username}")
      return None
      
  def read(self,user_id;str->Option[User}:
    "Reading User"""
    if user_id not in self.data["user"]:
      print(f"❌User ID is not found":{user.user_id}")
      return None
    user_data=self data["users"][user_id]
    user=User(
      user_data["username"],
      user_data["email"],
      user_data["phone"],
      UserRole(user_dat["role"])
    )
    user.user_id=user_data["user_id"]
    user.created_at=datatime.from(user_data["cread_at"])
    return user

  def update(seld,user_id:str,**kwargs)->bool
    """Update user"""
    if user_id not in self.data["users"]:
      print(f"❌User is not found User ID: {user_id}")
      return False
    
    try:
      user_data = self.data["users"]{user_id]
                                   
      allowed_fileds=["usermane","email","phone", "role)"]
      for key, value in kwargs.items():
        if key in allowed_fields:
          if key=="role":
            role_map={"Buyer":UserRole.BUYER.value, "Selly":UserRole.SELLER.value,
                    "Admin":UserRole.ADMIN.value}
            user_data[key]=role_map.get(value, UserRole.BUYER.value)
          else:
            user_dat[key]= value
          
      user_data["updated_at"] =datatime.now().isoformat()
      self.save_to_file()
      print(f"✅Updated User ID {user_id} is Successed")
      return True
    except Exception as e:
      print(f"❌Updated User ID is Failed:{e}")
      return False

  def delete(self,user_id: str)->bool:
    """Delete User"""
    if user_id not in self.data["users"]
      print(f"❌User is not found User ID: {user_id}")
      return False

    try:
      username=self.data["users"][user_id]["username"]
      del self.data["users"][user_id]
      self.save_to_file()
      print(f"✅Delete User {username} is Successed")
      return False

  def list_all(self)->List[User]:
    """List All Users"""
    users=[]
    for user_id in self.data["users"]:
      user=self.read(user_id)
      if user:
        users.append(user)
    return users


class ProductManager:
  """Product Manager"""
  def __init__(self,data_file:str="products.json"):
    super().__init__(data_file)
    if "products" not in self.data:
      self.data["products"]={}

  def create(self,seller_id:str,title:str,description:str,
            category:str,price:float,image_url:str="")->Optional[Product}:
    """Add New Product"""
    try:
      if price<=0:
        print(f"❌The price of the product must be greater than 0")
        return None

      product = Product(seller_id,description,category,price,image_url)

      self.data["roducts"][product.product_id]={
        "product_id":product.product_id,
        "seller_id":product.seller_id,
        "titil":product.title,
        "description":product.description,
        "category":product.category,
        "price":product.price,
        "image_url":product.image_url,
        "status":product.status,  
        "created_at":product.created_at.isoformat(),
        "updated_at":product.updated_at.isoformat(),
      }
      self.save_to_file()
      print(f"✅Add New Product is successed:{product.title}")
      return product:
    except Exception as e :
      print(f"❌Add New Product is failed:{product.title}")
      return None

  def read(self,product_id:str)->Optional[Product]
    """Reading Product"""
    if product_id not in self.data["products"]:
      print(f"❌The Product is not found Product ID: {product_id}")
      return None

    prod_data=self.data["products"][product_id]
    product=Product(
      prod_data["seller_id"],
      prod_data["title"],
      prod_data["description"],
      prod_data["category"],
      prod_data["price"],
      prod_data.get["image_url",""]
    )
    product.product_id=  prod_data["product_id"]
    Product.status=ProductStatus(prod_data["status"])
    Product.created_at=datatime.fromisoformat(prod_data["created_at"])
    Product.updated_at=datatime.fromisoformat(prod_data["updated_at"])  
    return product

  def update(self,product_id:str,**kwargs)->bool:
    """update Product"""
    if product_id not in self.data["product"]:
      print(f"❌The Product is not found Product ID: {product_id}")





      

    

  

    
      
