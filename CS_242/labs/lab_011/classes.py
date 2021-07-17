from LinkedList.LinkedList import LinkedList
from LinkedList.LinkedListIterator import LinkedListIterator
from datetime import datetime


class Product(object):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __str__(self):
        return str(self.name)

    def getName(self):
        return self.name


class Asset(object):
    def __init__(self, product: Product, unitOfMeasure: str, count: int) -> None:
        super().__init__()
        self.eventLog = []
        self.product = product
        self.unitOfMeasure = unitOfMeasure
        self.count = count

    def __str__(self):
        return f"{self.count} {self.unitOfMeasure} {self.product}"

    def getCount(self):
        return self.count

    def getUnitOfMeasure(self):
        return self.unitOfMeasure

    def getProduct(self):
        return self.product

    def updateEventLog(self, event):
        self.eventLog.append(event)

    def getEventLog(self):
        return self.eventLog


class Event(object):
    def __init__(self, type: str) -> None:
        super().__init__()
        self.type = type

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.time_of_log = current_time

    def __str__(self):
        return f"{self.type : self.time_of_log}"

    def getTimeOfLog(self):
        return self.time_of_log

    def getType(self):
        return self.type


class Batch(LinkedList):
    def __init__(self, assets) -> None:
        self.eventLog = []
        super().__init__(assets)
        self.list_iterator = LinkedListIterator(self)
        self.list_iterator.first()

    def updateEventLog(self, event: Event, assetIndex: int = None):
        ''' pass in position of asset to be updated. If position is  not defined, update entire batch event log'''

        self.list_iterator.first()

        eventTuple = (event.getType(), event.getTimeOfLog())

        while self.list_iterator.hasNext():
            theNode = self.list_iterator.next()
            pos = self.list_iterator.getPosition()
            if(assetIndex <= pos):
                theNode.updateEventLog(eventTuple)

    def getEventLog(self):
        event_log_collection = []
        for node in self:
            event_log_collection.append(node.getEventLog())

        return event_log_collection


aProduct = Product("foo")
aPallet = Asset(aProduct, "pallet", 2)
aCase = Asset(aProduct, "case", aPallet.getCount() * 2)
aItem = Asset(aProduct, "item", aCase.getCount()*2)

theBatch = Batch([aPallet, aCase, aItem])
li = LinkedListIterator(theBatch)

e = Event("Lost")
f = Event("Arrived at Location")

theBatch.updateEventLog(e, 2)

theBatch.getEventLog()
