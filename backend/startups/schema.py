from pydantic import BaseModel

class StartUp_Create(BaseModel):
    name:str
    #Придумать схему и всё что должно быть

class StartUp(StartUp_Create):
    name:str
    #Придумать схему и всё что должно быть

class StartUp_Delete(BaseModel):
    id:int
    #Придумать схему и всё что должно быть