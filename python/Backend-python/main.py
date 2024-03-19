from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello world !!"}


@app.get("/posts")
def get_posts():
    return {"Data":"This is your post"} 

@app.post("/createpost")
def create_post(payload:dict=Body(...)):
    print(payload)
    return {"msg":"Successfully created post "}
