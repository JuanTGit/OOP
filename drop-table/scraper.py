import requests
from bs4 import BeautifulSoup


bandos_wiki = requests.get("https://oldschool.runescape.wiki/w/General_Graardor")
soup = BeautifulSoup(bandos_wiki.text, "html.parser")
bandos_tables = soup.find_all('table', attrs={'class': 'item-drops'})


item_details = {}
for table in bandos_tables:
	table_name = table.find_previous('span', attrs={'class': 'mw-headline'}).text

	rows = table.find_all('tr')

	for row in rows[1:]:
		# Item Name Row
		item_name_cell = row.find('td', attrs={'class': 'item-col'})
		# Item Quantity Row
		item_quantity_cell = row.find('td', attrs={'data-sort-value': True})
		# Rarity Row
		item_rarity_cell = row.find('span', attrs={'data-drop-fraction': True})
		# Item Value Row
		item_value_cell = row.find('td', attrs={'class': 'ge-column'})

		if item_name_cell and item_quantity_cell and item_rarity_cell and item_value_cell:
			item_name = item_name_cell.text.strip()
			item_quantity = item_quantity_cell['data-sort-value']
			item_rarity = item_rarity_cell['data-drop-fraction'].replace(',', '')
			item_value = item_value_cell['data-sort-value']

			def convert_drops(str):
				if '/' in str:
					numerator, denominator = map(float, str.split('/'))
					return (numerator / denominator)

			if table_name not in item_details:
				item_details[table_name] = []


			item_details[table_name].append({
				'name': item_name,
				'quantity': item_quantity,
				'rarity': convert_drops(item_rarity),
				'value': item_value
			})

# for table, values in item_details.items():
# 	print(f'============{table}============')
# 	for item in values:
# 		print(item['name'])


# print(count, names)