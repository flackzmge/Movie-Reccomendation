# Collaborative Filtering Algorithm for Movie Recommendations

This is a basic collaborative filtering algorithm for making movie recommendations based on user ratings. It uses the data from the Movie Lens Small Latest Dataset, specifically the movies.csv, tags.csv, reviews.csv, and links.csv files.

Dataset: https://www.kaggle.com/datasets/shubhammehta21/movie-lens-small-latest-dataset

## How it works

The algorithm uses linear algebra to calculate the similarity between movies based on user ratings. When a user inputs the name of a movie and the number of similar movies they want to be recommended, the algorithm will output a list of movie recommendations.

## Dependencies

Python 3

Numpy

pandas

scipy

warnings


## Usage

To use the algorithm, first clone the repository:

```
git clone https://github.com/flackzmge/movie-recommendation.git
Next, navigate to the directory and run the following command, where [movie_name] is the name of the movie you want to get recommendations for and [num_recommendations] is the number of recommendations you want to receive:
``` 

```
python recommend.py [movie_name] [num_recommendations]
```
Example

Here is an example of how to use the algorithm to get recommendations for the movie "Toy Story":

```
python main.py "Toy Story (1995)" 5
```
This will output a list of the 5 most similar movies to "Toy Story (1995)", based on user ratings.

## Contributions

Contributions are welcome! If you have any ideas for improving the algorithm, please feel free to open a pull request.

## Limitations 

Reccomendations are done using the reviews. Te reviews only go up to 610 Movies so only movie 1-610 in movies.csv work. 

