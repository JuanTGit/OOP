import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
boss_wiki = requests.get("https://oldschool.runescape.wiki/w/General_Graardor", headers=headers)
soup = BeautifulSoup(boss_wiki.text, "html.parser")
boss_tables = soup.find_all('table', attrs={'class': 'item-drops'})
boss_table = soup.find('table', attrs={'class': 'infobox-monster'})
boss_image = boss_table.find('img')['src']

item_details = {}
item_details['boss_image'] = f'https://oldschool.runescape.wiki{boss_image}'



for table in boss_tables:
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
		# Image SRC
		item_img_cell = row.find('td', attrs={'class': 'inventory-image'})

		image_url = None
		# print(img_src)

		if item_img_cell:
			img_tag = item_img_cell.find('img', attrs={'src': True})
			if img_tag:
				image_url = img_tag['src']

		img_src = f'https://oldschool.runescape.wiki{image_url}'

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
				'value': item_value,
				'image': img_src
			})