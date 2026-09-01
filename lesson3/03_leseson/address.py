class Address:
     
     def __init__(self,index,city,street,house,flat):
          self.index = index 
          self.city = city
          self.street = street
          self.house = house
          self.flat = flat
     def __str__(self):
         return f"{self.index} {self.city} {self.street} {self.house} {self.flat} "
