import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ''
        self.states = []
    
    def write(self, string):
        self.content += string
    
    def save(self):
        if len(self.states) == 4:
            self.states.pop(0)
        self.states.append(Memento(self.file, self.content))
        return Memento(self.file, self.content)
    
    def undo(self, memento, index):
        if index <= len(self.states) and index != 0:
            memento = self.states[len(self.states)-index-1]
        self.file = memento.file
        self.content = memento.content

class FileWriterCaretaker:

    def save(self, writer):
        self.obj = writer.save()

    def undo(self, writer, ind):
        writer.undo(self.obj, ind)

if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()
    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n")
    caretaker.save(writer)
    
    print("Se graba información adicional y se salva")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n")
    caretaker.save(writer)
    
    print("Se graba información adicional 2 y se salva")
    writer.write("Material adicional N° 2 de la clase de patrones\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional 3 y se salva")
    writer.write("Material adicional N° 3 de la clase de patrones\n")
    print(writer.content + "\n")
    caretaker.save(writer)

    print("Se graba información adicional 4")
    writer.write("Material adicional N° 4 de la clase de patrones\n")
    print(writer.content + "\n")

    print("se invoca al <undo> con argumento '0'")
    caretaker.undo(writer, 0)
    print("Se muestra el estado actual")
    print(writer.content + "\n")

    print("se invoca al <undo> con argumento '1'")
    caretaker.undo(writer, 1)
    print("Se muestra el estado actual")
    print(writer.content + "\n")

    print("se invoca al <undo> con argumento '2'")
    caretaker.undo(writer, 2)
    print("Se muestra el estado actual")
    print(writer.content + "\n")

    print("se invoca al <undo> con argumento '3'")
    caretaker.undo(writer, 3)
    print("Se muestra el estado actual")
    print(writer.content + "\n")
