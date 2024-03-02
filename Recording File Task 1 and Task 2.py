from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Date
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id_publ = Column('id_publ', Integer, primary_key=True)
    name = Column('name', String(length=40))


class Book(Base):
    __tablename__ = 'book'
    id_book = Column('id_book', Integer, primary_key=True)
    title = Column('title', String(length=40))
    id_publ = Column('id_publ', Integer, ForeignKey('publisher.id_publ'))


class Shop(Base):
    __tablename__ = 'shop'
    id_shop = Column('id_shop', Integer, primary_key=True)
    name = Column('name', String(length=40))


class Stock(Base):
    __tablename__ = 'stock'
    id_stock = Column('id_stock', Integer, primary_key=True)
    id_book = Column('id_book', Integer, ForeignKey('book.id_book'))
    id_shop = Column('id_shop', Integer, ForeignKey('shop.id_shop'))
    count = Column('count', Integer)


class Sale(Base):
    __tablename__ = 'sale'
    id_price = Column('id_price', Integer, primary_key=True)
    price = Column('price', Integer)
    date_sale = Column('date_sale', Date)
    id_stock = Column('id_stock', Integer, ForeignKey('stock.id_stock'))
    count = Column('count', Integer)


engine = create_engine('postgresql://postgres:1109@localhost:5432/dbalchemy')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


def get_shops(input_data):
    query = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Shop). \
        join(Stock).join(Book).join(Publisher).join(Sale)

    if input_data.isdigit():
        result = query.filter(Publisher.id_publ == input_data).all()
    else:
        result = query.filter(Publisher.name == input_data).all()

    for title, shop_name, price, date_sale in result:
        print(f"{title: <40} | {shop_name: <10} | {price: <8} | {date_sale.strftime('%d-%m-%Y')}")


if __name__ == '__main__':
    user_input = input("Enter publisher name or ID: ")
    get_shops(user_input)

session.close()
