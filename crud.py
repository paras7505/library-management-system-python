from models import Book,Member
from database import session

def add_book(title,author,isbn,count):
    print('adding book to database....!')
    # now we have to connect it to the database 
    # we have maded the classes in the models file now we have to make their object here
    book = Book(title = title , author = author, isbn = isbn, count = count)
    session.add(book) # here we create a session  
    session.commit() # and we commit it to the database

    print("book added successfully")


def get_book():
    return session.query(Book).all()   # this will give all the books in the database

def get_members():
    return session.query(Member).all()

def add_member(name, email):
    print("adding new member....")
    member = Member(name=name, email=email)
    session.add(member)
    session.commit()
    print("new member added successfully")


