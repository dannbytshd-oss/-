"""
Campus Second-Hand Book Trading Platform 
CRUD Function
"""

from tying improt Optional, List, Dict
from datetime import datetime
from entity import User, Book, Transaction, UserRole, BookStatus
import json
from pathlib import Path 


class Base Management:
  """Base Management"""
  
  def __init__(self, data_file:str):
    self.data_file = Path(data_file)
    self.data: Dict = {}
    self.load_from_file()
    
  def load_from_file(self) -> None:
    """Load From File"""
    if self.data_file.exists():
      try:
        with open(self.data_file,'r',encoding='utf-8) as f:
          content=f.read()
          if content:
            self.data= json.loads(content)
          print(f"✅The Data Has Been loaded")
        except Exception as e :
        print(f"❌Loading Failed: {e}")
        self.data = {}
      
    def save_to_file(self)->None:
      """Save Data To File"""
      try:
        with open(self.data_file, 'w', encoding='utf-8) as f;
          json.dump(self.data, f,ensure_ascii=False. indent=2, default=str)
          print(f"✅The Data has Been Loaded")
      except Exception as e:
        print (f"❌Loading Failed: {e}")
      
        
class UserManagement:
  """User Management"""

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
    "Reading User"""
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
      print(f"✅Updated User ID {user_id} is Successed")
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
  def __init__(self,data_file:str="book.json"):
    super().__init__(data_file)
    if "books" not in self.data:
      self.data["books"]={}

  def create(self,seller_id:str,title:str,description:str,
            category:str,price:float,image_url:str="")->Optional[Product}:
    """Add New Product"""
    try:
      if price<=0:
        print("❌The Price Of The Book Must Be Greater Than 0")
        return None

      book = Book(seller_id,description,category,price)

      self.data["roducts"][book.book_id]={
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
    Book.status=ProductStatus(prod_data["status"])
    Book.created_at=datatime.fromisoformat(book_data["created_at"])
    Book.updated_at=datatime.fromisoformat(book_data["updated_at"])  
    return product

  def update(self,product_id:str,**kwargs)->bool:
    """update Product"""
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
              "Active":ProductStatus.ACTIVE.value,
              "Sold":ProductStatus.SOLD.value, 
              "Removed":ProductStatus.REMOVED.value,
            }
            book_data[key]=value
          else:
            book_data[key]=value

      book_data["updated_at"]=datetime.now().isoformat()
      self.save_to_file()
      print(f"✅Updated Book {book_id} is successed")
      return True
    except Exception as e:
      print(f"❌Updated Book {book_id} is failed")
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


class TransactionManagement:
  """Transaction Management"""
  def __init__(self,data_file:str="tramsactopms.jspm"):
    super().__init__(data_file)
    if "transactions" not in self.data:
      self.data["transactions"]={}

  def create(seld,buyer_id:str,seller_id:str,book_id: str,
            amount:float)->Optional[Transaction]:
      """Add New Transaction"""
      try:
        if amout<=0:
          promt
    



      





      

    

  

    
      
