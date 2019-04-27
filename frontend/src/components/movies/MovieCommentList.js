import React, { Component } from 'react'
import {Link} from 'react-router-dom'
import {
  connect
} from "react-redux";
import axios from 'axios'
class MovieCommentList extends Component {
  constructor(props){
    super(props)
    this.state={
      comments:[],
      movie: '',
      comment:''
    }
  }
  componentDidMount(){
    console.log(this.props);
    
  }
  
  handleCommentClick=(e)=>{
    console.log(this.state);
  }
  render() {
    return (
      < div style = {{backgroundColor: "red"}} className="col-md-12">
        <p>This is the movie comment section</p>
        <p>{this.props.id}</p>
        {
          //checks wether user can comment or not
          this.props.isAuthenticated ?
          <div className="col-md-12">
            <p>You are authenticatied</p> 
            
            <button className = "btn btn-primary" onClick = {this.handleCommentClick}> Comment </button>
          </div>
          :
          <p>Your not authenticatied please <Link to='/login'>Login</Link></p>
        }
        <p>this is is comment</p>
        

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

export default connect(mapStateToProps)(MovieCommentList);