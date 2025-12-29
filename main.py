from fastapi import FastAPI
import uvicorn

from users.views import router as users_router

app = FastAPI()
app.include_router(users_router)


@app.get("/", summary="Главный эндпоинт")
def main_func():
    return "Syasstroy"


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)