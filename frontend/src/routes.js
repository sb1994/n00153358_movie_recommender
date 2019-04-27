import React from 'react'
import { Route } from "react-router-dom";
import MovieList from './components/movies/MovieListView'
import MovieDetail from './components/movies/MovieDetailView'
import RegisterForm  from "./components/auth/RegisterForm";
import  LoginForm from "./components/auth/LoginForm";
const BaseRouter = ()=> {
  return (
    <div>
      <Route exact path='/movies' component={MovieList}/>
      <Route exact path='/movies/:id' component={MovieDetail}/>
      <Route exact path='/login' component={LoginForm}/>
      <Route exact path='/register' component={RegisterForm}/>
    </div>
  )
}

export default BaseRouter