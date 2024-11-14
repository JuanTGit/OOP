
async function getData() {
	let req = await fetch("http://127.0.0.1:5000/get-drop")
	let data = await req.json()
	console.log(data)
}
// getData()


// async () => {
// 	let req = await fetch("http://127.0.0.1:5000/get-drop")
// 	let data = await req.json()
// 	console.log(data)
// }


getData()