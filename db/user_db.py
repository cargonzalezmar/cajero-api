from typing import Dict #De la librería typing tomamos el método Dict. Si viene de la librería typing es porque tiene tipo de datos asociado
from pydantic import BaseModel #Este sirve para utilizar el modelo base que es el código que usaremos como si fuera la base de datos 
                               #(mapeo de información)

#Definicion de la base de datos con 3 atributos
class UserInDB(BaseModel): #Generamos una clase que se llama UserInDB y tiene como argumento la info del modelo que está en el método BaseModel
    
    #La clase crea 3 atributos y se le da a cada una el tipo de datos
    username: str
    password: str
    balance: int

#Esto es parte del archivo pero no parte de la clase
database_users = Dict[str, UserInDB] #Un diccionario que tiene una entrada string y hereda elementos de la clase UserInDB de forma que pueda
                                     #usar los 3 atributos que hay en UserInDB

#Crea los datos que se ingresan a la base de datos (para este caso 2 atributos). Los asteriscos son propios de la librería (palabras reservadas de validación)
#Creamos un diccionario donde se agregan un par de registros a la db (inicializan la base de datos)
database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",
                            "password":"root",
                            "balance":12000}),
    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "balance":34000}),
}

#Acá agregamos dos funciones. get_user tiene de atributo de entrada un username que es un string. Retorna la info del usuario
def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
        
#Este metodo permite usar la info de UserInDB y va a validar que esté ahi para entregar la info del mismo usuario
#Recibe un objeto con 3 tipos de datos 
#Para crear un usuario nuevo o actualzar
def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db