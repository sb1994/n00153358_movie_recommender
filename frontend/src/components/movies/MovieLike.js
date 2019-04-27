import React, { Component } from 'react'
import {
  connect
} from "react-redux";
import axios from 'axios'

class MovieLike extends Component {
  constructor(props){
    super(props)
    this.state={
      numLikes:0,
      isLiked:false,
      value:''
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this); 
 }
 handleChange(event) {
  this.setState({value: event.target.value});
}

handleSubmit(event) {
  alert('Rating is: ' + this.state.value);
  event.preventDefault();
  axios.post('http://localhost:8000/api/comment/create/', newComment, {
            headers: {
              "Authorization": `Bearer ${this.props.token}`
            }
          })
         .then((result) => {
          console.log(result);
          
          const movieID = this.props.match.params.id
            // // console.log(this.props.match.params);
            
            axios.get(`http://localhost:8000/api/rating/${movieID}`)
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


  componentDidMount(){
    // axios.get('')
  }
  render() {
    return (
      <div className="col-md-12">
        <<form onSubmit={this.handleSubmit}>
        <label>
          Pick your favorite flavor:
          <select value={this.state.value} onChange={this.handleChange}>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
          </select>
        </label>
        <input type="submit" value="Submit" />
      </form>
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

export default connect(mapStateToProps)(MovieLike);