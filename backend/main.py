#
#       CREATED BY MAXIM SHESTAKOV: LYMOOS
#     

from fastapi import FastAPI
from core.router import router

app = FastAPI()

@app.on_event("startup")
async def root():
    return {"connection": "START WORKING!"}
    #запуск базы данных, да и всеё системы впринципе

app.include_router(router,prefix='/api')


