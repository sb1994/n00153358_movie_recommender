import React, { Component } from 'react'
import { Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import * as actions from '../store/actions/auth';
// const BaseLayout =(props)=> {
//   return (
//     <div>
//       <nav className="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
//         <li className="nav-item">
//           {
//             props.isAuthenticated ?
//             <button className="btn btn-primary">
//               logout
//             </button>
//             :
//             <Link to="/login">Login</Link>
//           }  
//         </li>
//         <li className="nav-item">
//           <Link to="/movies">Movies</Link>
//         </li>
//         {/* <li className="nav-item">
//           <a className="nav-link" href="#">Link</a>
//         </li>
//         <li className="nav-item">
//           <a className="nav-link" href="#">Link</a>
//         </li>
//         <li className="nav-item">
//           <a className="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
//         </li> */}
//       </nav>
//       <div className="container">
//       {props.children}
//       </div>
//       <footer>
//         this is the footer
//       </footer>
//     </div>
//   )
// }


class BaseLayout extends Component {
  render() {
    return (
      <div>
      <nav className="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
        <li className="nav-item">
          {
            this.props.isAuthenticated ?
            <button className="btn btn-primary" onClick={this.props.handleLogout}>
              logout
            </button>
            :
            <Link to="/login">Login</Link>
          }  
        </li>
        <li className="nav-item">
          <Link to="/movies">Movies</Link>
        </li>
        {/* <li className="nav-item">
          <a className="nav-link" href="#">Link</a>
        </li>
        <li className="nav-item">
          <a className="nav-link" href="#">Link</a>
        </li>
        <li className="nav-item">
          <a className="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
        </li> */}
      </nav>
      <div className="container">
      {this.props.children}
      </div>
      <footer>
        this is the footer
      </footer>
    </div>
    )
  }
}
const mapDispatchToProps = dispatch => {
  return {
    handleLogout: () => dispatch(actions.logout())
  }
}

export default withRouter(connect(null, mapDispatchToProps)(BaseLayout));
