import { useState } from "react"
import DropSimulator from "./DropSimulator";
import npcData from '../assets/NpcID.json'
import FeaturedGame from "../components/FeaturedGame";

const SearchContent = () => {
	const [boss, setBoss] = useState({boss: ''})
	const [bossData, setBossData] = useState(null);
	const [suggestions, setSuggestions] = useState([]);
	const [featured, setFeatured] = useState([{name: 'Nex', image: 'https://oldschool.runescape.wiki/images/thumb/Nex.png/270px-Nex.png?2a1b3'}, 
	 										  {name: 'Araxxor', image: 'https://oldschool.runescape.wiki/images/thumb/Araxxor.png/280px-Araxxor.png?35d2e'}, 
											  {name: 'Zulrah', image: 'https://oldschool.runescape.wiki/images/thumb/Zulrah_%28serpentine%29.png/250px-Zulrah_%28serpentine%29.png?29a54'}, 
											  {name: 'Vardorvis', image: 'https://oldschool.runescape.wiki/images/thumb/Vardorvis.png/200px-Vardorvis.png?48af8'}]);

	const handleChange = (e) => {
		const input = e.target.value
		setBoss({boss: input});


		if (input.length > 0) {
            const filteredSuggestions = Object.keys(npcData).filter((npc) =>
                npc.toLowerCase().includes(input.toLowerCase())
            );
            setSuggestions(filteredSuggestions.slice(0, 10));
        } else {
            setSuggestions([]);
        }
	}
	const handleSuggestionClick = async (npcName) => {
		console.log(featured)
		setBoss({ boss: npcName }); // Update the state
		setSuggestions([]);         // Clear suggestions
		
		// Trigger getBossData directly
		const data = await getBossData(npcName);
		console.log(data)
		setBossData([data, npcName]);
		// console.log(data)
		setFeatured((prev) => {
			const updated = [...prev.filter(boss => boss.name !== npcName), { name: npcName, image: data?.Inventory[4] }];
			
			return updated.slice(-6);
		}
		)

	};
	
	const getBossData = async (npcName) => {
		try{
			const response = await fetch('http://127.0.0.1:5000/get-boss', {
				method: "POST",
				headers: {
					'content-type': 'application/json',
				},
				body: JSON.stringify({ boss: npcName })
			});

			if (!response.ok) {
				throw new Error(`Server responded with status: ${response.status}`);
			}
			const result = await response.json();
			console.log(result)
			return result
		} catch (error) {
			console.error('error fetching boss data in search', error)
			alert('Please enter a valid NPC')
		}
	};


	return(
		<div className="row text-center content-area">
			<div className="col-10 col-md-8">
			<h1 className="search-title">Drop Simulator!</h1>
				<form className="search-bar input-group" onSubmit={(e) => {
													e.preventDefault()
													getBossData(boss.boss)}}>
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
				{/* Suggestions List */}
                {suggestions.length > 0 && (
                    <ul className="list-group position-absolute mt-2" style={{ maxHeight: '200px', overflowY: 'auto' }}>
                        {suggestions.map((npc, index) => (
                            <li
                                key={index}
                                className="list-group-item list-group-item-action"
                                onClick={() => handleSuggestionClick(npc)}
                            >
                                {npc}
                            </li>
                        ))}
                    </ul>
                )}
			</div>
			{bossData ?
			(<DropSimulator bossData={bossData}/>)
			:
			(<div className="row">
				{featured.map((game, index) => (
					<FeaturedGame key={index} cardInfo={game}/>
				))}
			</div>)
			}
		</div>
	)
}

export default SearchContent