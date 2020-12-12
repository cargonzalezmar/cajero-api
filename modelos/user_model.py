from pydantic import BaseModel

#El modelo no es la tabla sino una forma de encapsular la información. Ppor eso, basandonos en las tablas
# tendremos un modelo de datos que será abstracción de los datos que tenemos en user_db
#Elementos de entrada para que el ingrese al sistema

#Para el ingreso del usuario solo nos interesa username y password
class UserIn(BaseModel):
    username: str
    password: str

#Elementos de salida. Solo nos interesa username y balance
class UserOut(BaseModel):
    username: str
    balance: int

#De todo lo que hay en la tabla hacemos un SELECT y nos traemos unas columnas específicas que son las 
#únicas que me interesan. A pesar de ser clases solo le definicimos atributos. En este caso no se hace procesamiento
#Solo necesitamos los objetos para que encapsulen la informacion pero no desarrollen ninguna tarea adicional. por eso no hay
#constructor ni metodos

#El BaseModel se usa para que asuma que cada uno es un modelo mas del modelo de datos total 
#para conectar asume que es un modelo mas para procesar
#hace las conexiones entre cosas y se usa para validadciones internas 