import React, { Component } from 'react';
import {BrowserRouter as Router} from'react-router-dom'
import BaseLayout from './containers/BaseLayout'
import { connect } from 'react-redux';
import * as actions from './store/actions/auth';
import  BaseRouter  from "./routes";
class App extends Component {
  componentDidMount() {
    this.props.onTrySignup();
  }
  render() {
    return (
      <div>
        <Router>
          <BaseLayout {...this.props}>
            <BaseRouter/>
          </BaseLayout>
        </Router>
      </div>
    );
  }
}
const mapStateToProps = state => {
  return {
    isAuthenticated: state.token !== null
  }
}

const mapDispatchToProps = dispatch => {
  return {
    onTrySignup: () => dispatch(actions.checkAuthState())
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(App);
