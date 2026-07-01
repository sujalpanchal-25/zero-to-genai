import json,random,string,os
from datetime import datetime
from pathlib import Path


class Library:
    database = "library.json"
    data = {"books":[],"members":[]}
    
    if Path(database).exists():
        with open(database,"r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
    else:
        with open(database,"w") as f:
            json.dump(data,f,indent=4)
             
    def get_id(prefix = 'B'):
        random_id = ""
        for i in range(6):
            random_id += random.choice(string.ascii_uppercase + string.digits)
        return prefix + '-' + random_id
    
    @classmethod    
    def save_data(cls):
        with open(cls.database,'w') as f:
            json.dump(cls.data,f,indent=4,default=str)
        
    def add_book(self):
        title = input("Enter The Book Title : ").strip().lower() 
        author = input("Enter The Book Author : ").strip().lower() 
        try:
            copies = int(input("Enter The Book Copies : "))
        except ValueError:
            print("Please Enter Valid Input")
            return
        b = {
            "id" : Library.get_id(),
            "title":title,
            "author":author,
            "total_copies":copies,
            "available_copies": copies,
            "added_on": datetime.now().strftime("%d/%m/%Y,%I:%M:%S %p") 
            }
        Library.data['books'].append(b)
        Library.save_data()
        print("The Book Added SuccessFully")
        
    def list_book(self):
        if not Library.data['books']:
            print("Sorry no Book Found")
            return
        print("-" * 120)
        print(f"{'ID':<12} | {'Title':<30} | {'Author':<20} | {'Total/Available':<15} | {'Added on':<25}")
        print("-" * 120)
        for b in Library.data['books']:
            print(
                f"{b['id']:<12} | "
                f"{b['title']:<30.30} | "
                f"{b['author']:<20.20} | "
                f"{b['total_copies']}/{b['available_copies']:<13} | ",
                f"{b['added_on']:<25}"
            )
        print("-" * 120)
                   
    def add_member(self):
        u_name = input("Enter the Member @Username :- ").strip().lower().replace(" ", "")
        p_no = input("Enter the Member Phone Number :- ")
        email = input("Enter the Member Email ID :- ").strip().lower()
        
        m = {
            "id":Library.get_id("M"),
            "username":u_name,
            "p_no":p_no,
            "email":email,
            "borrowed" : [],
            "added_on": datetime.now().strftime("%d/%m/%Y,%I:%M:%S %p"),      
        }
        Library.data['members'].append(m)
        Library.save_data()
        print("The Member Added SuccessFully")
        print()
        
        v = input(r"Can You Borrow Book(Y\N) :- ").lower()
        if v =='y':
            self.borrow()
        else:
            print(f"The Member ID is : {m['id']}\n Please remember...\nThis ID Use For Borrow & Return The Book..")
            return
    
    def list_member(self):
        if not Library.data['members']:
            print("Sorry, no members found.")
            return

        print("=" * 120)
        print(f"{'LIBRARY MEMBERS':^130}")
        print("=" * 120)

        for index, m in enumerate(Library.data['members'], start=1):

            print(f"\n{' MEMBER ' + str(index) + ' ':=^120}")

            print(f"🆔 Member ID : {m['id']}")
            print(f"👤 UserName      : {m['username']}")
            print(f"📞 Phone No. : {m['p_no']}")
            print(f"📧 Email     : {m['email']}")
            print(f"📅 Added On  : {m['added_on']}")

            print("-" * 120)
            print(f"{'Borrowed Books':^130}")
            print("-" * 120)

            if not m['borrowed']:
                print("No books borrowed.")
            else:
                print(f"{'Book ID':<20} | {'Book Title':<40} | {'Borrowed On'}")
                print("-" * 120)

                for i in m['borrowed']:
                    print(
                        f"{i['book_id']:<20} | "
                        f"{i['title']:<40} | "
                        f"{i['borrow_on']}"
                    )

            print("=" * 120)
      
    def borrow(self):
        mid = input("Enter The Member Id :- ").strip()
        
        mem = [m for m in Library.data['members'] if m['id'] == mid]
        if not mem:
            print("Sorry No such ID Exist..\n You are Not a Member\n")
            v = input(r"Can You Make Member(Y\N) :- ").lower()
            if v =='y':
                self.add_member()
                return
            else:
                print("Without Member you can't Borrow Book..\n Thank You To Visit....")
                return
        else:
            mem = mem[0]
        self.list_book()   
        books_id = input("Enter The Book Id : ")
        book = [b for b in Library.data['books'] if b["id"] == books_id]
        if not book:
            print("Sorry No such id of book Exist...")
            return
        book = book[0]
        
        if book['available_copies'] <= 0:
            print("Sorry all available Book copies are Currently in Use ")
            return
        
        be = {
            "book_id":book['id'],
            "title":book['title'],
            "borrow_on": datetime.now().strftime("%d/%m/%Y,%I:%M:%S %p")
        } 
        mem['borrowed'].append(be)
        book['available_copies'] -= 1
        print(f"✅{book['title']} Book Borrowed Successfully.")
        Library.save_data()
        
    def return_b(self):
        mid = input("Enter The Member Id :- ").strip()
        
        mem = [m for m in Library.data['members'] if m['id'] == mid]
        if not mem:
            print("Sorry No such ID Exist..")
            return
        else:
            mem = mem[0]
            
        if not mem['borrowed']:
            print("Member Not Borrowed any Book...")
            return
        print("*"*40)
        print("Borrowed Books : ")
        print("*"*40)
        for i ,b in enumerate(mem['borrowed'],start=1):
            print(f"{i} | {b['title']} | {b['book_id']}")
        print("*"*40)
        
        try:
            choi = int(input("Enter Number to Return :- "))
            select = mem['borrowed'].pop(choi-1)
        except Exception as err:
            print(f"Invalid Value {err}")
            return
            
        book = [bk for bk in Library.data['books'] if bk['id'] == select['book_id']]
        if book:
            book[0]['available_copies'] += 1
            print(f"✅{book[0]['title']} Book Return Successfully.")
        Library.save_data()
                 
    def delete_book(self):
        self.list_book()
        book_id = input("Enter Book ID to Delete :- ").strip()
    
        book = None
        for b in Library.data['books']:
            if b['id'] == book_id:
                book = b
                break
            
        if book is None:
            print("❌ No book found with this ID.")
            return
    
        print("\nBook Found")
        print("-" * 60)
        print(f"ID       : {book['id']}")
        print(f"Title    : {book['title']}")
        print(f"Author   : {book['author']}")
        print(f"Copies   : {book['available_copies']}/{book['total_copies']}")
        print("-" * 60)

        borrowed = book['total_copies'] - book['available_copies']

        if borrowed > 0:
            print(f"❌ {borrowed} copy/copies are still borrowed.")
            print("Return all copies before deleting.")
            return
        
        ch = input(r"Delete this book? (Y\N): ").strip().upper()
    
        if ch == "Y":
            Library.data['books'].remove(book)
            Library.save_data()
            print("✅ Book Deleted Successfully.")
        else:
            print("❌ Deletion Cancelled.")
            
    def delete_member(self):
        mem_id = input("Enter Member ID to Delete :- ").strip()
        
        member = None
        for m in Library.data['members']:
            if m['id'] == mem_id:
                member = m
                break
        
        if member is None:
            print("❌ No Member found with this ID.")
            return
        
        print("\nMember Found")
        print("-" * 60)
        print(f"ID        : {member['id']}")
        print(f"UserName      : {member['username']}")
        print(f"Phone No. : {member['p_no']}")
        print(f"Email     : {member['email']}")
        print("*"*60)
        print(f"Borrowed Book:-")
        print(f"{'Book_ID':<20} | {'Title':<18} | {'Borrow_On'} ")
        for i in member['borrowed']:
            print(f"{i['book_id']:<20} | {i['title']:<18} | {i['borrow_on']} ")
        print("*"*60)
        print("-" * 60)
            
        if member['borrowed']==[]:
            ch = input("Delete this Member? (Y/N): ").strip().upper()

            if ch == "Y":
                Library.data['members'].remove(member)
                Library.save_data()
                print("✅ Member Deleted Successfully.")
            else:
                print("❌ Deletion Cancelled.")
        else:
            print("please return The Book First\nWithout Return All Book You Can't Cancel Member")

    def find_book(self):
        book_t = input("Enter Book Title:- ").strip().lower()
    
        book = None
        for b in Library.data['books']:
            if b['title'] == book_t:
                book = b
                break
            
        if book is None:
            print("❌ No book found with this ID.")
            return
        
        print("\nBook Found")
        print("-" * 60)
        print(f"ID       : {book['id']}")
        print(f"Title    : {book['title']}")
        print(f"Author   : {book['author']}")
        print(f"Copies   : {book['available_copies']}/{book['total_copies']}")
        print("-" * 60)  
        
        v = input(r"Can You Borrow This Book(Y\N) :- ").lower()
        if v == 'y':
            self.borrow()
        else:
            print("Thank You for Visit...")
            return

    def find_member(self):
        mem_id = input("Enter Member Username :- ").strip().lower().replace(" ", "")
        
        member = None
        for m in Library.data['members']:
            if m['username'] == mem_id:
                member = m
                break
        
        if member is None:
            print("❌ No Member found with this ID.")
            return
        
        print("\nMember Found")
        print("-" * 60)
        print(f"ID        : {member['id']}")
        print(f"UserName      : {member['username']}")
        print(f"Phone No. : {member['p_no']}")
        print(f"Email     : {member['email']}")
        print("*"*60)
        print(f"Borrowed Book:-")
        print("*"*60)
        
        if member['borrowed'] == []:
            print("No Book Borrowed")
        else:
            print(f"{'Book_ID':<20} | {'Title':<18} | {'Borrow_On'} ")
            for i in member['borrowed']:
                print(f"{i['book_id']:<20} | {i['title']:<18} | {i['borrow_on']} ")
        print("*"*60)
        print("-" * 60)
        print()
        
        print("+"*60)
        print("1. Borrow Book")     
        print("2. Return Book")
        print("3. Delete Book")
        print("+"*60)
        print()
      
        try:
            v = int(input("What Task You Want to Do :- "))
        except ValueError:
            print("Invalid Input Please Try Again...")

        if v == 1:
            self.borrow()
        elif v == 2:
            self.return_b()
        elif v == 3:
            self.delete_member()
        else:
            print("Invalid Input...")
          
Book = Library()

while True:
    print()
    print("="*60)
    print("Library Management System")
    print("="*60)
    print("1. Add Book ")
    print("2. List Books ")
    print("3. Add Member ")
    print("4. List Member ")
    print("5. Find Book ")
    print("6. Find Member ")
    print("7. Borrow Book ")
    print("8. Return Book ")
    print("9. Delete Book ")
    print("10. Delete Member ")
    print("0. Exit ")
    print("="*60)
    print()

    try:
        cho = int(input("What Task You Want to Do :- "))
    except ValueError:
        print("Invalid Input Please Try Again...")

    print()
    if cho == 1:
        Book.add_book()
    if cho == 2:
        Book.list_book()
    if cho == 3:
        Book.add_member()
    if cho == 4:
        Book.list_member()
    if cho == 5:
        Book.find_book()
    if cho == 6:
        Book.find_member()
    if cho == 7:
        Book.borrow()
    if cho == 8:
        Book.return_b()
    if cho == 9:
        Book.delete_book()
    if cho == 10:
        Book.delete_member()
    if cho == 0:
        break
    print()
    os.system("pause")