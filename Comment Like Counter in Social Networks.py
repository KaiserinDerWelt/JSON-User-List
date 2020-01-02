import facebook #Python library
import requests #Python library
token = “********" #Token from FB API Library
graph = facebook.GraphAPI(token)
cantidadComentarios = 26
PageId = '1415691342026378'
cuentaLikes = 0
cuetaPaginas = 0
cuentaComentarios = 0
ListaComents = []
bandera = False
coments = graph.get_connections(PageId, 'feed')
print(coments)
while True:
try:
for coment in coments['data']:
lstComent = []
try:
mensaje = coment['message']
except KeyError :
continue
cuentaLikes = 0
print(mensaje)
while(True):
try:
for like in coment['likes']['data']:
cuentaLikes = cuentaLikes + 1
coment['likes'] = requests.get(coment['likes']['paging']['next']).json()
except KeyError:
break
print(cuentaLikes)
lstComent.append(mensaje)
lstComent.append(cuentaLikes)
ListaComents.append(lstComent)
cuentaComentarios = cuentaComentarios + 1
print("")
if (cuentaComentarios >= cantidadComentarios):
bandera = True
break
if (bandera):
break
coments = requests.get(coments['paging']['next']).json()
except KeyError :
break
def ToCSV(lista):
cadena = ''
for linea in lista:
cuenta = 0
for stats in linea:
if (cuenta != 0):
cadena = cadena + ',' + str(stats)
else:
cadena = cadena + str(stats).replace(",", "").replace("\n", "")
cuenta += 1
cadena = cadena + '\r'
csv = open("C:\\Users\\Beto\\Desktop\\Comentarios.csv", "w+")
csv.write(cadena)
csv.close()
ToCSV(ListaComents)
print("")
print("Paginas Analizadas: " + str(cuetaPaginas))
