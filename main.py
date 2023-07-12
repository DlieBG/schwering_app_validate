from fastapi import FastAPI, Header, HTTPException
from dotenv import load_dotenv, find_dotenv
import jwt, os

app = FastAPI()

load_dotenv(find_dotenv())

@app.get('/')
def validate(authorization: str = Header()):
    jwt_string = ''

    try:
        jwt_string = authorization.split('Bearer ')[1]
    except:
        raise HTTPException(400)
    
    jwt_body = {}

    try:
        jwt_body = jwt.decode(authorization.split(' ')[1], os.getenv('JWT_SECRET'), algorithms=["HS256"])
    except:
        raise HTTPException(401)

    return jwt_body
