from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import or_

engine = create_engine('postgresql://postgres:postgres@localhost:5432/ORMDB')
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    publisher = relationship('Publisher', backref='books')


class BookStore(Base):
    __tablename__ = 'bookstores'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship('Book', backref='sales')
    shop_id = Column(Integer, ForeignKey('shops.id'))
    shop = relationship('Shop', backref='sales')
    date = Column(DateTime)
    price = Column(Integer)

class PublisherShop(Base):
    __tablename__ = 'publisher_shops'
    id = Column(Integer, primary_key=True)
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    shop_id = Column(Integer, ForeignKey('shops.id'))


Session = sessionmaker(bind=engine)
session = Session()


def get_shops(publisher_input):
    publisher = session.query(Publisher).filter(or_(Publisher.name == publisher_input, Publisher.id == publisher_input)).first()
    if publisher is None:
        return None
    publisher_shops = session.query(PublisherShop).filter(PublisherShop.publisher_id == publisher.id).all()
    shops = [session.query(Shop).filter(Shop.id == ps.shop_id).first() for ps in publisher_shops]
    return shops




def print_sales(shops):
    for shop in shops:
        sales = session.query(Sale).filter(Sale.shop_id == shop.id).all()
        for sale in sales:
            print(f"{sale.book.title} | {shop.name} | {sale.price} | {sale.date}")

Base.metadata.create_all(engine)
if __name__ == '__main__':
    publisher_name = input("Enter publisher name: ")
    shops = get_shops(publisher_name)
    if shops is None:
        print(f"No shops found for publisher {publisher_name}")
    else:
        print_sales(shops)
