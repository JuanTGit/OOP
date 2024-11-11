import requests
from bs4 import BeautifulSoup


cox_wiki = requests.get("https://oldschool.runescape.wiki/w/Ancient_chest")
soup = BeautifulSoup(cox_wiki.text, "html.parser")
cox_tables = soup.find_all('table', attrs={'class':'item-drops'})

item_data = {}

for table in cox_tables:

	rows = table.find_all('tr')

	print('==============================TABLE==============================')
	
	for row in rows:

		item_name_cell = row.find('td', attrs={'class': 'item-col'})
		# print(item_name_cell)

		quantity_cell = row.find('td', attrs={'data-sort-value': True})
		# print(quantity_cell)

		rarity_cell = row.find('span', attrs={'data-drop-percent': True})
		# print(rarity_cell)

		value_cell = row.find('td', attrs={'class': 'ge-column'})
		# print(value_cell)

		if item_name_cell and quantity_cell and rarity_cell and value_cell:
			item_name = item_name_cell.text.strip()
			quanity = quantity_cell['data-sort-value']
			rarity = rarity_cell.text.strip()
			value = value_cell.text.strip()

			print(f'name: {item_name} - quantity: {quanity} - rarity: {rarity} - value: {value}')
			item_data[item_name] = {
				'quantity': quanity,
				'rarity': rarity,
				'value': value
			}


print(item_data)