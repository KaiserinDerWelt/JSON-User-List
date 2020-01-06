
apikey = ‘********'
lenguaje = 'spa'
ligaPetición =
'https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?text={0}&language={1}&apikey={2}'
mensaje1 = "Comment here"
ligaPetición = ligaPetición.format(mensaje1,lenguaje,apikey)
print(ligaPetición)
jsonRespuesta= requests.get(ligaPetición).json()
print(jsonRespuesta["positive"])
print(jsonRespuesta["negative"])
print(jsonRespuesta["aggregate"]["sentiment"])
print(jsonRespuesta["aggregate"]["score"])
