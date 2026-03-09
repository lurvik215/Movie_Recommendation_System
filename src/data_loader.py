import pandas as pd

def load_movies(path="../DataSets/movies.csv"):
    movies = pd.read_csv(path)
    return movies


def load_ratings(path="../DataSets/ratings.csv"):
    ratings = pd.read_csv(path)
    return ratings


def merge_datasets(movies, ratings):
    df = pd.merge(ratings, movies, on="movieId")
    return df

def save_dataset(df, path):
    df.to_csv(path, index=False)


def load_data(path):
    return pd.read_csv(path)