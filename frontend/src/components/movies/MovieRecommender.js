import React, {
  Component
} from 'react'
import {
  Link
} from 'react-router-dom'
import {
  connect
} from "react-redux";
import axios from 'axios'
import MovieComment from './MovieComment'
import MovieLike from './MovieLike';

// let jwtDecode = require('jwt-decode')

class MovieRecommender extends Component {
  constructor(props) {
    super(props)
    this.state = {
      movie:{},
      comments:[],
      movie_id: this.props.match.params.id,
    }
  }
  handleCommentClick = (e) => {
    // console.log(this.state);
    let newComment ={
      movie_id:this.state.movie_id,
      comment:this.state.comment
    }
    // console.log(jwtDecode(this.props.token));
  componentDidMount() {
    const movieID = this.props.match.params.id
    // console.log(this.props.match.params);
    
    axios.get(`http://localhost:8000/api/rating/recommender`)
      .then((response) => {
        this.setState({
          movies: response.data,
        })
      }).catch((err) => {
        console.log(err);
      });
    
  }
  render() {
    
    return ( 
      <div >
        <div className="row">
        {
            //checks wether user can comment or not
            this.props.isAuthenticated ?
            <div className="col-md-12">
              {/* <MovieLike tmdb_id={this.state.movie.tmdb_id}/> */}
            </div>
            :
            <p>Login to like this movie <Link to='/login'>Login</Link></p>
          } 
        </div>
        <div className="row danger">
          
          {/* <p>This is the movie comment section</p> */}
          {/* <p>{this.props.id}</p> */}
          {
            //checks wether user can comment or not
            this.props.isAuthenticated ?
            <div className="col-md-12">
              <p>You are authenticatied</p>

              <input value={this.state.value} onChange={this.handleCommentInputChange} />
              <button className = "btn btn-primary" onClick = {this.handleCommentClick}> Comment </button>
            </div>
            :
            <p>Your not authenticatied please <Link to='/login'>Login</Link></p>
          } 
          
        </div>
        <div className="row danger">
          {this.props.movies}
        </div>
      </div>
      
    )
  }
}
const mapStateToProps = state => {
  return {
    token: state.token,
    // isAuthenticated:state.isAuthenticated
    isAuthenticated: state.token !== null
  };
};

export default connect(mapStateToProps)(MovieRecommender);