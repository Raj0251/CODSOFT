# recommend.py - Simple content-based movie recommender using genres
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def build_data():
    data = pd.DataFrame({
        'title': [
            'Inception', 'Interstellar', 'The Dark Knight', 'Shutter Island',
            'Titanic', 'The Matrix', 'The Prestige', 'Memento'
        ],
        'genre': [
            'Sci-Fi Thriller', 'Sci-Fi Drama', 'Action Crime', 'Thriller Mystery',
            'Romance Drama', 'Sci-Fi Action', 'Drama Mystery', 'Mystery Thriller'
        ],
        'year': [2010,2014,2008,2010,1997,1999,2006,2000]
    })
    return data

def build_model(data):
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['genre'])
    similarity = cosine_similarity(count_matrix)
    return similarity, cv

def recommend(title, data, similarity, topn=3):
    if title not in list(data['title']):
        return []
    idx = data[data.title == title].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recommendations = [data.iloc[i[0]].title for i in scores[1: topn+1]]
    return recommendations

if __name__ == '__main__':
    data = build_data()
    similarity, cv = build_model(data)
    query = 'Inception'
    print('Dataset:')
    print(data.to_string(index=False))
    print('\nRecommendations for:', query)
    print(recommend(query, data, similarity, topn=3))
