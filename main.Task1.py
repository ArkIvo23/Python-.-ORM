from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine("postgresql://postgres:postgres@localhost:5432/ORMDB1")
metadata = MetaData()


class Publisher(metadata.Table):
    __tablename__="Publishers"
    id = Column(Integer, promary_key=True)
    name = Column(String)


class Book (metadata.Table):
    __tablename__="books"
    id = Column(Integer, primaty_key=True)
    title = Column(String)
    Publisher_id = Column(Integer, Foreignkey("publisher.id"))
    Publisher = Relationship("Publisher", backref = "books")


class Stock(metadata.Table):
    __tablename__ = "stock"
    id = Column(Integer, primary_ley = True)
    book_id = Column(Integer, Foreignkey("books.id"))
    shop_id = Column(Integer, Foreignkey("shops.id"))
    count = Column(Integer)
    book = Relationship("Book",backref="stock")
    shop = Relationship("Shop", backref="stock")
    
     
class Shop(metadata.Table):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
class Sale(metadata.Table):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    stock = Relationship('Stock', backref='sales')
    count = Column(Integer)

session = Session()


publisher1 = Publisher(name='Publisher 1')
publisher2 = Publisher(name='Publisher 2')
session.add(publisher1)
session.add(publisher2)

book1 = Book(title='Book 1', publisher=publisher1)
book2 = Book(title='Book 2', publisher=publisher2)
session.add(book1)
session.add(book2)

shop1 = Shop(name='Shop 1')
shop2 = Shop(name='Shop 2')
session.add(shop1)
session.add(shop2)

stock1 = Stock(book_id=book1.id, shop_id=shop1.id, count=10)
stock2 = Stock(book_id=book2.id, shop_id=shop2.id, count=5)
session.add(stock1)
session.add(stock2)

sale1 = Sale(date=datetime.datetime(2022, 1, 1), stock_id=stock1.id, count=5)
sale2 = Sale(date=datetime.datetime(2022, 2, 1), stock_id=stock2.id, count=3)
session.add(sale1)
session.add(sale2)

session.commit()

books = session.query(Book).join(Publisher).join(Stock).join(Shop)
for book in books:
    print(book.title, book.publisher.name, book.stock.shop.name)