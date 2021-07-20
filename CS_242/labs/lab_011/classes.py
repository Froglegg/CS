from LinkedList.LinkedList import LinkedList
from LinkedList.LinkedListIterator import LinkedListIterator
from datetime import datetime
from tabulate import tabulate


class Product(object):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __str__(self):
        return str(self.name)

    def getName(self):
        return self.name


class Event(object):
    def __init__(self, assetTag: str, type: str) -> None:
        super().__init__()
        self.type = type
        self.assetTag = assetTag

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.time_of_log = current_time

    def __str__(self):
        return f"{self.type} : {self.time_of_log}"

    def getTimeOfLog(self):
        return self.time_of_log

    def getEvent(self):
        return self.type

    def getAssetTag(self):
        return self.assetTag


class Asset(LinkedList):

    def __init__(self, product: Product, unitOfMeasure: str, assetChildren, tag: str) -> None:

        super().__init__(assetChildren)
        self.tag = tag
        self.assetChildren = assetChildren
        self.eventLog = [Event(tag, "origin")]
        self.product = product
        self.unitOfMeasure = unitOfMeasure

        self.list_iterator = LinkedListIterator(self)
        self.list_iterator.first()

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.time_created = current_time

    def __str__(self):
        return f"{self.unitOfMeasure} {self.product} {self.assetChildren}"

    def __updateEventLog(self, event: Event):
        self.eventLog.append(event)

    def getListIterator(self):
        return self.list_iterator

    def getTag(self):
        if self.tag:
            return str(self.tag)

    def getUnitOfMeasure(self):
        return self.unitOfMeasure

    def getProduct(self):
        return self.product

    def getEventLog(self):
        return self.eventLog

    def getTimeCreated(self):
        return self.time_created

    def updateEventLog(self, event: str):

        newEvent = Event(self.getTag(), event)

        self.__updateEventLog(newEvent)

        # reset cursor
        self.list_iterator.first()

        while self.list_iterator.hasNext():

            theNode = self.list_iterator.next()

            theNode.updateEventLog(event)

        # reset cursor
        self.list_iterator.first()

    def getAssetTable(self):
        data = []
        for i in self:
            data.append([i.tag, i.unitOfMeasure, ", ".join(
                [child.tag for child in i.assetChildren] if i.assetChildren else []), i.time_created, i.eventLog[len(i.eventLog)-1]])

        return tabulate(data, headers=[
            "Asset tag", "Unit of Measure", "Asset Children", "Time Created", "Last Event"], tablefmt="github", numalign="left")

    def getEventLogTable(self):
        eventLog = self.getEventLog()
        data = [(e.getAssetTag(), e.getEvent(), e.getTimeOfLog())
                for e in eventLog]
        data.sort(reverse=True)
        return tabulate(data, headers=["Asset", "Event", "Time of Log"], tablefmt="github", numalign="left")
