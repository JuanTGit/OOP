
const getDropButton = document.getElementById('get-drop')
const itemList = document.getElementById('drop-details')
const droppedItem = document.getElementById('dropped-item')

getDropButton.addEventListener('click', async (e) => {
	e.preventDefault();

	itemList.innerHTML = '';
	droppedItem.innerHTML = ''

	let data = await getData();
	let inventoryItems = data.Inventory[1]
	let currentDrop = data.Inventory[2]

	for (const key in inventoryItems) {
		const newItem = document.createElement('li')
		newItem.textContent = `${key}: Amount: ${inventoryItems[key]['quantity']} - Value: ${inventoryItems[key]['value']} gp`;
		droppedItem.textContent = `${currentDrop['name']}`
		document.getElementById('dropped-item-details').textContent = `Drop Details: Amount: ${currentDrop['quantity']} Value: ${currentDrop['value']} gp`
		itemList.classList.add('list-group-item')
		itemList.appendChild(newItem)
	};
});

async function getData() {
	let req = await fetch("http://127.0.0.1:5000/get-drop")
	let data = await req.json()
	return data
}