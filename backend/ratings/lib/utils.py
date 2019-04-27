import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
import random
import math
from scipy.spatial.distance import cosine 


import numpy as np
import warnings
warnings.filterwarnings('ignore')
def recommendations(currentUser):
  return movieRecommendations(currentUser,5)


def userSimularity(currentUser,user_2):
  currentUser=np.array(currentUser)-np.nanmean(currentUser) 
    
  user_2=np.array(user_2)-np.nanmean(user_2)
  #get the shared movie ids 
  sharedMovieRatingIds=[i for i in range(len(currentUser)) if currentUser[i]>0 and user_2[i]>0]
  
  if len(sharedMovieRatingIds)==0:   
    return 0
  else:
    #creates and array of of of the values of the ratiangs and puts them into the correlation method
    currentUser=np.array([currentUser[i] for i in sharedMovieRatingIds])
    user_2=np.array([user_2[i] for i in sharedMovieRatingIds])
    return cosine(currentUser,user_2)

def nearestMovieUserNeigbourRatings(currentUser,k,):
  connection = pg.connect("host='127.0.0.1' dbname=movie_recommender user=postgres password='postgres'")
  if connection:
    print('You are connected')
  # dataframe = psql.DataFrame("SELECT * FROM ratings_rating", connection)
  #get the list of movies and puts it into a dataframe
  movies_sql = "select id,title from movies_movie "
  df_movies = pd.DataFrame(pd.read_sql_query(movies_sql,con=connection))
  # df_movies.head()

  #gets movie ratings
  ratings_sql = "select user_id,movie_id,rating from ratings_rating"
  df_ratings = pd.DataFrame(pd.read_sql_query(ratings_sql,con=connection))
  movie_ratings=pd.merge(df_ratings,df_movies, left_on='movie_id', right_on='id')
  movie_ratings = pd.DataFrame(movie_ratings.drop(movie_ratings.columns[[3]], axis=1) )
  movie_ratings['rating'] = movie_ratings.rating.astype(float)
  movie_ratings['title'] = movie_ratings.title.astype(str)
  # movie_ratings.dtypes

  #makes the index of the dataframe to the user_id
  movieRatingMatrix=pd.pivot_table(movie_ratings, values='rating', index=['user_id'], columns=['movie_id'])
  #creates user simularity matrix that will be added to contain the id and the 
  #simularity of the neigbor to the current usr
  userSimularityMatrix=pd.DataFrame(index=movieRatingMatrix.index,columns=['simularity'])
  #loop the to check the user against the neighbor
  for i in movieRatingMatrix.index:
    userSimularityMatrix.loc[i]=userSimularity(movieRatingMatrix.loc[currentUser],movieRatingMatrix.loc[i])
  #sets the order of the users nearest neighbors so the highest comes first and so on
  userSimularityMatrix=pd.DataFrame.sort_values(userSimularityMatrix,['simularity'],ascending=False)
  #get the top nearest neigbours besed on the input value
  currentUserNearestNeigbours=userSimularityMatrix[:k]
  # creates a obejct that contains the curretn user neeigbours ratings 
  currentUserNeigbourMovieRatings=movieRatingMatrix.loc[currentUserNearestNeigbours.index]
  #empty datframe for the predictied ratings that uses the colums of the ratings of the movie ratings matrix as index
  predictMovieUserRating=pd.DataFrame(index=movieRatingMatrix.columns, columns=['rating'])
  #loop to populate the predictUserMovieRating dataframe
  for i in movieRatingMatrix.columns:
    # i for each row in the dataframe
    #get the mean of each movie that doesnt contain 
    predictedMovieRating=np.nanmean(movieRatingMatrix.loc[currentUser])
    # print(predictedUserMovieRating)
    # start with the average rating of the user
    for y in currentUserNeigbourMovieRatings.index:
      # eact neigbor in the datadrame 
      if movieRatingMatrix.loc[y,i]>0:
        #add mean of rted movie to the predicted Movierating if the neighbor has voted for the movie
        predictedMovieRating += (movieRatingMatrix.loc[y,i]-np.nanmean(movieRatingMatrix.loc[y]))*currentUserNearestNeigbours.loc[y,'simularity']
    #contains a that dataframe that contains the predicted ratings for the movie for the curretn user
    predictMovieUserRating.loc[i,'rating']=predictedMovieRating
  return predictMovieUserRating

def movieRecommendations(currentUser,n):
  connection = pg.connect("host='127.0.0.1' dbname=movie_recommender user=postgres password='postgres'")
  if connection:
    print('You are connected')
  # dataframe = psql.DataFrame("SELECT * FROM ratings_rating", connection)
  #get the list of movies and puts it into a dataframe
  movies_sql = "select id,title from movies_movie "
  df_movies = pd.DataFrame(pd.read_sql_query(movies_sql,con=connection))
  # df_movies.head()

  #gets movie ratings
  ratings_sql = "select user_id,movie_id,rating from ratings_rating"
  df_ratings = pd.DataFrame(pd.read_sql_query(ratings_sql,con=connection))
  movie_ratings=pd.merge(df_ratings,df_movies, left_on='movie_id', right_on='id')
  movie_ratings = pd.DataFrame(movie_ratings.drop(movie_ratings.columns[[3]], axis=1) )
  movie_ratings['rating'] = movie_ratings.rating.astype(float)
  movie_ratings['title'] = movie_ratings.title.astype(str)
  # movie_ratings.dtypes

  #makes the index of the dataframe to the user_id
  movieRatingMatrix=pd.pivot_table(movie_ratings, values='rating', index=['user_id'], columns=['movie_id'])
  # gets 10 previous neigobor ratings for eact movies 
  predictUserMovieRatings=nearestMovieUserNeigbourRatings(currentUser,10)
  #get a list og the current users prevous ratings  based on the index of the movies_ratings dataframe
  currentUserMoviesPreviousRated=list(movieRatingMatrix.loc[currentUser].loc[movieRatingMatrix.loc[currentUser]>0].index)
  #drops nan vals
  predictUserMovieRatings=predictUserMovieRatings.drop(currentUserMoviesPreviousRated)
  #sort the dataframe
  movieRecommendations=pd.DataFrame.sort_values(predictUserMovieRatings,['rating','movie_id'],ascending=False)[:10]
  # for row in movieRecommendations.rows:
  #  print (movieRecommendations[row])
  # movie_ids= movieRecommendations.movie_id.unique()

  movieIdMatrix=pd.pivot_table(movieRecommendations, values='movie_id',  columns=['movie_id'])
  
  
  
  return(movieIdMatrix)