from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/", summary="Главный эндпоинт")
def main_func():
    return {'data': 'Syasstroy'}


@app.get('/users', summary='Данные от пользователя')
def func_num(a: int, b: int):
    return a + b



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)