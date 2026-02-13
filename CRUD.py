"""
Campus Second-Hand Book Trading Platform (COMP 2090SEF Group Assignment)
CRUD Function
"""

from tying improt Optional, List, Dict
from datetime import datetime
import json
from pathlib import Path 


class BaseFunction:
  """BaseManagement"""
  
  def __init__(self, data_file:str):
    self.data_file = Path(data_file)
    self.dataDict = {}
    self.load_from_file()
    
  def load_from_file(self) -> None:
    """Load From File"""
    if self.data_file.exists():
      try:
        with open(self.data_file,'r', encoding='utf-8) as f:
          content=f.read()
          if content:
            self.data= json.loads(content)
          print(f"✅The Data Has Been loaded")
        except Exception as e:
          print(f"❌Loading Failed: {e}")
          self.data = {}
      
    def save_to_file(self)->None:
      """Save Data To File"""
      try:
        with open(self.data_file, 'w', encoding='utf-8) as f;
          json.dump(self.data, f,ensure_ascii=False. indent=2, default=str)
          print(f"✅The Data Has Been Loaded")
      except Exception as e:
        print (f"❌Loading Failed: {e}")
      
        
class User:
  """User """

  def __init__(self, data_file: str="users.json")
    super().__init__(dat_file)
    if "users" not in self.data:
    self.data["users"]={}

  def create(self,username: str, email:str,
           role: str = "Buyer") -> Optional[User}:
    """Adding New User"""
    try:
      for user_data in self.data["user"].Values():
        if user_data["email"]==email:
          print(f"❌The Email Of {email} Adready Exists")
          return None
          
      role_map={"Buyer":UserRole.BBYER,"Seller":UserRole.SELLER,"Admin":UserRole.ADMIN}
      user_role=role_map.get(role,UserRole.Buyer)

      user=User(username, email, user_role)

      self.data["users"][user.user_id]={
        "user_id":user.user_id,
        "username":user.username,
        "email":user.email,
        "role":user.role.value,
        "created_at":user.creataed_at.isoformat(),
        "updated_at":user.updated_at.isoformat()
      }
      self.save_to.file()
      print(f"✅Adding New User Successed":{user.username}")
      return user
    except Exception as e:
      print(f"❌Adding New User Failed":{user.username}")
      return None
      
  def read(self,user_id;str->Option[User}:
    "Read User"""
    if user_id not in self.data["user"]:
      print(f"❌User ID Is Not Found":{user.user_id}")
      return None
    user_data=self data["users"][user_id]
    user=User(
      user_data["username"],
      user_data["email"],
      UserRole(user_data["role"])
    )
    user.user_id=user_data["user_id"]
    user.created_at=datatime.from(user_data["created_at"])
    user.updated_at=datatime.from(user_data["updated_at"])
    return user

  def update(seld,user_id:str,**kwargs)->bool
    """Update user"""
    if user_id not in self.data["users"]:
      print(f"❌User Is Not Found User ID: {user_id}")
      return False
    
    try:
      user_data = self.data["users"]{user_id]
                                   
      allowed_fileds=["usermane","email","phone"]
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
      print(f"✅Updated User ID {user_id} Is Successed")
      return True
    except Exception as e:
      print(f"❌Updated User ID Is Failed:{e}")
      return False

  def delete(self,user_id: str)->bool:
    """Delete User"""
    if user_id not in self.data["users"]
      print(f"❌User Is Not Found User ID: {user_id}")
      return False

    try:
      username=self.data["users"][user_id]["username"]
      del self.data["users"][user_id]
      self.save_to_file()
      print(f"✅Delete User {username} Is Successed")
      return False

  def list_all(self)->List[User]:
    """List All Users"""
    users=[]
    for user_id in self.data["users"]:
      user=self.read(user_id)
      if user:
        users.append(user)
    return users


class BookManagement:
  """Book Management"""
  def __init__(self,data_file:str="books.json"):
    super().__init__(data_file)
    if "books" not in self.data:
      self.data["books"]={}

  def create(self,seller_id:str,title:str,description:str,
            category:str,price:float,image_url:str="")->Optional[Product}:
    """Add New Book"""
    try:
      if price<=0:
        print("❌The Price Of The Book Must Be Greater Than 0")
        return None

      book = Book(seller_id,description,category,price)

      self.data["books"][book.book_id]={
        "book_id":book.book_id,
        "seller_id":book.seller_id,
        "titil":book.title,
        "description":book.description,
        "category":book.category,
        "price":book.price,
        "status":book.status,  
        "created_at":book.created_at.isoformat(),
        "updated_at":book.updated_at.isoformat(),
      }
      self.save_to_file()
      print(f"✅Add New Book Is Successed:{book.title}")
      return book:
    except Exception as e :
      print(f"❌Add New Book Is Failed:{book.title}")
      return None

  def read(self,book_id:str)->Optional[Book]
    """Read Book"""
    if product_id not in self.data["books"]:
      print(f"❌The Book is not found book ID: {book_id}")
      return None

    book_data=self.data["books"][book_id]
    book=Book(
      book_data["seller_id"],
      book_data["title"],
      book_data["description"],
      book_data["category"],
      book_data["price"]
    )
    book.book_id=book_data["book_id"]
    Book.status=BookStatus(prod_data["status"])
    Book.created_at=datatime.fromisoformat(book_data["created_at"])
    Book.updated_at=datatime.fromisoformat(book_data["updated_at"])  
    return product

  def update(self,book_id:str,**kwargs)->bool:
    """Update Book"""
    if book_id not in self.data["books"]:
      print(f"❌The Book is not found Book ID: {book_id}")
      return False

    try:
      book_data=self.data["books"][book_id]

      allowed_fields = ["title","description","category","price","status"]
      for key, value in kwargs.items():
        if key in allowed_fields:
          if key=="price" and value<=0:
            print("❌The Price Of The Book Must Be Greater Than 0")
            return False

          if key=="status":
            statis_map={
              "Active":BookStatus.ACTIVE.value,
              "Sold":BookStatus.SOLD.value, 
              "Removed":BookStatus.REMOVED.value,
            }
            book_data[key]=value
          else:
            book_data[key]=value

      book_data["updated_at"]=datetime.now().isoformat()
      self.save_to_file()
      print(f"✅Updated Book {book_id} Is Successed")
      return True
    except Exception as e:
      print(f"❌Updated Book {book_id} Is Failed")
      return False

  def delete(self, book_id:str)->bool:
    """Delete Book"""
    if book_id not in self.data["books"]:
      print(f"❌The Book is not found Book ID: {book_id}")
      return False

    try:
      title=self.data["books"][book_id]["title"]
      del self.data["books"][book_id]
      self.save_to_file()
      print(f"✅Delet Book {title} is successed")
      return True
    except Exception as e:
      print(f"❌Delet Book is failed: {r}")
      return False

  def list_all(self)->List[Book]:
    """List All Books"""
    books=[]
    for Book_id in self.data["books"]:
        book=self.read(book_id)
        if book:
          book.append(book)
    return book
  
  def list_by_seller(self,seller_id:str)->List[Product]:
    """List Books From A Specified Seller"""
    return[p for p in self.list_all() if p.seller_id==seller_id]

  def search(self,keyword:str)->List[Book]:
    """Search For Products"""
    keyword_lower=keyword.lower()
    return[p for p in self.list_all() 
           if keyword_lower in p.title.lower() or keyword_lower in p.category.lower()]


class OrderManagement:
  """Order Management"""
  def __init__(self,data_file:str="orders.jspm"):
    super().__init__(data_file)
    if "orders" not in self.data:
      self.data["orders"]={}

  def create(seld,buyer_id:str,seller_id:str,book_id: str,
            amount:float)->Optional[Order]:
      """Add New Order"""
      try:
        if amount<=0:
          print("❌The Order Amount Must Be Greater Than 0")
          return None

        order=Order(buyer_id,seller_id,book_id,amount)

        self.data["order"][order.order_id]={
        "order_id"order.order_id,
        "buyer_id":order.buyer_id,
        "seller_id":order.seller_id,
        "book_id":order.book_id,
        "amount":order.amount,
        "status":order.status,  
        "created_at":order.created_at.isoformat(),
        "updated_at":order.updated_at.isoformat(),
        }
        self.save_to_file()
        print(f"✅The Order Is successed:${amount}")
        return order
      except Exception as e:
        print(f"❌The Order Is Failed:${amount}")
        return None

  def read(self,order_id:str)->Optional[Order]
    """Read Order"""
    if transsaction_id not in self.data["orders"]
      print(f"❌Order Is Not Found Order ID: {order_id}")
      return None

    order_data=self.data["orders"][order_id]
    order=Order(
      order_data["buyer_id"]
      order_data["seller_id"]
      order_data["product_id"]
      order_data["amount"]
    )
    order.order_id=order_data["order_id"]
    order.status=order_data["status"]
    order.created_at=order_data["created_at"]
    order.updated_at=order_data["updated_at"]
    return order

  def update(self, order_id:str,**kwargs)->bool:
    """Update Order Status"""
    if order_id not in self.data["orders"]:
      print(f"❌The Order Is Not Found Order ID: {order_id}")
      return False

    try:
      order_data=self.data["order"]:
      
      allowed_fields = ["status"]
      for key, value in kwargs.items():
        if key in allowed_fields:
          order_data[key]=value

      order_data["updated_at"]=datetime.now().isoformat()
      self.save_to_file()
      print(f"✅Update Order {order_id} Is Successed")
      return True
    except Exception as e:
      print(f"❌Update Order {order_id} Is Failed")
      return False

  def delete(self, book_id:str)->bool:
    """Delete Order"""
    if order_id not in self.data["orders"]:
      print(f"❌The Book Is Not Found Order ID: {order_id}")
      return False

    try:
      del self.data["orders"][order_id]
      self.save_to_file()
      print(f"✅Delet Order {title} Is Successed")
      return True
    except Exception as e:
      print(f"❌Delet Order Is Failed: {e}")
      return False

  def list_all(self)->List[Order]:
    """List All Orders"""
    orders=[]
    for order_id in self.data["orders"]:
        order=self.read(order_id)
        if orders:
          order.append(orders)
    return orders
  
  def list_by_seller(self,buyer_id:str)->List[Order]:
    """List The Buyer Orders"""
    return[t for t in self.list_all() if t.buyer_id==buyer_id]

  def search(self,keyword:str)->List[Book]:
    """Search Seller Order"""
    return[t for t in self.list_all() if t.seller_id==seller_id]
          
          

   

  


      





      

    

  

    
      
