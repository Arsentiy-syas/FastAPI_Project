from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from auth import router


app = FastAPI()

app.include_router(router.router_users)


@app.get('/')
async def main_func():
    return {'description of site': 'Добро пожаловать в Сясьстрой!'}


@app.get("/marker_cafe")
async def geo_func():
    return [
        {'title': 'Кафе Встреча', "latitude": 60.143394353972404, "longitude": 32.545669818104095, 'description': 'Уютное придорожное кафе, расположенное на трассе "Кола". В меню представленны различные кухни'},
        {'title': 'Кафе Зеркальное', "latitude": 60.141564579383044, "longitude": 32.55577638167218, 'description': 'Кафе рассчитано на проведение различного рода банкетов'},
        {'title': 'Кафе Камелот', "latitude": 60.140943500595974, "longitude": 32.558760723749025, 'description': 'Одно из самых пафосных мест в Сясьстрое'},
        {'title': 'Кафе Берлога', "latitude": 60.13610724750983, "longitude": 32.52006981219947, 'description': 'Самое пафосное место в Сясьстрое, расположенное на берегу реки Сясь'},
        {'title': 'Кафе Панда', "latitude": 60.1454967596958, "longitude": 32.55358649575883, 'description': 'Маленькое семейное кафе со вкусными ролами и сушами'},
        {'title': 'Кафе Берлога', "latitude": 60.13656738781703, "longitude": 32.56764702575829, 'description': 'Новый бар, не успевший получить характеристику'},
    ]

origins = [
    'http://localhost:3000',
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