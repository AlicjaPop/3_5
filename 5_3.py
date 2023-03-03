
class BaseContact:
    def __init__(self, first_name, last_name, phone_private, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_private = phone_private
        self.email_address = email_address
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.phone_private}, {self.email_address}"
    def contact(self):
        return f"Wybieram numer {self.phone_private} i dzwonię do {self.first_name} {self.last_name}"
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)

class BusinessContact(BaseContact):
    def __init__(self, company, position, phone_company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.phone_company = phone_company
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.position}, {self.company}, {self.phone_company}, {self.email_address}"
    def contact(self):
        return f"Wybieram numer {self.phone_company} i dzwonię do {self.first_name} {self.last_name}"
    @property
    def label_length(self):
        return len(self.first_name) + len(self.last_name)


BC1=BusinessContact(first_name="Dean", last_name="Gonzalez", phone_private="+48123123123",email_address="Dean.Gonzalez@M-M.com", company="Martin-Martin", position="Engineer", phone_company="+48987987987")
BC2=BusinessContact(first_name="James", last_name="Smith", phone_private="+48234234234", email_address="J.Smith@smith.com", company="Smith Inc.", position="Regulatory Affairs Officer", phone_company="+48876876876")
BC3=BusinessContact(first_name="Zachary", last_name="Salinas", phone_private="+48345345345", email_address="Zachary.Salinas@CBS.com", company="Cook, Bauer and Strickland", position="Scientist, research (medical)", phone_company="+48765765765")
BC4=BusinessContact(first_name="Andrew", last_name="Nguyen", phone_private="+48456456456", email_address="A.Nguyen@DN&A.com", company="Dorsey, Nunez and Alvarez", position="Make", phone_company="+48654654654")
BC5=BusinessContact(first_name="Elizabeth", last_name="Jones", phone_private="+48567567567", email_address="E.Jones@C-H-S.com", company="Campbell, Holland and Smith", position="Designer, multimedia", phone_company="+48543543543")

BCs=[BC1, BC2, BC3, BC4, BC5]
print(BC1.label_length())

