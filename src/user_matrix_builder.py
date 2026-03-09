import pandas as pd
def create_user_movie_matrix(data):

    user_movie_matrix = data.pivot_table(
        index = "userId",
        columns = "movieId",
        values = "rating",
        aggfunc = "mean"
    ).fillna(0)

    return user_movie_matrix

def save_user_movie_matrix(matrix,path):
    matrix.to_pickle(path)
    