class Contact:
    def __init__(self, name, phn_no):
        self.name = name
        self.phn_no = phn_no

    def display_contact(self):
        return f'Name: {self.name}\nPhone_No: {self.phn_no}'

class Person(Contact):
    def __init__(self, name, phn_no, age):
        super().__init__(name, phn_no)
        self.age = age

    def display_contact(self):
        return f'Name: {self.name}, Phone_No: {self.phn_no}, Age: {self.age}'

class Business(Contact):
    def __init__(self, name, phn_no, company):
        super().__init__(name, phn_no)
        self.company = company

    def display_contact(self):
        return f'Name: {self.name}, Phone_No: {self.phn_no}, Company: {self.company}'

class PhoneBook:
    def __init__(self):
        self.phonebook = []

    def add_contact(self, contact):
        self.phonebook.append(contact)
        print(f'Added {contact.name} to the phone book.')

    def search_contact(self, name):
        for det in self.phonebook:
            if det.name == name:
                print(det.display_contact())
                break
            print('Contact not Found.')

    def display_contact(self):
        for cont in self.phonebook:
            print(cont.display_contact())
            print()


print('Welcome to PhoneBook Application!')
phn_book = PhoneBook()
while True:
    print('\nMenu')
    print('1.Add Contact')
    print('2.Search Contact')
    print('3.Display Contact')
    print('4.Exit')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        print('Choose the type of contact:')
        print('1.Person')
        print('2.Business')
        opt = int(input('Enter your choice: '))
        if opt == 1:
            name = input('Enter the name: ')
            phn = int(input('Enter the phone no: '))
            age = int(input('Enter the age: '))
            person = Person(name,phn,age)
            phn_book.add_contact(person)
        elif opt == 2:
            name = input('Enter the name: ')
            phn = int(input('Enter the phone no: '))
            company = input('Enter the company name: ')
            business = Business(name,phn,company)
            phn_book.add_contact(business)
        else:
            print('Invalid choice')
    elif choice == 2:
        name = input('Enter the name to search: ')
        phn_book.search_contact(name)
    elif choice == 3:
        phn_book.display_contact()
    elif choice == 4:
        print('Done')
        break
    else:
        print('Invalid Choice')
