class Contact:
    def __init__(self):
        self.details = {}

    def add_contact(self, name, ph_no, eml):
        self.details[name] = [ph_no, eml]
        print('Contact Added.')

    def update_contact(self, name, new_ph, new_eml):
            self.details[name] = [new_ph, new_eml]
            print('Details Updated')

    def del_contact(self, name):
        if name in self.details.keys():
            del self.details[name]
            print('Contact Deleted')

    def list_contact(self):
        print('Contacts:')
        for info in self.details:
            print(f'Name: {info},', end='')
            ph, eml = self.details[info]
            print(f' PhoneNo: {ph}, Email: {eml}')


contact = Contact()
while True:
    print('\nMenu')
    print('1.Add Contact')
    print('2.Update Contact')
    print('3.Delete Contact')
    print('4.List Contact')
    print('5.Quit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        name = input('Enter Name: ')
        phn = int(input('Enter PhnNo: '))
        eml = input('Enter Email: ')
        contact.add_contact(name,phn,eml)
    elif choice == 2:
        name = input('Enter Name: ')
        if name not in contact.details:
            print('No Contact Found')
        else:
            phn = int(input('Enter New PhnNo: '))
            eml = input('Enter New Email: ')
        contact.update_contact(name,phn,eml)
    elif choice == 3:
        name = input('Enter the contact name to delete: ')
        contact.del_contact(name)
    elif choice == 4:
        contact.list_contact()
    elif choice == 5:
        print('Done')
        break
    else:
        print('Invalid Choice')
