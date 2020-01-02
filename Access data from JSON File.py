import json
jasonSTR = '{"cuentaUsuarios": 2,"usuarios":[{"nombre": "Mario","online": true},{"nombre": "Jesus","online": false}]}'
jasonDecod = json.loads(jasonSTR)
print(jasonDecod)
print(jasonDecod["cuentaUsuarios"])
usuarios = jasonDecod["usuarios"]
print(usuarios)
usuario0 = usuarios[0]
usuario1 = usuarios[1]
print(usuario0)
print(usuario1)
print(usuario0["nombre"])
print(usuario0["online"])
print(jasonDecod["usuarios"][1]["nombre"])
print(jasonDecod["usuarios"][1]["online"])
for usuario in usuarios:
print(str( usuario["nombre"]) +", "+ str(usuario["online"]))
