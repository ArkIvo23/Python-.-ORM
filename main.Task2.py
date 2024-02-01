import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine('postgresql://postgres:postgres@localhost:5432/ORMDB')
Base = declarative_base()



class Book(Base):
   __tablename__ = 'books'
   id = Column(Integer, primary_key=True)
   title = Column(String)
   publisher_id = Column(Integer, ForeignKey('publishers.id'))
   publisher = Relationship('Publisher', backref='books')



class Shop(Base):
   __tablename__ = 'shops'
   id = Column(Integer, primary_key=True)
   name = Column(String)



class Sale(Base):
   __tablename__ = 'sales'
   id = Column(Integer, primary_key=True)
   book_id = Column(Integer, ForeignKey('books.id'))
   shop_id = Column(Integer, ForeignKey('shops.id'))
   date = Column(DateTime)
   price = Column(Integer)


Session = sessionmaker(bind=engine)
session = Session()


def get_shops_by_publisher(publisher_name):
   publisher = session.query(Publisher).filter(Publisher.name == publisher_name).first()
   shops = publisher.shops
   return shops

def print_sales(shops):
   for shop in shops:
       sales = session.query(Sale).filter(Sale.shop_id == shop.id).all()
       for sale in sales:
           print(f"{sale.book.title} | {shop.name} | {sale.price} | {sale.date}")


shops = get_shops_by_publisher(input("Введите имя или идентификатор издателя: "))


print_sales(shops)
