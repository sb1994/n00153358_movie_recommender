import React, { Component } from 'react'
import MovieThumbnail from './MovieThumbnail';
import axios from 'axios'

 class MovieList extends Component {
  constructor(props){
    super(props)
    this.state={
      movies:[],
      count:'',
      next:'',
      previous:'' 
    }
  }
  componentDidMount(){
    // const listData = [];
    // for (let i = 0; i < 23; i++) {
    //   listData.push({
    //     href: 'http://ant.design',
    //     title: `ant design part ${i}`,
    //     avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    //     description: 'Ant Design, a design language for background applications, is refined by Ant UED Team.',
    //     content: 'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
    //   });
    // }
    // this.setState({
    //   articales:listData
    // })
    axios.get('http://localhost:8000/api/movie/')
         .then((response) => {
           this.setState({
             movies:response.data.results,
             count:response.data.count,
             previous:response.data.previous,
             next:response.data.next,
           })
           console.log(this.state);
           
           
         }).catch((err) => {
           console.log(err);
         });

  }
  render() {
      let movieList =  this.state.movies.map(movie=><MovieThumbnail key={movie.id}movie={movie}/>)
    return (
      // <Movie data={this.state.movies}/>
      <div className='container'>
        <div className="row">
          {movieList}
        </div>
      </div>
    )
  }
}
export default MovieList