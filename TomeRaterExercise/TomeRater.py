        
            
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email
        

    def change_email(self, address):
        self.email = address
        print("User {} has a new email address.".format(self.name))
        
    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        rating_count = 0
        for rating in self.books.values():
            if rating:
             total += rating
             rating_count += 1
        average = total / rating_count
        return average
                
    def __repr__(self):
        return "User {name}, email: {email}, books read: {books}".format(name = self.name, email = self.email, books = len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
          

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("{} has a new isbn".format(self.title))

    def add_rating(self, rating):
        if rating and rating >= 1 and rating <= 4:
            self.ratings.append(rating)

    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            total += rating
        avg = total / len(self.ratings)
        return avg
    
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title
            

class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

    
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
         Book.__init__(self, title, isbn)
         self.subject = subject
         self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)
                
    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction

    def create_non_fiction(self, title, subject, level, isbn):
        new_nonfiction = Non_Fiction(title, subject, level, isbn)
        return new_nonfiction

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with this email.")

    def print_catalog(self):
        for item in self.books:
            print(item)

    def print_users(self):
        for item in self.users:
            print(item)

    def get_most_read_book(self):
        max_reads = float("-inf")
        most_read = None

        for book in self.books:
            num_reads = self.books[book]
            if num_reads > max_reads:
                max_reads = num_reads
                most_read = book

        return most_read

    def highest_rated_book(self):
        highest_rating = float("-inf")
        highest_book = None

        for book in self.books:
            avg = book.get_average_rating()
            if avg > highest_rating:
                highest_rating = avg
                highest_book = book

        return highest_book

    def most_positive_user(self):
        highest_rating = float("-inf")
        positive_user = None

        for user in self.users.values():
            avg = user.get_average_rating()
            if avg > highest_rating:
                highest_rating = avg
                positive_user = user

        return positive_user

    


Tome_Rater = TomeRater()



#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.get_most_read_book())
        
        
            
                
        
        
              
