
contacts = []

def add_contacts():
    name=input("enter your name: ")
    phone=input("enter your phone number: ")
    contacts.append(name)
    contacts.append(phone)

def view():
    i = 0
    while i < len(contacts):
        print("------")
        print("Name:", contacts[i])
        print("Phone:", contacts[i + 1])
        print("------")
        i += 2

def search():
    search_name = input("Enter name to search: ")

    found = False
    i = 0
    while i < len(contacts):
        if contacts[i].lower() == search_name.lower():
            print("Name:", contacts[i])
            print("Phone:", contacts[i + 1])
            found = True
            break
        i += 2

    if not found:
        print("Contact not found")


def main():
    while True:
        print("1 , add contact")
        print("2 , view")
        print("3 , search")
        print("4 , exit")

        choose = int(input("enter your numbers "))

        if choose == 1:
            add_contacts()
        elif choose == 2:
            view()
        elif choose == 3:
            search()
        elif choose == 4:
            break
    print("good bye! ")


main()
