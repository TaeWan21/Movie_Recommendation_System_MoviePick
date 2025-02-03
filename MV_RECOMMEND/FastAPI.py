from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from ActorNameSearch import ActorNameSearch as ans
from MovieNameSearch import MovieNameSearch as mns
from KeyWordSearch import KeyWordSearch as kws

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
    allow_credentials=True,
    expose_headers=["*"],
)

@app.post("/process_actor")
async def process_actor(data: dict):
    keyword = data.get("search")
    result = ans.actor_name_seach(keyword)
    return result

@app.post("/process_movie")
async def process_movie(data: dict):
    keyword = data.get("search")
    result = mns.mv_name_search(keyword)
    return result

@app.post("/process_keyword")
async def process_keyword(data: dict):
    keyword = data.get("search")
    result = kws.keyword_search(keyword)
    return result

@app.options("/process_actor")
@app.options("/process_movie")
@app.options("/process_keyword")
async def options_process_json(request: Request):
    return {"allow": "POST, OPTIONS"}
  
if __name__ == "__main__" :
    uvicorn.run("FastAPI:app", reload=True)