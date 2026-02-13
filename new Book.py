class book:
  def __init__(self, book_id, title, author, seller_id, price, status)
    self.book_id = book_id
    self.title = title
    self.author = author
    self.seller_id = seller_id
    self.price = round(price, 1)
    self.status = status

   def __init__(self)
    self.__book_list = []

 def add_book(self, book)
    """Add A New Book To The Book List"""
    try:
      self.book__book_list.append(book) 
      print(f"✅Adding New Book Is Successed":{book.book_id}")
        return buyer
    except Error:
      print(f"❌Adding New Book Is Failed":{book.book_id}")
      return False

  def remove_book(self, book)
    """Remove A Book From The Book List"""
    try:
      self.book__book_list.append(book)
      print(f"✅Remove A Book Is Successed":{book.book_id}")
      return True
    except Error:
      print(f"❌Remove A Book Is Failed":{book.book_id}")
      return False
