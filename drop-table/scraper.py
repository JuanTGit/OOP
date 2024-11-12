import requests
from bs4 import BeautifulSoup


bandos_wiki = requests.get("https://oldschool.runescape.wiki/w/General_Graardor")
soup = BeautifulSoup(bandos_wiki.text, "html.parser")
bandos_tables = soup.find_all('table', attrs={'class': 'item-drops'})


item_details = {}
for table in bandos_tables:

	rows = table.find_all('tr')

	print(f'==================================TABLE==================================')
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
			item_rarity = item_rarity_cell['data-drop-fraction']
			item_value = item_value_cell.text.replace(',', '')
			item_value.replace('–', '-')
			# if item_value.split('-'):
			# 	min_value, max_value = item_value.split('-')
			# 	print(min_value, max_value)
			range_list = []


			if '-' in item_value:
				print(item_value)