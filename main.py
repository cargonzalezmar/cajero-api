#Aca es donde pondremos la logica de la fastAPI
#Importaremos todo lo de los otros archivos

from db.user_db import UserInDB
from db.user_db import update_user, get_user

from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction

from modelos.user_model import UserIn, UserOut
from modelos.transaction_model import TransactionIn, TransactionOut

import datetime
from fastapi import FastAPI #Con esta le decimos a lo que estamos creando que es una aplicacion de fastapi
from fastapi import HTTPException #Esta se utiliza para lanzar los errores

api=FastAPI() #Con esta linea creamos una api-rest (creamos la aplicacion)

#Vamos a importar las operaciones
@api.post("/user/auth/") #Para asociar la funcion a un servicio web usamos el deocrador @api."METODO HTTP" +
                         # con la url  que usara el usuario para acceder al servicio web "/user/auth/". Luego
                         # Esa URL con ese metodo entrara a la funcion que estaremos por definir
async def auth_user(user_in: UserIn):#asincrono: a penas llega la peticion lo pone a correr y es sincronico. 
                                     #Hasta que no termina uno no inicial la siguiente.
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado":False}
    return {"Autenticado":True}

@api.get("/user/balance/{username}")
async def get_balance(username:str):
    user_in_db=get_user(username)
    if user_in_db==None:
        raise HTTPException(status_code=404,detail="El usuario no existe")
    user_out=UserOut(**user_in_db.dict())
    return user_out

@api.put("/user/transaction/")
async def make_transaction(transaction_in: TransactionIn):
    user_in_db = get_user(transaction_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in_db.balance < transaction_in.value:
        raise HTTPException(status_code=400, detail="Sin fondos suficientes")

    user_in_db.balance = user_in_db.balance - transaction_in.value
    update_user(user_in_db)
    
    transaction_in_db = TransactionInDB(**transaction_in.dict(),actual_balance = user_in_db.balance)
    transaction_in_db = save_transaction(transaction_in_db)
    transaction_out = TransactionOut(**transaction_in_db.dict())
    return transaction_out