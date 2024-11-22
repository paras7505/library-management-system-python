# the code will run here 

from crud import add_book,add_member,get_book,get_members


def enter_book():
    title = input("Enter the title of the book:")
    author = input("Enter the Author of the book:")
    isbn = input("Enter book ISBN:")
         # we can do exception handling here if not an interger then what will happen 
    try:
        count = count = int(input("Enter the count of the book: "))
    except:
        count = int(input("enter the value in interger: "))

        add_book(title,author,isbn,count) # this will add the data into the database we are making the function in another 
        #file Crud.py (and all the function will be written there only form there we will import the function)


def view_books():
    books = get_book()  # it will give us an array so we will print all
    for book in books:
        available = "available" if book.count > 0 else "not available"
        print(f"{book.id} : {book.title} by {book.author} available {book.count} copies")


def add_member():
    name = input("Enter your name :")
    email = input("Enter your Email :")
    add_member(name,email)

def view_member():
    members = get_members()
    for member in members:
        print(f"{member.id} {member.name} {member.email}")



def main():
    print("**************************************")
    print("1. Add book ")
    print("2. View book")
    print("3. Add members")
    print("4. View members")

    print("**************************************")

    choice = input("Enter your choice:")

    if choice == '1':
        enter_book()

    elif choice =="2":
        view_books()

    elif choice == '3':
        add_member()

    elif choice == '4':
        view_member()

        



if __name__ == "__main__":  # this is usually used for the big project to point out that our project/code is starting from here 
    main()


