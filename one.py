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
url:http://localhost:801/about
method type : Get
Required feilds:None
access type : public

'''

@app.get("/home")
def about_page():

    return {"message":"about_page"}