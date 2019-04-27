import React, { Component } from 'react'
import {Link} from 'react-router-dom'
class MovieThumbnail extends Component {
  constructor(props) {
    super(props)
    this.state={
      movie:this.props.movie
    }
  }
  render() {
    let thumbnail = "https://image.tmdb.org/t/p/w185/" +  this.state.movie.poster_path
    return (
      // < div className ={ "card col-md-3 col-sm-4"+(this.state.isLiked? ' liked':'')} >
      < div className = "card col-md-3 col-sm-4">
        <Link to={`/movies/${this.state.movie.id}`}>
          < img className="card-img-top img-responsive"
            src={thumbnail} alt="" /> 
        </Link>
        < div className = "card-body" >
          < Link to = {
            `/movies/${this.state.movie.id}`
          } >
            <h2 className = "card-title" >{this.state.movie.title} </h2> 
          </ Link>
          <p>{this.state.isLiked}</p>
          {/* < button
          className = "btn btn-primary" type="button" onClick={this.handleLikeClick} > <i className= "fa fa-thumbs-up" ></i>Like </ button > */}
        </div>
       </div>
    )
  }
}
export default MovieThumbnail
