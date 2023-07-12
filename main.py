from fastapi import FastAPI, Header, HTTPException
from dotenv import load_dotenv, find_dotenv
import jwt, os

app = FastAPI()

load_dotenv(find_dotenv())

@app.get('/')
def validate(authorization: str = Header()):
    try:
        jwt_string = authorization.split(' ')[1]
        print(jwt_string)
    
        try:
            jwt_body = jwt.decode(jwt_string, os.getenv('JWT_SECRET'), algorithms=["HS256"])
        except:
            raise HTTPException(401)

        return jwt_body
    except:
        raise HTTPException(400)
