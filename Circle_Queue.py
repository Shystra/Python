class Nodo():
    def __init__(self, date):
        self.date = date
        self.next = None


class CircleQueue ():
    def __init__ (self):
        self.first = None
        self.last = None
    
    def Empty(self):
        return self.first == None
    
    def PlusFirst(self,date):
        if self.Empty():
            self.first = self.last = Nodo(date)
            self.last.next = self.first

        else:
            aux = Nodo(date)
            aux.next = self.first
            self.first = aux
            self.last.next = self.first
        

    def PlusLast(self, date):
        if self.Empty():
            self.first = self.last = Nodo(date)
            self.last.next = self.first

        else:
            aux = self.last
            self.last = aux.next = Nodo(date)
            self.last.next = self.first


    def Travel(self):
        aux = self.first
        while aux.next != self.first:
            print(aux.date)
            aux = aux.next
        print(aux.date)



list = CircleQueue()

list.PlusFirst(10)
list.PlusFirst(56)
list.PlusFirst(78)
list.PlusFirst(90)
list.PlusFirst(15)
list.PlusFirst(100)

list.Travel()