import React, { Component } from 'react'

export default class MovieComment extends Component {
  constructor(props) {
    super(props)
    this.state={
      comment:this.props.comment
    }
  }
  render() {
    return (
      <div style = {{backgroundColor: "red"}} className='col-md-12'>
        <div className="col-md-2">
        <img src={this.props.comment.user.avatar} alt="" className="img-responsive"/>
        </div>
        <p>{this.props.comment.user.username}</p>
        <p>{this.props.comment.comment}</p>
      </div>
    )
  }
}
