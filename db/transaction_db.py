from datetime import datetime
from pydantic import BaseModel
             
#Creamos clase con 5 atributos. La fecha tiene la hora actual de cuando se hace la transacción. Es con la info del SERVIDOR
# Tiene valores por defecto (0 en el id o fecha). LA CLASE SE USA PARA MAPEAR LA TABLA. Se usa para hacer empalme entre código y tabla de base de datos
# Por eso en fastAPI se necesita una clase por cada tabla que se tenga
class TransactionInDB(BaseModel):
    id_transaction: int = 0
    username: str
    date: datetime = datetime.now()
    value: int
    actual_balance: int

database_transactions = []

#El generador es un diccionario porque tiene clave valor
generator = {"id":0}

#Esta funcion permite guardar la transacción que hace el usuario en una base de datos
def save_transaction(transaction_in_db: TransactionInDB):
    generator["id"] = generator["id"] + 1
    transaction_in_db.id_transaction = generator["id"]
    database_transactions.append(transaction_in_db)
    return transaction_in_db