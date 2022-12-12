# Implement a basic collaborative filtering algorithm to make movie recommendations based on user ratings.
# Get the data from the Data folder.
# Represent the ratings matrix as a sparse matrix using scipy.
import numpy as np
import pandas as pd
import scipy.sparse as sp
from scipy.sparse.linalg import svds
import warnings
warnings.filterwarnings("ignore")

# Read the data
movies = pd.read_csv('Data/movies.csv')
ratings = pd.read_csv('Data/ratings.csv')
tags = pd.read_csv('Data/tags.csv')
links = pd.read_csv('Data/links.csv')

# Create a ratings matrix
ratings_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
ratings_matrix.fillna(0, inplace=True)

# Create a sparse matrix
ratings_matrix_sparse = sp.csr_matrix(ratings_matrix.values)

# Compute the SVD of the ratings matrix
U, sigma, Vt = svds(ratings_matrix_sparse, k=50)

# Convert the sigma matrix to a diagonal matrix
sigma = np.diag(sigma)

# Make predictions
all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + ratings_matrix.mean().mean()

# Convert the predictions to a dataframe
preds_df = pd.DataFrame(all_user_predicted_ratings, columns=ratings_matrix.columns)

# Get the movie titles
movie_titles = movies.set_index('movieId')['title'].to_dict()

# Get the movie IDs
movie_ids = movies.set_index('title')['movieId'].to_dict()

# Get the movie genres
movie_genres = movies.set_index('movieId')['genres'].to_dict()

# Get the movie IMDB IDs
movie_imdb_ids = links.set_index('movieId')['imdbId'].to_dict()

# Get the movie TMDB IDs
movie_tmdb_ids = links.set_index('movieId')['tmdbId'].to_dict()


# Get the movie recommendations
def get_movie_recommendations(movie_name, num_recommendations):
    # Get the movie ID
    movie_id = movie_ids[movie_name]
    # Get the movie row number
    movie_row_number = ratings_matrix.index.get_loc(movie_id)
    # Get the movie row
    movie_row = preds_df.iloc[movie_row_number]
    # Sort the movie row
    sorted_movie_row = movie_row.sort_values(ascending=False)
    # Get the top N recommendations
    top_n_recommendations = sorted_movie_row.iloc[1:num_recommendations+1]
    # Get the movie titles
    top_n_recommendations = top_n_recommendations.index.map(lambda x: movie_titles[x])
    # Return the top N recommendations
    return top_n_recommendations

# Get the movie recommendations by inputting a movie title and remove white spaces from the movie title
movie_name = input('Enter a movie title: ').strip()
#movie_name = input('Enter a movie title: ')

num_recommendations = int(input('Enter the number of recommendations: '))
movie_recommendations = get_movie_recommendations(movie_name, num_recommendations)
print()
print(movie_recommendations)
exit()



