from flask import Flask, request

app = Flask(__name__)

doces = [
    {"receita": "Bolo", "items":
        [
            {"sabor": "Chocolate", "preco": 19.99}
        ]
    },
     {"receita": "Rocambole", "items":
        [
            {"sabor": "Goiabada", "preco": 24.99}
        ]
    }
    ]

@app.get("/doces")
def get_doces():
    return {"doces": doces}

@app.get("/doces/<string:receita>")
def get_doces_by_receita(receita):
    for doce in doces:
        if doce["receita"] == receita:
            return doce
    return {"message": "doces not found"}, 404

@app.get("/doces/<string:receita>/item/")
def get_item_in_doces(receita):
    for doce in doces:
        if doce["receita"] == receita:
            return {"items": doce["items"]}
    return {"message": "doces not found"}, 404

@app.post("/doces")
def create_doces():
    request_data = request.get_json() #pega o conteudo do body
    new_doces = {"receita": request_data["receita"], "items": []}
    doces.append(new_doces) #insere o payload na doces
    return new_doces, 201

@app.post("/doces/<string:receita>/item")
def create_item(receita):
    request_data = request.get_json()
    for doce in doces:
        if doce["receita"] == receita:
            new_item = {"sabor": request_data["sabor"], "preco": request_data["preco"]}
            doce["items"].append(new_item)
            return new_item, 201
    return {"message": "receita nao encontrado "}, 404


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)