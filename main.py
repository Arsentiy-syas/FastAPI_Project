from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/", summary="Главный эндпоинт")
def main_func():
    return "Syasstroy"


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)