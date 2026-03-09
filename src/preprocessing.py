import pandas as pd


def handle_missing_year(data):
    """
    Fill missing year values with 'Unknown'
    """
    data["year"] = data["year"].fillna("Unknown")
    return data


def remove_duplicates(data):
    """
    Remove duplicate user-movie ratings
    """
    data = data.drop_duplicates(subset=["userId", "movieId"])
    return data


def filter_sparse_users(data, min_ratings=100):
    """
    Remove users with very few ratings
    """
    user_counts = data["userId"].value_counts()
    active_users = user_counts[user_counts >= min_ratings].index

    return data[data["userId"].isin(active_users)]


def filter_sparse_movies(data, min_ratings=200):
    """
    Remove movies with very few ratings
    """
    movie_counts = data["movieId"].value_counts()
    popular_movies = movie_counts[movie_counts >= min_ratings].index

    return data[data["movieId"].isin(popular_movies)]


def convert_timestamp(data):
    """
    Convert timestamp to datetime
    """
    data["timestamp"] = pd.to_datetime(data["timestamp"], unit="s")
    return data