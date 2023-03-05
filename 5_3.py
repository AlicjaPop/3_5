class BaseContact:
    def __init__(self, first_name, last_name, phone_private, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_private = phone_private
        self.email_address = email_address

        self._label_length=len(self.first_name)+len(self.last_name)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone_private}, {self.email_address}"
    
    def contact(self):
        return f"Wybieram numer {self.phone_private} i dzwonię do {self.first_name} {self.last_name}"
    
    @property
    def label_length(self):
        return self._label_length
    

class BusinessContact(BaseContact):
    def __init__(self, company, position, phone_company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.phone_company = phone_company

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone_private}, {self.email_address}, {self.company}, {self.position}, {self.phone_company}"
    
    def contact(self):
        return f"Wybieram numer {self.phone_company} i dzwonię do {self.first_name} {self.last_name}"
    
    @property
    def label_length(self):
        return self._label_length
    
contacts_list=[]

def create_contacts(contact_type, number_of_contacts):
    from faker import Faker
    fake=Faker()
    for i in range (number_of_contacts):
        if contact_type=="Business":
            company=fake.company()
            position=fake.job()
            phone_company=fake.phone_number()
            first_name=fake.first_name()
            last_name=fake.last_name()
            phone_private=fake.phone_number()
            email_address=fake.email()
            Business_contact=BusinessContact(company, position, phone_company, first_name, last_name, phone_private, email_address)
            contacts_list.append(Business_contact)
        elif contact_type=="Base":
            first_name=fake.first_name()
            last_name=fake.last_name()
            phone_private=fake.phone_number()
            email_address=fake.email()
            Base_contact=BaseContact(first_name, last_name, phone_private, email_address)
            contacts_list.append(Base_contact)
    return contacts_list