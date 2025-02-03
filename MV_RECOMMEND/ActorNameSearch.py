import sqlite3


class ActorNameSearch:
    def actor_name_seach(name):
        db_path = "db/data.db"
        # DB 연결
        con = sqlite3.connect(db_path)
        cur = con.cursor()

        # 해당 배우의 영화 목록 가져오기
        cur.execute(f"SELECT * FROM data WHERE actor LIKE '%{name}%'")
        movie_data = cur.fetchall()
        movielist = []
        datas = {}
        size = min(len(movie_data), 5)

        
        for i in enumerate(movie_data[:size]):
            movie = movie_data[i]
            data = {"title" : movie[1], "theme" : movie[2], "actor" : movie[3], "director" : movie[4], "time" : movie[6], "limit_age" : movie[7], "poster" : movie[8], "story" : movie[9]}
            datas[f"movie{i + 1}"] = data

        return datas
