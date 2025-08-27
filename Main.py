from fastapi import FastAPI

app = FastAPI()

# MENSAGEM PRINCIPAL AO ACESSAR O IP DA APLICAÇÃO 127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World"}

# PARA ACESSAR ESTA MENSAGEM O ENDEREÇO É -> 127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": "deu certo"}


