"""
Campus Secondhand Trading Platform 
CRUD Function
"""
from tying improt Optional, List, Dict
from datetime import datetime
from entity import User, Product, Trnsaction, Review, User Role, ProductStatus
import json
from pathlib import Path 

class:
  """    """
  def__init__(self, data_file:str):
    self.data_file = Path(data_file)
    self.data: Dict = {}
    self.load_from_file()
    
  defload_from_file(self) -> None:
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
  """
