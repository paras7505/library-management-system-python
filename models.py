from sqlalchemy import Column, Integer, String, ForeignKey, Date 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base() # it is database class

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String,nullable=False)
    count = Column(Integer, nullable=False,default=1)

 
class Member(Base):
    __tablename__ = "member"
    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    


class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id') , nullable= False)
    member_id = Column(Integer,ForeignKey('member.id'), nullable=False)
    issue_date = Column(Date, nullable=False)
    return_data = Column(Date, nullable=True)


    book = relationship("Book") # used to make foreign key relationship 
    member = relationship('Member') 