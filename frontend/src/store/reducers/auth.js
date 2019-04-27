import * as types from '../actions/types';
import { updateStateObject } from '../utility';

const initialState = {
  token: null,
  error: null,
  isLoading: false
}
const startAuth = (state, action) => {
  return updateStateObject(state, {
    error: null,
    loading: true
  });
}
const successAuth = (state, action) => {
  //takes in the action and returns the updated state
  //with the token
  return updateStateObject(state, {
    token: action.token,
    error: null,
    loading: false
  })
}
const failAuth = (state, action) => {
  //takes in the action and returns the updated state
  //with the error that was passed in as a parameter
  return updateStateObject(state, {
    error: action.error,
    loading: false
  })
}
const logoutAuth = (state, action) => {
  return updateStateObject(state, {
    //updates the state to tell the app that 
    //the token is null
    token: null
  })
}

//defines the reducer of when the actions take place
const reducer = (state = initialState, action) => {
  switch (action.type) {
    case types.START_AUTH:
      return startAuth(state, action)
    case types.FAIL_AUTH:
      return failAuth(state, action)
    case types.SUCCESS_AUTH:
      return successAuth(state, action)
    case types.LOGOUT_AUTH:
      return logoutAuth(state, action)
    default:
      return state
  }
}

export default reducer;
