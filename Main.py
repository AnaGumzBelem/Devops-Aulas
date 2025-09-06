from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

### modificacao-nomes-end-point

@app.get("/funcaoteste")

# PARA ACESSAR ESTA MENSAGEM O ENDEREÇO É -> 127.0.0.1:8000/teste
@app.get("/teste")
### main
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}


