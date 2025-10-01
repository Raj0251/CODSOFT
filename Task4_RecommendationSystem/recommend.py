# recommend.py (single input version)
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.DataFrame({
    'title': [
        'Inception', 'Interstellar', 'The Dark Knight', 'Shutter Island',
        'Titanic', 'The Matrix', 'The Prestige', 'Memento'
    ],
    'genre': [
        'Sci-Fi Thriller', 'Sci-Fi Drama', 'Action Crime', 'Thriller Mystery',
        'Romance Drama', 'Sci-Fi Action', 'Drama Mystery', 'Mystery Thriller'
    ]
})

cv = CountVectorizer()
count_matrix = cv.fit_transform(data['genre'])
similarity = cosine_similarity(count_matrix)

def recommend(movie):
    if movie not in list(data['title']):
        return []
    idx = data[data.title == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recs = [data.iloc[i[0]].title for i in scores[1:4]]
    return recs

if __name__ == "__main__":
    movie = input("Enter a movie: ")
    recs = recommend(movie)
    if recs:
        print("Recommended:", recs)
    else:
        print("Movie not found in dataset.")
