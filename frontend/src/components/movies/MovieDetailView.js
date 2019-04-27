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
import MovieRecommender from'./MovieRecommender'

// let jwtDecode = require('jwt-decode')

class MovieDetail extends Component {
  constructor(props) {
    super(props)
    this.state = {
      movie:{},
      comments:[],
      movie_id: this.props.match.params.id,
      comment:'',
      savedComment:{}
    }
    this.handleCommentClick = this.handleCommentClick.bind(this)
    this.handleCommentInputChange = this.handleCommentInputChange.bind(this)
  }
  handleCommentClick = (e) => {
    // console.log(this.state);
    let newComment ={
      movie_id:this.state.movie_id,
      comment:this.state.comment
    }
    // console.log(jwtDecode(this.props.token));

    axios.post('http://localhost:8000/api/comment/create/', newComment, {
            headers: {
              "Authorization": `Bearer ${this.props.token}`
            }
          })
         .then((result) => {
          console.log(result);
          
          const movieID = this.props.match.params.id
            // // console.log(this.props.match.params);
            
            axios.get(`http://localhost:8000/api/movie/${movieID}`)
              .then((response) => {
                this.setState({
                  // movie: response.data,
                  comments:response.data.comments
                })
                console.log(response.data);
                
                // console.log(this.state);
                // console.log(this.state);
              }).catch((err) => {
                console.log(err);
              });
              // console.log(this.state);
           
         }).catch((err) => {
           console.log(err);
         });
  }
  handleCommentInputChange = (e) => {
    this.setState({
      comment: e.target.value
    })
  }
  componentDidMount() {
    const movieID = this.props.match.params.id
    // console.log(this.props.match.params);
    
    axios.get(`http://localhost:8000/api/movie/${movieID}`)
      .then((response) => {
        this.setState({
          movie: response.data,
          comments:response.data.comments
        })
      }).catch((err) => {
        console.log(err);
      });
    
  }
  render() {
    let commentList =  this.state.comments.map(comment=><MovieComment key={comment.id} comment={comment}/>)
    let thumbnail = `https://image.tmdb.org/t/p/w185${this.state.movie.poster_path}`
    return ( 
      <div >
        <div className="row" style = {{backgroundColor: "blue"}}>
          <div className="col-md-12">
            <p>{this.state.movie.title}</p>
            <p>{this.state.movie.overview}</p>
            <p><span>Runtime:</span>{this.state.movie.runtime}</p>
            <p>{this.state.movie.release_date}</p>
            <img src={thumbnail} className="img-responsive"/>
          </div>
        </div>
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
          {/* <MovieCommentList tmdb_id={this.state.movie.tmdb_id} comments={this.state.comments}/> */}
          {commentList}
          {/* <p style = {{backgroundColor: "green"}}>{this.props.token}</p> */}
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

export default connect(mapStateToProps)(MovieDetail);