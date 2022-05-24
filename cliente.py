import requests

id = input("Digite o id: ")
imagem = input("Digite o url da imagem: ")
titulo = input("Digite o titulo do item: ")
quantidade = input("Digite a quantidade do item: ")
descricao = input("Digite a descrição do item: ")


dados = {"id": id, "imagem": imagem, "titulo": titulo,
         "quantidade": quantidade, "descricao": descricao}

x = requests.post("http://localhost:5000/estoque", json=dados)

if x.status_code != 200:
    print(f"[{x.status_code}] {x.text}")
else:
    print(x.text)
