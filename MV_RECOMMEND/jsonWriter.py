import json

def createJSON(list):
    filename = "./movies.json"
    data = {}
    data['movies'] = []
    for movie in list:
        data['movies'].append({
        "title": str(movie[0]),
        "theme": str(movie[1]),
        "actor": str(movie[2]),
        "director": str(movie[3]),
        "time": str(movie[4]),
        "limit_age": str(movie[5]),
        "poster": str(movie[6]),
        "story": str(movie[7]),
    })
    with open(filename, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)
    
