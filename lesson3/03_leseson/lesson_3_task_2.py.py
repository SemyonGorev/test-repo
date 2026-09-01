from smartphone import Smartphone

catalog = [
Smartphone ('Samsung', 'Galaxy', +79203887823),
Smartphone ('Nokia', '3310', +79203887824),
Smartphone ('Iphone', '16', +79203887814),
Smartphone ('Honor', 'Magic 8 Pro ', +79203884314),
Smartphone ('xiaomi', '16 Pro ', +79203824314)
]


for smartphone in catalog:
	print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")