
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
def imprimirItems(topic):

	print("\n === ITEMS DE " + topic.name + " === ")
	titles = ["ID", "NOMBRE", "DESCRIPCION"]
	txt = ""

	#Print titles
	for item in titles:
		txt += item
		txt += addSpace(10, item)
	print(txt)
	txt = ""

	#Print content
	for i in range(0, len(topic.itemList)):
		txt = ""
		#Id
		item = str(i)
		txt += item + addSpace(10, item)

		#Name
		item = topic.itemList[i].name
		txt += item + addSpace(10, item)

		#Descripcion
		item = topic.itemList[i].desc
		txt += item + addSpace(10, item)
		print(txt)


#Imprimir lista
def imprimirTopicos():

	print("\n === TOPICOS === ")
	titles = ["ID", "NOMBRE"]
	txt = ""

	#Print titles
	for item in titles:
		txt += item
		txt += addSpace(10, item)
	print(txt)
	txt = ""

	#Print content
	for i in range(0, len(topicList)):
		txt = ""
		#Id
		item = str(i)
		txt += item + addSpace(10, item)

		#Name
		item = topicList[i].name
		txt += item + addSpace(10, item)
		print(txt)

#Menus
def menuTopic():
	printBlank()
	imprimirTopicos()

	print("\n --- Opciones --- ")
	print("1. Agregar topico")
	print("2. Eliminar topico")
	print("3. Renombrar topico")

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

	menuTopic()

def printBlank():
	for l in range(0, 100):
		print("\n")

#Variables
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



