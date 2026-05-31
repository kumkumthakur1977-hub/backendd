
from database import supabase
def hash_password(password : str):
    
    password = password.replace('a','#')
    password = password.replace('b','@')
    password = password.replace('c','%')
    password = password.replace('d','*')
    password = password.replace('e',')')
    password = password.replace('f','-')
    password = password.replace('g','/')
    password = password.replace('h','!')
    password = password.replace('i','(')
    
    return password

def isuser_exist(username):
    result = (
        supabase.table('users').select("*").eq("username",username).execute()

    )
    return len(result.data) > 0   
  
def create_user(username,passw):
    result = (
        supabase.table('users').insert({
            "username" : username,
            'password': hash_password(passw)
        }).execute()
    )
    return result.data

def get_all_users():
    result = (
        supabase.table('users').select("username").execute()
    )
    return result.data


def send_msg(sender,reciever,contant,):
    is_sender_exist = isuser_exist(sender)
    is_reciever_exist = isuser_exist(reciever)
    if is_sender_exist and is_reciever_exist:
        result = (
            supabase.table('messages')
            .insert({
                "sender" : sender,
                "receiver" : reciever,
                "message" : contant

            }).execute()
        )
        return result.data
    else:
        notfound = f"sender/reciever in found"
        return notfound
    


def get_all_msg(sender,reciever):
    result = (
        supabase
        .table('messages')
        .select("*")
        .or_(
            f"and(sender.eq.{sender},receiver.eq.{reciever}),"
            f"and(sender.eq.{reciever},receiver.eq.{sender})"
        )
        .order("created_at")
        .execute()

    )
    
    return result.data

def login(username, password):

    result = (
        supabase
        .table("users")
        .select("*")
        .eq("username", username)
        .execute()
    )

    if len(result.data) == 0:
        return {
            "success": False,
            "message": "User not found"
        }

    user = result.data[0]

    if user["password"] != hash_password(password):
        return {
            "success": False,
            "message": "Wrong password"
        }

    return {
        "success": True,
        "message": "Login successful",
        "user": {
            "username":{
                "username": user["username"],
                "id": user["id"]

            } 
        }
    }
def signup(username,password):
    iue = isuser_exist(username)
    if iue :
        return {
            "success": False,
            "message": "user already exist"
        }
    else:
        result = create_user(username,password)
        return {
            "success": True,
            "message": "User created successfully",
            "user": result
        }   
            
