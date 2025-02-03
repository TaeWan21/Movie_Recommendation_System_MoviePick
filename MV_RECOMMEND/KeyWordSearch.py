from gensim.models.word2vec import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import sqlite3
from Recommend import Recommend as rec
from precleaning import Precleaning  as pc
class KeyWordSearch:
  def keyword_search(keywords):
      model = Word2Vec.load('W2V/MV_Model')
      pre_clean_list = pc.preclean(keywords)
      sentence = []
      for word in pre_clean_list:
          labels = []
          sim_word = model.wv.most_similar(word, topn = 5)
          for label, _ in sim_word:
              labels.append(label)

          for i, word in enumerate(labels):
              sentence += [word] * (9-i)
      
      for keyword in keywords:
          sentence += [keyword] * 10
      sentence = ' '.join(sentence)
      
      # DB 불러오기
      connection = sqlite3.connect("db/data.db")

      # 테이블 읽기
      data = pd.read_sql("SELECT * FROM data;", connection)

      # TF-IDF 변환
      tfidf = TfidfVectorizer()
      tfidf_matrix = tfidf.fit_transform(data.storyWord)
      sentence_vec = tfidf.transform([sentence])  

      cosine_sim = linear_kernel(sentence_vec, tfidf_matrix) 

      return rec.key_word(data, cosine_sim) 


