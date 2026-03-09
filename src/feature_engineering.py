
def rating_normalization(data):
    """
    Normalize ratings by subtracting user mean rating
    """
    data["rating_normalized"] = data.groupby("userId")["rating"].transform(
        lambda x: x - x.mean()
    )

    return data


def extract_decade(data):
    """
    Create decade feature from year
    """
    data["year"] = data["year"].replace("Unknown", None)
    data["year"] = data["year"].astype(float)

    data["decade"] = (data["year"] // 10) * 10

    return data


def genre_count(data):
    """
    Number of genres per movie
    """
    data["genre_count"] = data["genre_list"].apply(len)
    return data