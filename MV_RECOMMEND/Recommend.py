"""추천 해주기"""
class Recommend:

    def mv_name(data, indices, title, cosine_sim):
        
        # 입력한 영화로 부터 인덱스 가져오기
        idx = indices[title]

        # 모든 영화에 대해서 해당 영화와의 유사도를 구하기
        sim_scores = list(enumerate(cosine_sim[idx]))

        # 유사도에 따라 영화들을 정렬
        sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse = True)

        # 가장 유사한 5개의 영화를 받아옴
        sim_scores = sim_scores[1:6]

        # 가장 유사한 5개 영화의 인덱스 받아옴
        movie_indices = [i[0] for i in sim_scores]
        
        # 기존에 읽어들인 데이터에서 해당 인덱스의 값들을 가져온다. 그리고 스코어 열을 추가하여 코사인 유사도도 확인할 수 있게 한다.
        result_df = data.iloc[movie_indices].copy()
        result_df['sim_score'] = [i[1] for i in sim_scores]
        
        # 읽어들인 데이터에서 출력 필요없는 부분 제거 
        del result_df['storyWord']
        del result_df['score']
        del result_df['id']
        del result_df['keyword1']
        del result_df['keyword2']
        del result_df['keyword3']
        del result_df['keyword4']
        del result_df['keyword5']
        del result_df['sim_score']

        mv_list = result_df.values.tolist()
        datas = {}

        for i in range(5):
            movie = mv_list[i]
            data = {"title" : movie[0], "theme" : movie[1], "actor" : movie[2], "director" : movie[3], "time" : movie[4], "limit_age" : movie[5], "poster" : movie[6], "story" : movie[7]}
            datas[f"movie{i + 1}"] = data

         # 가장 유사한 5개의 영화의 제목을 리턴
        return datas
    
    def key_word(data, cosine_sim):
        # 각 코사인 유사도 값에 인덱스를 붙임
        simScore = list(enumerate(cosine_sim[-1]))
        # 코사인 유사도가 큰것부터 정렬
        simScore = sorted(simScore, key = lambda x:x[1], reverse = True)
        # 유사한 영화 5개 리스트
        simScore = simScore[1:6]
        movie_indices = [i[0] for i in simScore]
        
        result_df = data.iloc[movie_indices].copy()
        result_df['sim_score'] = [i[1] for i in simScore]
        
        # 읽어들인 데이터에서 출력 필요없는 부분 제거 
        del result_df['storyWord']
        del result_df['score']
        del result_df['id']
        del result_df['keyword1']
        del result_df['keyword2']
        del result_df['keyword3']
        del result_df['keyword4']
        del result_df['keyword5']
        del result_df['sim_score']

        mv_list = result_df.values.tolist()

        datas = {}

        for i in range(5):
            movie = mv_list[i]
            data = {"title" : movie[0], "theme" : movie[1], "actor" : movie[2], "director" : movie[3], "time" : movie[4], "limit_age" : movie[5], "poster" : movie[6], "story" : movie[7]}
            datas[f"movie{i + 1}"] = data

         # 가장 유사한 5개의 영화의 제목을 리턴
        return datas
       
        
