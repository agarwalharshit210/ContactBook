contact_book = []

def add_Contact():
    name = input("Enter your Name : ")
    phone = input("Enter your Phone Number : ")
    email = input("Enter your email id : ")
    address = input("Enter your Address : ")
    contact_book.append({"name":name,"phone":phone,"email":email,"address":address})
    print("Contact Added Successfully")

def update_Contact():
    view_Contact()
    update_no = int(input("Enter the sequence number of contact which you want to update : "))
    if 1 <= update_no <= len(contact_book):
        name = input("Enter new Name : ")
        phone = int(input("Enter new Phone Number : "))
        email = input("Enter new email id : ")
        address = input("Enter new Address : ")

        contact_book[update_no-1]["name"] = name
        contact_book[update_no-1]["phone"] = phone
        contact_book[update_no-1]["email"] = email
        contact_book[update_no-1]["address"] = address

        print("Contact Updated Successfully")
    else:
        print("Invalid Contact Number")    

def delete_Contact():
    view_Contact()
    delete_no = int(input("Enter the sequence number of contact which you want to Delete : "))
    if 1 <= delete_no <= len(contact_book):
        contact_book.pop(delete_no-1)
        print("Contact Deleted Successfully")
    else:
        print("Invalid Contact Number")    

def search_Contact():
    view_Contact()
    choose = int(input("Search Through : \n1.Name\n2.Phone Number\n "))
    if choose == 1:
        search_name = input("Enter the Name you want to search : ")
        for i in contact_book:
            if i["name"] == search_name:
                print(f"Name : {i['name']} | Phone : {i['phone']} | Email : {i['email']} | Address : {i['address']}")  
    elif choose == 2:
        search_phone = input("Enter the Phone Number you want to Search : ")
        for i in contact_book:
            if i["phone"] == search_phone:
                print(f"Name : {i['name']} | Phone : {i['phone']} | Email : {i['email']} | Address : {i['address']}")   
    else:
        print("Invalid Contact Number or Name")  



def view_Contact():
    if not contact_book:
        print("Contact list is Empty")
    else:
        print("\n------------------------Contact List---------------------------\n ")
        for index,contact in enumerate(contact_book,start=1):  
            print(f"{index}. Name : {contact['name']} | Phone : {contact['phone']} | Email : {contact['email']} | Address : {contact['address']}")   
        print()  

def main():
    while True:
        print("1.Add the Contact\n2.Update the Contact\n3.Delete the Contact\n4.Search the Contact\n5.View the Contact\n6.Exit")
        choice = int(input("Enter the Choice : "))

        if choice == 1:
            add_Contact()
        elif choice == 2:
            update_Contact()
        elif choice == 3:
            delete_Contact()
        elif choice == 4:
            search_Contact()
        elif choice == 5:
            view_Contact()
        elif choice == 6:
            print("Thank you")
            break
        else:
            print("Invalid Choice, Please! enter the Valid Number")                     

if __name__ == '__main__':
    main()