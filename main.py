from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from auth import router


app = FastAPI()

app.include_router(router.router_users)



@app.get("/", summary="Главный эндпоинт")
def main_func():
    return {'data': 'Syasstroy'}


origins = [
    'http://localhost:3000',
    'http://127.0.0.1:8000',
    'http://localhost:8001',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)