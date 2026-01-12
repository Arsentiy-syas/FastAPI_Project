import os
from dotenv import load_dotenv
import jwt
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone


load_dotenv()


private_key = os.getenv('PRIVATE_KEY')
public_key = os.getenv('PUBLIC_KEY')
algorithm = os.getenv('ALGORITHM')


password_hash = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, private_key, algorithm=algorithm)


