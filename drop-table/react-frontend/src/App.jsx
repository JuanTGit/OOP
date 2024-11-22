import './App.css'
import DropSimulator from './components/DropSimulator'
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from './components/Navbar'
import SearchContent from './components/Search'

function App() {
    return (
		<div className='container'>
			<Router>
				<Navbar />
				<Routes>
					<Route path='/' element={<SearchContent />} />
				</Routes>
			</Router>
		</div>
    )
}

export default App
