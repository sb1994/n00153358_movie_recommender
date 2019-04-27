import axios from 'axios';
import * as types from './types';

export const startAuth = () => {
  return {
    type: types.START_AUTH
  }
}
export const successAuth = token => {
  return {
    type: types.SUCCESS_AUTH,
    token: token
  }
}
export const failAuth = error => {
  return {
    type: types.FAIL_AUTH,
    error: error
  }
}
export const loginAuth = (username, password) => {
  //alert that the login has started

  return dispatch => {
    dispatch(startAuth())
    axios.post('http://localhost:8000/api/user/login/', {
        username: username,
        password: password
      })
      .then((result) => {
        const token = result.data.token
        const user = result.data.user
        //sets the expirey date 
        const expire = new Date(new Date().getTime() + 10000 * 1000);

        //stores the the token and the expireation date in the browser
        //as a cookie
        localStorage.setItem('token', token)
        localStorage.setItem('user', user)
        dispatch(successAuth(token))

      }).catch((err) => {
        console.log(err);
      });
  }
}
export const logout = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('expirationDate');
  return {
    type: types.LOGOUT_AUTH
  };
}


export const checkAuthState = () => {
  return dispatch => {
    const token = localStorage.getItem('token');
    if (token === null) {
      dispatch(logout());
    } else {
      dispatch(successAuth(token));
    }
  }
}