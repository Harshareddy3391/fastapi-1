from fastapi import FastAPI




#create fast api app
app=FastAPI()

'''
usage: Application root
url:http://localhost:8010/
method type : Get
Required feilds:None
access type : public

'''
@app.get("/")
def index_page():
    return {"message":"index_page"}


'''
usage: Application root
url:http://localhost:8000/home
method type : Get
Required feilds:None
access type : public

'''

@app.get("/about")
def about_page():

    return {"message":"about_page"}


@app.get("/home")
def about():
    return {"message":"home_page"}

@app.post("/create")
def create():
    return {"message":"create data"}

@app.delete("/delate")
def delate():
    return {"message":"delate_data"}
@app.put("/post")
def put_data():
    return {"message":"post_dataa"}
