from starlette.types import Receive
from fastapi import FastAPI
from pydantic import BaseModel
from auth import login,signup,hash_password,isuser_exist,send_msg,get_all_msg,get_all_users,create_user
from fastapi.middleware.cors import CORSMiddleware

class logina(BaseModel):
    username : str
    password : str
class signupa(BaseModel):
    username : str
    password :  str

class msg_a(BaseModel):
    sender : str
    reciever : str
    msg :str 
class get_mag(BaseModel):
    sender : str
    reciever : str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
def login_api(data:logina):
    username = data.username
    password = data.password
    return login(username,password)
@app.post("/signup")
def signup_api(data:signupa):
    username = data.username
    password = data.password
    return signup(username,password)

@app.get("/get_msg")
def get_all_msg_api(sender:str , reciever:str):
    return get_all_msg(sender,reciever)

@app.post("/send_msg")
def send_msg_api(data:msg_a):
    sender = data.sender
    reciever = data.reciever
    msg = data.msg
    return send_msg(sender,reciever,msg)    



@app.get("/get_all_users")
def get_all_users_api():
    return get_all_users()



