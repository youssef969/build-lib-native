import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth



class Firebase:
    
    const = {"apiKey": "AIzaSyDp60qdDnLVaST16cyeHBuETmIcTIOTqVc",
        "authDomain": "ai-elderly-care-system.firebaseapp.com",
        "projectId": "ai-elderly-care-system",
        "storageBucket": "ai-elderly-care-system.firebasestorage.app",
        "messagingSenderId": "100061616391",
        "appId": "1:100061616391:web:5d25c56f626d97822e8da2",
        
        }
    
    cred = credentials.Certificate(r"D:\Python\Flet - Cross Platform\hala\assets\files\ai-elderly-care-system-firebase-adminsdk-ltmp7-76550f1e25.json")
    firebase =firebase_admin.initialize_app(cred,{"databaseURL": "https://ai-elderly-care-system-default-rtdb.firebaseio.com/"})
    db = db.reference("/")

    


    @staticmethod
    def Number_of_users():
        users = Firebase.db.get()
        users_count = len(users) if users else 0
        return users_count -1
    
       
    @staticmethod
    def Add_user(Elder_name:str,Elder_age:str,Elder_email:str,Elder_ph:str,res_name:str,res_email:str,res_ph:str,password:str):
        elderly_user_movment = ["1"]
        elderly_user = {
            "name": Elder_name,
            "age": Elder_age,
            "contact": Elder_email,
            "ph_number": Elder_ph,
            }
        
        responsible_user = {
            "name": res_name,
            "contact": res_email,
            "ph_number":res_ph,
            "password": password
            }
        
        Firebase.Signup(res_email,password,Elder_ph)
        users = Firebase.Number_of_users()
        Firebase.db.child(f"{ users + 1}").child("responsible_user_id").set(responsible_user)
        Firebase.db.child(f"{users + 1}").child("elderly_user_movment").set(elderly_user_movment)
        Firebase.db.child(f"{ users + 1}").child("old_user_id").set(elderly_user)


    @staticmethod
    def Signup(email:str,Password:str,phone):
        auth.create_user(email=email,password=Password ,phone_number = phone)

    
    @staticmethod
    def Login (email:str,phone_number:str):
        try:
            auth.get_user_by_phone_number(phone_number)
            auth.get_user_by_email(email)    
        except: 
            print("aha")

    @staticmethod
    def update_movments(user_id):
        Firebase.db.child(f"{user_id}").child("elderly_user_movment").set(["1","2","3","4"])

    @staticmethod
    def get_Elder_data(user_id:int):
        person = Firebase.db.child(f"{user_id}").child("old_user_id").get() 
        return list(person.values())

    @staticmethod 
    def get_responsible_data(user_id:int):
        person = Firebase.db.child(f"{user_id}").child("responsible_user_id").get()
        return list(person.values())


     
    
    @staticmethod
    def save_user_id(user_id:str):
        state = {"user_id": user_id}
        with open(r"D:\Python\Flet - Cross Platform\alderly\assets\files\user_id.json", "w+") as f:
            json.dump(state, f)
       
       
         
    @staticmethod
    def load_user_id():
            with open(r"D:\Python\Flet - Cross Platform\alderly\assets\files\user_id.json","r") as f:
                state = json.load(f)
                return state["user_id"]
            

# Firebase.Add_user("youssef","18","awadallayossef@gmail.com","+201096923909","haamda","gggg@gmail.com","+201065668088","123467")
# Firebase.Login("gggg@gmail.com","123467")
# print(type(Firebase.load_user_id()))
# print(Firebase.Number_of_users())


