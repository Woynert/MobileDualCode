
#Clases
class Topic():
	name = ""
	itemList = []

	def __init__(self, name = "", itemList = []):
		self.name = name
		self.itemList = itemList

class Item():
	name = ""
	desc = ""

	def __init__(self, name = "", desc = ""):
		self.name = name
		self.desc = desc

#Espacio de Tabla
def addSpace(max, txt):
	rtxt = ""
	for _k in range(0, max-len(txt)):
		rtxt += " "
	return(rtxt)

#Imprimir Items
def imprimirItems(topicId):

	_topic = topicList[topicId]
	print("\n === ITEMS DE " + _topic.name + " === ")
	titles = ["ID", "NOMBRE", "DESCRIPCION"]
	txt = ""

	#Print titles
	for item in titles:
		txt += item
		txt += addSpace(10, item)
	print(txt)
	txt = ""

	#Print content
	for i in range(0, len(_topic.itemList)):
		txt = ""
		#Id
		item = str(i)
		txt += item + addSpace(10, item)

		#Name
		item = _topic.itemList[i].name
		txt += item + addSpace(10, item)

		#Descripcion
		item = _topic.itemList[i].desc
		txt += item + addSpace(10, item)
		print(txt)


#Imprimir lista
def imprimirTopicos():

	print("\n === TOPICOS === ")
	titles = ["ID", "NOMBRE", "ITEMS"]
	txt = ""

	#Print titles
	for item in titles:
		txt += item
		txt += addSpace(13, item)
	print(txt)
	txt = ""

	#Print content
	for i in range(0, len(topicList)):
		txt = ""
		#Id
		item = str(i)
		txt += item + addSpace(13, item)

		#Name
		item = topicList[i].name
		txt += item + addSpace(13, item)

		#Items
		item = str(len(topicList[i].itemList))
		txt += item + addSpace(13, item)
		print(txt)

#Menus
def menuTopic():
	printBlank()
	imprimirTopicos()

	print("\n --- Opciones --- ")
	print("1. Agregar topico")
	print("2. Eliminar topico")
	print("3. Renombrar topico")
	print("4. Abrir topico")

	ent = int(input("-> "))

	printBlank()
	if (ent == 1):
		print("\n --- Agregar Topico --- ")
		_name = input("Nombre: ")

		#Agregar
		topicList.append(Topic(name = _name))
	elif (ent == 2):
		print("\n --- Eliminar Topico --- ")
		imprimirTopicos() #Mostrar
		_id = int(input("Id: "))

		#Eliminar
		topicList.pop(_id)

	elif (ent == 3):
		print("\n --- Renombrar Topico --- ")
		imprimirTopicos() #Mostrar
		_id = int(input("Id: "))

		#Seleccionar ID
		_newname = input("Nuevo nombre: ")
		topicList[_id].name = _newname

	elif (ent == 4):
		print("\n --- Abrir Topico --- ")
		imprimirTopicos() #Mostrar
		_id = int(input("Id: "))

		#Abrir
		global topicSelID
		topicSelID = _id
		menuItems()

	menuTopic()

def menuItems():

	goback = False

	printBlank()
	imprimirItems(topicSelID)

	print("\n --- Opciones --- ")
	print("1. Agregar item")
	print("2. Eliminar item")
	print("3. Renombrar item")
	print("4. Editar descripcion")
	print("5. Salir de topico " + topicList[topicSelID].name)

	ent = int(input("-> "))

	printBlank()
	if (ent == 1):
		
		print("\n --- Agregar Item --- ")
		imprimirItems(topicSelID) #Mostrar
		_name = input("Nombre: ")
		_desc = input("Descripción: ")

		#Agregar
		topicList[topicSelID].itemList.append(Item(name = _name, desc = _desc))

	elif (ent == 2):
		print("\n --- Eliminar Item --- ")
		imprimirItems(topicSelID) #Mostrar
		_id = int(input("Id: "))

		#Eliminar
		topicList[topicSelID].itemList.pop(_id)

	elif (ent == 3):
		print("\n --- Renombrar Item --- ")
		imprimirItems(topicSelID) #Mostrar
		_id = int(input("Id: "))

		#Seleccionar ID
		_newname = input("Nuevo nombre: ")
		topicList[topicSelID].itemList[_id].name = _newname

	elif (ent == 4):
		print("\n --- Editar Descripcion --- ")
		imprimirItems(topicSelID) #Mostrar
		_id = int(input("Id: "))

		#Seleccionar ID
		_newdesc = input("Nueva Descripción: ")
		topicList[topicSelID].itemList[_id].desc = _newdesc

	elif (ent == 5): #Regresar
		goback = True

	if (not goback):
		menuItems()

def printBlank():
	for l in range(0, 100):
		print("\n")

#Variables
topicSelID = 0
topicList = []

_itemList = []
_itemList.append(Item(name = "Hola", desc = "Esto es una descripcion"))
_itemList.append(Item(name = "Hola2", desc = "Esto es una descripcion2"))
_topic = Topic(name = "Minecraft", itemList = _itemList)

topicList.append(_topic)

#Iniciar
#print(topicList[0].itemList)
#imprimirTopicos()
#imprimirItems(topicList[0])
menuTopic()
#Menus



