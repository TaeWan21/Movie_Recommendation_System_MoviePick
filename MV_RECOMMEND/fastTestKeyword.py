from KeyWordSearch import KeyWordSearch as kws
from fastapi import FastAPI
import uvicorn

# 실행 후    uvicorn MV_RECOMMEND.fastTestKeyword:app --reload   터미널에 입력.


app = FastAPI()

@app.get("/")
def test():
    keyword = input('키워드를 입력하세요 : ')
    result = kws.keyword_search(keyword)
    print(result)
    return result
  
if __name__ == "__main__" :
  uvicorn.run("fastTestKeyword:app", reload=True)