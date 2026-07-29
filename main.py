from fastapi import FastAPI

app = FastAPI()

@app.get('/clientes')

def ola_mundo():
    return {'mensagem': 'Minha primeira API em FastAPI!'}

@app.get('/sobre')

def sobre():
    return {'mensagem': 'Página Sobre'}