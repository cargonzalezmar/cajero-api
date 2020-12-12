from pydantic import BaseModel
from datetime import datetime

#Sucede algo similar a lo de user_model. Solo tenemos dos valores que llegan (username y value)
#De la tabal de user_db se observa que el id y el date se asignan por lo cual con el unico que debemos
#hacer algo es con el balance. Este lo tendremos que aplicar en una capa de logica PERO aca no se implementara
#porque solo estamos en db y modelo

#Entrada: usuario y valor
class TransactionIn(BaseModel):
    username: str
    value: int

#Salida: estado actual que le queda al usuario de saldo en su cuenta. En el Out son los 5 campos asignados
# en el transactioon_db
class TransactionOut(BaseModel):
    id_transaction: int
    username: str
    date: datetime
    value: int
    actual_balance: int