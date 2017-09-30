import numpy as np
import pandas as pd
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine, correlation

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('u.data', sep='\t', names=r_cols,
                      encoding='latin-1')

m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(5),
                     encoding='latin-1')

movie_ratings = pd.merge(movies, ratings)

#Dropping the columns that are not required
ratings.drop( "unix_timestamp", inplace = True, axis = 1 )
movies.drop(movies.columns[[3,4]], inplace = True, axis = 1 )

#Creating a pivot table with the following parameters
ratings_matrix = ratings.pivot_table(index=['movie_id'],columns=['user_id'],values='rating').reset_index(drop=True)
ratings_matrix.fillna( 0, inplace = True )

#Calculating Cosine Similiarities
movie_similarity = 1 - pairwise_distances( ratings_matrix.as_matrix(), metric="cosine" )

#Filling diagonals with 0s instead of 1 to avoid recommending the same movie when sorting
np.fill_diagonal( movie_similarity, 0 )
ratings_matrix = pd.DataFrame( movie_similarity )

try:
    user_inp=input('Enter the reference movie title based on which recommendations are to be made: ')
    inp = movies[movies['title'] == user_inp].index.tolist()
    inp = inp[0]

    movies['similarity'] = ratings_matrix.iloc[inp]
    movies.columns = ['movie_id', 'title', 'release_date', 'similarity']
    print("Recommended movies based on your choice of ", user_inp, ": \n",
          movies.sort_values(["similarity"], ascending=False)[1:10])

except:
    print("Sorry, the movie is not in the database!")




