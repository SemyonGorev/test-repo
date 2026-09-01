from mailing import Mailing
from address import Address
to_address = Address ("123456","Кострома","ул.Димитрова","д.9","кв.11")
from_address = Address ("123456","Кострома","ул.Димитрова","д.9","кв.10")
track = 142122
cost = 200

mailing = Mailing (to_address, from_address, cost, track)

print (mailing)

