class AddressBook:
    def __init__(self, first_name, last_name, company, position, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email_address = email_address
    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.company}, {self.email_address}"
    def contact(self):
        return f"Kontaktuję się z {self.first_name} {self.last_name}, {self.position}, {self.email_address}"
    


BC1=AddressBook(first_name="Dean", last_name="Gonzalez", company="Martin-Martin", position="Engineer", email_address="Dean.Gonzalez@M-M.com")
BC2=AddressBook(first_name="James", last_name="Smith", company="Smith Inc.", position="Regulatory Affairs Officer", email_address="J.Smith@smith.com")
BC3=AddressBook(first_name="Zachary", last_name="Salinas", company="Cook, Bauer and Strickland", position="Scientist, research (medical)", email_address="Zachary.Salinas@CBS.com")
BC4=AddressBook(first_name="Andrew", last_name="Nguyen", company="Dorsey, Nunez and Alvarez", position="Make", email_address="A.Nguyen@DN&A.com")
BC5=AddressBook(first_name="Elizabeth", last_name="Jones", company="Campbell, Holland and Smith", position="Designer, multimedia", email_address="E.Jones@C-H-S.com")

BCs=[BC1, BC2, BC3, BC4, BC5]
