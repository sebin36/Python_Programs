class Contact:
    def __init__(self, name, phone, email, det):
        self.name = name
        self.phone = phone
        self.email = email
        self.details = det

    def add_contact(self, nam, phn, eml):
        self.details.append([nam, phn, eml])
        print('Details Saved Successfully.')

    def update_contact(self, nam, new_phn, new_eml):
        self.details[nam] = [new_phn, new_eml]
        print(f'Details of {nam} has been updated.')
        
    def delete_contact(self, nam):
        if nam in self.details:
            del self.details[nam]
            print(f'Details of {nam} has been deleted.')
        else:
            print('No data available.')

    def list_contacts(self):
        for key in self.details:
            ph, eml = self.details[key]
            print(f'Name: {key}, PhoneNo:{ph}, EmailId:{eml}')
                
    def __str__(self):
        return f'Name: {self.nam}\nPhoneNo: {self.phn}\nEmailID: {self.eml}'


details = []
while True:
    print('\nContact Application Menu:')
    print('1.Add Contact')
    print('2.Update Contact')
    print('3.Delete Contact')
    print('4.List Contacts')
    print('5.Quit')
    choice = input('Enter your choice: ')
    if int(choice) == 1:
        name = input('Enter Name: ')
        phone = input('Enter Phone Number: ')
        email = input('Enter Email Address: ')
        info = Contact(name,phone,email,details)
        info.add_contact(name,phone,email)
    elif int(choice) == 2:
        name = input('Enter Name: ')
        phone = int(input('Enter New Phone Number: '))
        email = input('Enter New Email Address: ')
        info = Contact(name,phone,email,details)
        info.update_contact(name,phone,email)
    elif int(choice) == 3:
        name = input('Enter Name: ')
        info = Contact(name,phone,email,details)
        info.delete_contact(name)
    elif int(choice) == 4:
        print('Contacts:')
        info = Contact(name,phone,email,details)
        info.list_contacts()
    elif int(choice) == 5:
        print('Done')
        break
    else:
        print('Invalid Choice')    
