from pathlib import Path
import os

def create_folder():
    try:
        name = input("Please enter the folder name: ")
        p = Path(name)
        p.mkdir()
        print(f"✅ Folder '{name}' created successfully! 🎉\n")
    except Exception as err:
        print(f"⚠️ An error occurred: {err}\n")
   
def read_file_folder():
    print("\n📂 Current Directory Contents:")
    p = Path(".")
    items = list(p.rglob('*'))
    if not items:
        print("   (Directory is empty)")
    for i, v in enumerate(items):
        print(f"   {i+1} : {v}")
    print()
        
def update_folder():
    try:
        read_file_folder()
        o_name = input("Please enter the name of the folder you want to rename: ")
        p = Path(o_name)
        if p.exists() and p.is_dir():
            n_name = input("Please enter the new folder name: ")
            n_p = Path(n_name)
            p.rename(n_p)
            print(f"✅ Folder renamed to '{n_name}' successfully! 🎉\n")
        else:
            print("❌ Folder not found.\n")
    except Exception as err:
        print(f"⚠️ An error occurred: {err}\n")
 
def delete_folder():
    try:
        read_file_folder()
        name = input("Please enter the name of the folder you want to delete: ")  
        p = Path(name)
        if p.exists() and p.is_dir():
            va = input(f"⚠️ Are you sure you want to delete the folder '{name}'? (y/n): ").lower()
            if va == 'y':
                p.rmdir()
                print("🗑️ Folder deleted successfully! 🎉\n")  
            else:
                print("✨ Operation cancelled. Your folder is safe! 🎊\n")
        else:
            print("❌ Folder not found.\n")
    except Exception as err:
        print(f"⚠️ An error occurred: {err}\n")
  
def create_file():
    try:
        read_file_folder()
        name = input("Please enter the file name: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as f:
                d = input("Please enter the data you want to write to the file: ")
                f.write(d)
            print("✅ File created successfully! 🎉🎊\n")
        else:
            print("❌ Sorry, this file already exists!\n")
    except Exception as err:
        print(f"⚠️ An error occurred: {err}\n")

def read_file():
    try:
        read_file_folder()
        name = input("Please enter the file name you want to read: ") 
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as f:
                data = f.read()
            print(f"\n📖 Data inside '{name}':")
            print("---")
            print(data)
            print("---\n")
        else:
            print("❌ Sorry, this file does not exist!\n")
    except Exception as err:
        print(f"⚠️ An error occurred: {err}\n")

def update_file():
    print("\n" + "-"*30)
    print("Options:")
    print("1) Rename the file")  
    print("2) Append data to the file")  
    print("3) Overwrite data in the file") 
    print("-"*30)
    
    try:
        ch = int(input("Please enter your choice (1-3): ")) 
        read_file_folder()
        
        if ch == 1:
            o_n = input("Enter the current file name: ")
            p = Path(o_n)
            if p.exists() and p.is_file():
                n_n = input("Enter the new file name: ")
                pn = Path(n_n)
                if not pn.exists():
                    p.rename(pn)
                    print("✅ File renamed successfully! 🎉🎊\n")
                else:
                    print("❌ A file with that name already exists!\n")
            else:
                print("❌ File does not exist!\n")

        elif ch == 2:
            n = input("Enter the file name to append data: ")
            p = Path(n)
            if p.exists() and p.is_file():
                d = input("Enter the data you want to append: ")
                with open(p, 'a') as f:
                    f.write("\n" + d)
                print("✅ Data appended successfully! 📝\n")
            else:
                print("❌ File does not exist!\n")

        elif ch == 3:
            n = input("Enter the file name to overwrite: ")
            p = Path(n)
            if p.exists() and p.is_file():
                d = input("Enter the new data: ")
                with open(p, 'w') as f:
                    f.write(d)
                print("✅ Data overwritten successfully! 💾\n")
            else:    
                print("❌ File does not exist!\n")
        else:
            print("❌ Invalid choice!\n")
            
    except Exception as err:
        print(f"⚠️ An error occurred: {err}\n")
  
def delete_file():
    try:
        read_file_folder()
        n = input("Please enter the file name you want to delete: ")
        p = Path(n)
        if p.exists() and p.is_file():
            va = input(f"⚠️ Are you sure you want to delete the file '{n}'? (y/n): ").lower()
            if va == 'y':
                p.unlink()
                print("🗑️ File deleted successfully! 🎉\n")  
            else:
                print("✨ Operation cancelled. Your file is safe! 🎊\n")
        else:
            print("❌ File not found.\n")
    except Exception as err:    
        print(f"⚠️ An error occurred: {err}\n")
        
while True:   
    print()
    print("*" * 60)
    print("      FILE & FOLDER MANAGEMENT SYSTEM 📁")
    print("*" * 60)
    print("1) Create a Folder")
    print("2) View All Files & Folders")
    print("3) Rename a Folder")
    print("4) Delete a Folder") 
    print()
    print("5) Create a File") 
    print("6) Read a File") 
    print("7) Update a File") 
    print("8) Delete a File")
    print("0) Exit the Program") 
    print("*" * 60)
    print()
    
    try:
        cho = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Please enter a valid number!\n")
        continue
    
    if cho == 1: create_folder()
    elif cho == 2: read_file_folder()
    elif cho == 3: update_folder()
    elif cho == 4: delete_folder()
    elif cho == 5: create_file()
    elif cho == 6: read_file()
    elif cho == 7: update_file()
    elif cho == 8: delete_file()
    elif cho == 0:
        print("🙏 Thank you for using the system! Goodbye! 👋")
        print()
        break
    else:
        print("❌ Invalid option, please try again.\n")
        print()
    os.system("pause")