
const getDropButton = document.getElementById('get-drop')
const itemList = document.getElementById('drop-details')
const droppedItem = document.getElementById('dropped-item')
const killCounter = document.getElementById('kill-count')
const totalValue = document.getElementById('total-value')
const removeItem = document.getElementById('remove-item')
const updateItemName = document.getElementById('item-name')
const updateItemImg = document.getElementById('dropped-item-img')
const updateBossImg = document.getElementById('boss-img')

let currentItem = null

async function getData() {
	try{
		let req = await fetch("http://127.0.0.1:5000/get-drop")
		let data = await req.json()
		return data
	} catch (error) {
		console.error('Failed to fetch data:', error);
		return { Inventory: [] };
	}
}

async function recentlyDeleted() {
	try{
		let req = await fetch("http://127.0.0.1:5000/get-drop/drop-current")
		let data = await req.json()
		return data
	} catch (error) {
		console.error('Failed to fetch data:', error);
		return { Inventory: [] };
	}
	
}

function updateUI(data) {
	const inventoryItems = data.Inventory[1];
	const currentDrop = data.Inventory[2];
	const totalKills = data.Inventory[3];
	const itemImage = currentDrop['image']
	const totalProfit = data.Inventory[0]
	currentItem = `${currentDrop['name']}`

	itemList.innerHTML = '';
	updateItemName.innerHTML = `You received ${currentDrop['quantity'].toLocaleString()} x ${currentDrop['name']}!`
	updateItemImg.src = `${itemImage}`
	updateItemImg.classList.remove('bounce');
	updateItemImg.offsetHeight;
	updateItemImg.classList.add('bounce');
	updateBossImg.src = `${data.Inventory[4]}`

	
	document.getElementById('dropped-item-details').innerHTML = `Value: ${Number(currentDrop['value']).toLocaleString() || 0} gp`
	killCounter.textContent = `Total Kills: ${totalKills || 0}`
	totalValue.textContent = `Total Value: ${totalProfit.toLocaleString() || 0} gp`

	for (const key in inventoryItems) {
		const newItem = document.createElement('li');
		const itemWrapper = document.createElement('div');
		const img = document.createElement('img');
		const quantityLabel = document.createElement('span')
		const head = document.createElement('p');
		const foot = document.createElement('p');
		newItem.name = `${key}`
		img.id = 'inventory-item'
		foot.id = 'footer-gp-value'

		quantityLabel.textContent = `${inventoryItems[key]['quantity'].toLocaleString() || 0}`
		quantityLabel.classList.add('quantity-label')

		head.innerHTML = `${key}`
		head.classList.add('mt-3')
		foot.textContent = `${inventoryItems[key]['value'].toLocaleString() || 0} gp`;

		img.src = inventoryItems[key]['image']
		
		itemWrapper.appendChild(quantityLabel);
		itemWrapper.appendChild(img);
		itemWrapper.appendChild(head)
		itemWrapper.appendChild(foot)
		
		newItem.appendChild(itemWrapper);
		itemList.appendChild(newItem);
	}

}

getDropButton.addEventListener('click', async (e) => {
	e.preventDefault();
	let data = await getData();
	updateUI(data)
});



removeItem.addEventListener('click', async (e) => {
	e.preventDefault();
	let data = await recentlyDeleted();
	itemDetails = data.itemDetails

	const itemListItems = Array.from(itemList.children)
	console.log(itemListItems)

})