import { useState } from "react"
import DropSimulator from "./DropSimulator";

const SearchContent = () => {
	const [boss, setBoss] = useState({boss: ''})
	const [bossData, setBossData] = useState(null);

	const handleChange = (e) => {
		console.log(e)
		setBoss({boss: e.target.value});
	}

	const getBossData = async (e) => {
		e.preventDefault();
		const response = await fetch('http://127.0.0.1:5000/get-boss', {
			method: "POST",
			headers: {
				'content-type': 'application/json',
			},
			body: JSON.stringify(boss)
		})
		const result = await response.json()
		setBossData([result, boss.boss])
	}


	return(
		<div className="row text-center justify-content-center align-items-center vh-100">
			<div className="col-8">
			<h1>Drop Simulator!</h1>
				<form className="input-group" onSubmit={getBossData}>
                    <input
                        type="text"
                        className="form-control"
                        placeholder="Enter Boss Name"
                        aria-label="Boss's username"
                        aria-describedby="button-addon2"
                        value={boss.boss}
                        onChange={handleChange}
                    />
                    <button
                        className="btn btn-success"
                        type="submit"
                        id="button-addon2"
                    >
                        Search
                    </button>
                </form>
			</div>
			{bossData && <DropSimulator bossData={bossData}/>}
		</div>
	)
}

export default SearchContent