

const FeaturedGame = ({ cardInfo }) => {

	return(
		<div className="card" style={{width: 18 + "rem"}}>
			<img src={cardInfo.image} className="card-img-top" alt="..."/>
			<div className="card-body">
				<p className="card-text">Loot {cardInfo.name}!</p>
			</div>
		</div>
	)
}

export default FeaturedGame;