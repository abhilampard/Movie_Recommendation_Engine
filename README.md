# Movie Recommendation Engine
## Collaborative Filtering

* Collaborative Filtering simply put uses the "wisdom of the crowd" to recommend items. 

* Item based collaborative filtering uses the patterns of users who liked the same movie as me to recommend me a movie (users who liked the movie that I like, also liked these other movies).

* Recommendation based on user's input of any movie present in the dataset is done.

## Dataset
The following main data source was used for this project:
- [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/)

## Data Pre-processing

- Dropping columns that are not required

- Merging dataframes

## Pivot Table 

![Pivot_Table](https://github.com/abhilampard/Movie_Recommendation_Engine/blob/master/Pivot_Table.PNG)

- Pivot tables give you the ability to look at data in so many different ways.


- Pivot table is created as shown in the image with Movies as rows, Users as columns and Ratings as values. 

## Cosine Similarity

- Also known as vector-based similarity, this formulation views two items and their ratings as vectors, and defines the similarity between them as the angle between these vectors:

![itembased-cosine](https://github.com/abhilampard/Movie_Recommendation_Engine/blob/master/itembased-cosine.png)


## Recommender

- User enters his favourite movie (or the movie on the basis of which he wants the system to recommend movies)

- Based on the user's input, recommendation is made by sorting the similarities in descending order

## References

- Schafer, J. B., Frankowski, D., Herlocker, J., & Sen, S. (2007). Collaborative filtering recommender systems. In The Adaptive Web (pp. 291-324). Springer Berlin Heidelberg.



