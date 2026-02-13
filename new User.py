class Seller:
  def __init__(self, username, user_id, email):
    self.name = name
    self.user_id = user_id
    self.email = email

  def __init__(self)
    self.__seller_list = []

  def add_seller(self, seller)
    """Add A New Seller To The Seller List"""
    try:
      self.seller__seller_list.append(seller) 
      print(f"✅Adding New Seller Is Successed.\n":{seller.username}")
        return seller
    except Error:
      print(f"❌Adding New Seller Is Failed.\n":{seller.username}")
      return None

  def remove_seller(self, seller)
    """Remove A Seller From The Seller List"""
    try:
      self.seller__seller_list.append(seller)
      print(f"✅Remove A Seller Is Successed.\n":{seller.username}")
      return True
    except Error:
      print(f"❌Remove A Seller Is Failed.\n":{seller.username}")
      return None
      
class Buyer:
  def __init__(self, username, user_id, email):
    self.name = name
    self.user_id = user_id
    self.email = email

  def __init__(self)
    self.__buyer_list = []

  def add_buyer(self, buyer)
    """Add A New Buyer From The Buyer List"""
    try:
      self.buyer__buyer_list.append(buyer) 
      print(f"✅Adding New buyer Is Successed.\n":{buyer.username}")
        return buyer
    except Error:
      print(f"❌Adding Newbuyer Is Failed.\n":{buyer.username}")
      return False

  def remove_buyer(self, buyer)
    """Remove A Buyer From The Buyer List"""
    try:
      self.seller__seller_list.append(buyer)
      print(f"✅Remove A Buyer Is Successed.\n":{buyer.username}")
      return True
    except Error:
      print(f"❌Remove A Buyer Is Failed.\n":{buyer.username}")
      return False
  
