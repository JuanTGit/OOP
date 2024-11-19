
const itemList = document.getElementById('drop-details')
const droppedItemDetails = document.getElementById('dropped-item-details')
const killCounter = document.getElementById('kill-count')
const totalValue = document.getElementById('total-value')
const updateItemName = document.getElementById('item-name')
const updateItemImg = document.getElementById('dropped-item-img')
const updateBossImg = document.getElementById('boss-img')
const determineShadow = document.getElementById('shadow')
const alertContainer = document.getElementById('alert-container')

let currentItem = null

function updateUI(data) {
	console.log(data)
	itemList.innerHTML = '';
	const inventoryItems = data.Inventory[1];
	
	// setTimeout(() => {
		const currentDrop = data.Inventory[2];
		const totalKills = data.Inventory[3];
		const itemImage = currentDrop['image']
		const totalProfit = data.Inventory[0]
		const itemRarity = currentDrop['rarity'][1]
		currentItem = currentDrop['name']

	// Kill Details
		updateItemName.innerHTML = `You received ${currentDrop['quantity'].toLocaleString()} x ${currentDrop['name']}!`
		updateItemImg.src = `${itemImage}`
		updateItemImg.classList.remove('bounce');
		updateItemImg.offsetHeight;
		updateItemImg.classList.add('bounce');
		updateBossImg.src = `${data.Inventory[4]}`
		determineShadow.classList.add('shadow')
	
		const droppedItemValue = document.createElement('h5')
		const droppedItemRarity = document.createElement('h5')
		droppedItemValue.innerText = `Value: ${Number(currentDrop['value']).toLocaleString()}`;
		droppedItemRarity.innerText = `Drop Rate: ${itemRarity}`		
		
		droppedItemDetails.innerHTML = ''
		droppedItemDetails.append(droppedItemValue, droppedItemRarity)
		killCounter.textContent = `Total Kills: ${totalKills || 0}`
		totalValue.innerHTML = `Total Value: ${totalProfit.toLocaleString() || 0} gp`
	// },1000)

		// console.log(inventoryItems)

		
		for (const key in inventoryItems) {
			const newItem = document.createElement('li');
			const itemWrapper = document.createElement('div');
			const img = document.createElement('img');
			const quantityLabel = document.createElement('p')
			const head = document.createElement('p');
			const foot = document.createElement('p');
			newItem.name = `${key}`
			newItem.setAttribute('name', `${key}`); 
			foot.setAttribute('name', `${key}`)
			img.id = 'inventory-item'
			
			
			
			quantityLabel.textContent = `${inventoryItems[key]['quantity'].toLocaleString() || 0}`
			quantityLabel.classList.add('quantity-label')
			
			head.innerHTML = `${key}`
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
	
// Update droptable -- ROLL DROP

async function getData() {
	try{
		let res = await fetch("http://127.0.0.1:5000/get-drop")
		let data = await res.json()
		return data
	} catch (error) {
		console.error('Failed to fetch data:', error);
		return { Inventory: [] };
	}
}

const getDropButton = document.getElementById('get-drop')

getDropButton.addEventListener('click', async (e) => {
	e.preventDefault();
	let data = await getData();
	updateUI(data)
});


// Drop item - DROP ITEM

async function recentlyDeleted() {
	try{
		let res = await fetch("http://127.0.0.1:5000/get-drop/drop-current")
		let data = await res.json()
		return data
	} catch (error) {
		console.error('Failed to fetch data:', error);
		return { Inventory: [] };
	}
	
}

const removeItem = document.getElementById('remove-item')

removeItem.addEventListener('click', async (e) => {
	e.preventDefault();
	let data = await recentlyDeleted();
	updateOrRemoveItem(currentItem, data.Inventory, data.total)
})


function updateOrRemoveItem(itemName, inventory, total) {
	console.log(itemName, total)
    const itemElement = document.querySelector(`li[name="${itemName}"]`);
    if (inventory[itemName] && total) {
        // Update item
        const quantityLabel = itemElement.querySelector('.quantity-label');
        const foot = itemElement.querySelector('p:last-child');
        const newQuantity = inventory[itemName].quantity;
        const newValue = inventory[itemName].value;

        // Update quantity label
        quantityLabel.textContent = `${newQuantity.toLocaleString()}`;

        // Update total value
        foot.textContent = `${newValue.toLocaleString()} gp`;
		totalValue.innerHTML = `Total Value: ${total} gp`
		
    } else if (itemElement) {
		// Remove item if no longer in inventory
        itemElement.remove();
		totalValue.innerHTML = `Total Value: ${total} gp`
    } else {
		const alert = document.createElement('div')
		alert.className = 'alert alert-warning alert-dismissible fade show';
		alert.role = 'alert';
		alert.innerHTML = `${itemName} is no longer in your inventory.
		<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>`;

		alertContainer.appendChild(alert);

		setTimeout(() => {
			alert.remove()
		}, 3000);
	}

}


// Clear inventory - CLEAR INVENTORY

async function clearInventory() {
	let data = await fetch('http://127.0.0.1:5000/clear-inventory')
	let res = data.json()
	return res
}

const clearInventoryButton = document.getElementById("clear-inventory")


clearInventoryButton.addEventListener('click', async (e) => {
	e.preventDefault();
	let data = await clearInventory()
	currentItem = null;
	if (itemList.innerHTML === ''){
		console.error('Inventory already empty')
		const alert = document.createElement('div')
		alert.className = 'alert alert-warning alert-dismissible fade show';
		alert.role = 'alert';
		alert.innerHTML = `Your inventory is empty.
		<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>`;

		alertContainer.appendChild(alert);

		setTimeout(() => {
			alert.remove()
		}, 3000);
	} else {
		itemList.innerHTML = '';
		totalValue.innerHTML = `Total Value: ${0} gp`
		killCounter.innerHTML = 'Total Kills: 0'
	}
})