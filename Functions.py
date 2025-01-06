import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_tfidf_similarity(sentence1, sentence2):
    # Remove dots and normalize text
    sentence1 = re.sub(r'[^\w\s]', '', sentence1.lower())
    sentence2 = re.sub(r'[^\w\s]', '', sentence2.lower())

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([sentence1, sentence2])
    similarity = cosine_similarity(vectors[0], vectors[1])
    percentage_similarity = similarity[0][0] * 100
    return percentage_similarity