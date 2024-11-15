
const getDropButton = document.getElementById('get-drop')
const itemList = document.getElementById('drop-details')
const droppedItem = document.getElementById('dropped-item')
const killCounter = document.getElementById('kill-count')
const removeItem = document.getElementById('remove-item')

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

function updateUI(data) {
	const inventoryItems = data.Inventory[1];
	const currentDrop = data.Inventory[2];
	const totalKills = data.Inventory[3];
	currentItem = `${currentDrop['name']}`

	itemList.innerHTML = '';
	droppedItem.innerHTML = currentDrop?.name || 'No item';
	document.getElementById('dropped-item-details').textContent = `Drop Details: Amount: ${currentDrop['quantity'].toLocaleString() || 0} Value: ${Number(currentDrop['value']).toLocaleString() || 0} gp`
	killCounter.textContent = `Total Kills: ${totalKills || 0}`

	for (const key in inventoryItems) {
		const newItem = document.createElement('li');
		newItem.textContent = `${key}: Amount: ${inventoryItems[key]['quantity'].toLocaleString() || 0} - Value: ${inventoryItems[key]['value'].toLocaleString() || 0} gp`;
		itemList.appendChild(newItem)
	}

}

getDropButton.addEventListener('click', async (e) => {
	e.preventDefault();
	let data = await getData();
	updateUI(data)
	// let inventoryItems = data.Inventory[1]
	// let currentDrop = data.Inventory[2]
	// let totalKills = data.Inventory[3]
	// console.log(currentDrop['name'])
	// currentItem = `${currentDrop['name']}`

	// for (const key in inventoryItems) {
	// 	const newItem = document.createElement('li');
	// 	newItem.textContent = `${key}: Amount: ${inventoryItems[key]['quantity']} - Value: ${inventoryItems[key]['value']} gp`;
	// 	droppedItem.textContent = `${currentDrop['name']}`
	// 	document.getElementById('dropped-item-details').textContent = `Drop Details: Amount: ${currentDrop['quantity']} Value: ${currentDrop['value']} gp`
	// 	killCounter.textContent = `Total Kills: ${totalKills}`
	// 	itemList.classList.add('list-group-item')
	// 	itemList.appendChild(newItem)
	// };
});



removeItem.addEventListener('click', (e) => {
	e.preventDefault();
	fetch(`http://127.0.0.1:5000/get-drop/${currentItem}`).catch(console.error)
})