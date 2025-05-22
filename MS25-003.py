import json
import os
class Book:

    #intilizes constructor method to store values
    def __init__(self, Title, Author, Genre, Rate):   
        self.Title = Title
        self.Author = Author
        self.Genre = Genre
        self.Rate = Rate

    #getter
    def get_book(self):     #only meant to return whats already inside object
        return self.Title, self.Author, self.Genre, self.Rate
    
    #setter:
    def set_book(self, Title, Author, Genre, Rate):
        self.Title = Title
        self.Author = Author
        self.Genre = Genre
        self.Rate = Rate

user_dict = {}
user_rate = {}

def Add():
    #passes user input to object within class

    #meand to load file if exists if it dosent then it creates dictionary 
    if os.path.exists("Book.json"):
            with open("Book.json", "r") as file:
                user_dict = json.load(file)
    else:
        user_dict = {}

    while True:
        title = input("Enter book Title: ")
        if title.lower() == 'done':
            break
        
        author = input("Enter book Author: ")
        genre = input("Enter book Genre: ")
        Rate = "blank" 
    
        book = Book(title, author, genre, rate)
        user_dict[title] = {
            "Title": book.Title,
            "Author": book.Author,
            "Genre": book.Genre,
            "Rate" : book.Rate
        }
    
    #enter contents into json file
    with open("Book.json", "w") as file:
        json.dump(user_dict, file, indent=4)

        #passes user input thats withn a dictionary to a constructor to be within getter for retreival



def View():
    #read through json file
    with open("Book.json", "r") as file:
        data = json.load(file)  # `data` is a dictionary of book info

    count = 1
    for title, book_data in data.items():  # book_data is a dict for each book
        book = Book(book_data["Title"], book_data["Author"], book_data["Genre"])
        info = book.get_book()
        print(f"{count}. Title: {info[0]}, Author: {info[1]}, Genre: {info[2]}")
        count += 1

#rating book requires a graph strucure in this instance dictionary
def Rate():
    username = input("Enter your username: ")
    # Load existing book data
    with open("Book.json", "r") as file:
        data = json.load(file)

    # create list of titles to add numbers to the books
    titles = list(data.keys())

    print("\nSelect a book to rate: ")

    #
    for idx, title in enumerate(titles, 1):
        print(f"{idx}. {title}")

    selection = int(input("\nEnter the number of the book you want to rate: "))

    #if 1 is less thatn or equal to the input of the list of titles then access key within dictionary to enter rating
    if 1 <= selection <= len(titles):
        selected_title = titles[selection - 1]
        rating = input(f"Enter your rating for {selected_title} (1–5): ")

        data[selected_title]["Rate"] = rating

        with open("Book.json", "w") as file:
            json.dump(data, file, indent=4)





def main():
    print("Enter 1 to add book: ")
    print("Enter 2 to view book: ")
    print("Enter 3 to rate book: ")


    choice = int(input("Enter a choice: "))
    if choice == 1:
        Add()

    elif choice == 2:
        View()
    
    elif choice == 3:
        Rate()
main()