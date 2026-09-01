class User:

    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name
        self.fullname = first_name + " " + last_name
    def sayFirstName(self):
        print("меня зовут ", self.firstname)
    def sayLastName(self):
        print("меня зовут ", self.lastname)
    def sayFullName(self):
        print("меня зовут ", self.fullname)
		
Sam = User("Sam", "Lensherr")
Ava = User("Ava", "Daniels ")
Marta = User("Marta", "Clark")
Sam.sayFirstName()