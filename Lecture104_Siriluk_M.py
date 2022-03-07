class Customor:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to ",self.name,self.lastName,"'s cart","Age",self.age,"years old")

customer1 = Customor()
customer1.name = "Siriluk"
customer1.lastName = "Mentha"
customer1.age = 24
customer1.addCart()

customer2 = Customor()
customer2.name = "Loïc"
customer2.lastName = "Mentha"
customer2.age = 39
customer2.addCart()

customer3 = Customor()
customer3.name = "Wiphada"
customer3.lastName = "Boontarava"
customer3.age = 56
customer3.addCart()

customer4 = Customor()
customer4.name = "Tualek"
customer4.lastName = "Kaewmongkon"
customer4.age = 26
customer4.addCart()