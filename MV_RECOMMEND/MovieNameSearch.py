from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import sqlite3
from Recommend import Recommend as rec

class MovieNameSearch:
    def mv_name_search(title):
        # DB 불러오기
        connection = sqlite3.connect("db/data.db")

        # 테이블 읽기
        data = pd.read_sql("SELECT * FROM data;", connection)

        # TF-IDF 변환
        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform(data.storyWord)


        # 코사인 유사도 구하기
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        """인덱스 테이블 만들기"""
        indices = pd.Series(data.index, index = data.title).drop_duplicates()

        return rec.mv_name(data, indices, title, cosine_sim)
