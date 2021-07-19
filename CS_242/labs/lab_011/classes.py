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
    def __init__(self, asset: str, type: str) -> None:
        super().__init__()
        self.type = type
        self.asset = asset

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.time_of_log = current_time

    def __str__(self):
        return f"{self.type : self.time_of_log}"

    def getTimeOfLog(self):
        return self.time_of_log

    def getEvent(self):
        return self.type

    def getAsset(self):
        return self.asset


class Asset(LinkedList):

    def __init__(self, product: Product, unitOfMeasure: str, assetChildren, batchName: str = None) -> None:

        super().__init__(assetChildren)
        self.batchName = batchName
        self.assetChildren = assetChildren
        self.eventLog = []
        self.product = product
        self.unitOfMeasure = unitOfMeasure

        self.list_iterator = LinkedListIterator(self)
        self.list_iterator.first()

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.time_created = current_time

    def __str__(self):
        return f"{self.unitOfMeasure} {self.product} {self.assetChildren}"

    def getBatchName(self):
        if self.batchName:
            return str(self.batchName)

    def getUnitOfMeasure(self):
        return self.unitOfMeasure

    def getProduct(self):
        return self.product

    def updateEventLog(self, event: Event):
        self.eventLog.append(event)

    def getEventLog(self):
        return self.eventLog

    def updateEventLog(self, event: str):
        ''' pass in position of asset to be updated. If position is  not defined, update entire batch event log'''
        # reset cursor
        self.list_iterator.first()

        while self.list_iterator.hasNext():

            theNode = self.list_iterator.next()

            newEvent = Event(theNode.getUnitOfMeasure(), event)

            eventTuple = (newEvent.getAsset(),
                          newEvent.getEvent(), newEvent.getTimeOfLog())

            theNode.updateEventLog(eventTuple)

            if theNode.assetChildren:
                for child in theNode.assetChildren:
                    child.updateEventLog(eventTuple)

        # reset cursor
        self.list_iterator.first()

    def getEventLog(self):
        event_log_collection = []
        for node in self:
            event_log_collection.append(node.getEventLog())
        return event_log_collection

    def getListIterator(self):
        return self.list_iterator

    def getAssetTable(self):
        data = []
        for i in self:
            data.append([i.unitOfMeasure, i.product.name])

        return tabulate(data, headers=[
            "Unit of Measure", "Product"], tablefmt="github", numalign="left")

    def getEventLogTable(self):
        eventLog = self.getEventLog()
        data = []
        for i in eventLog:
            for j in i:
                data.append([j[0], j[1], j[2]])
        return tabulate(data, headers=["Asset", "Event", "Time of Log"])


# class Batch(LinkedList):
#     def __init__(self, assets: list[Asset], name: str) -> None:
#         self.name = name
#         self.eventLog = []
#         super().__init__(assets)
        # self.list_iterator = LinkedListIterator(self)
        # self.list_iterator.first()

        # now = datetime.now()
        # current_time = now.strftime("%H:%M:%S")
        # self.time_created = current_time

#     def getName(self):
#         return str(self.name)

#     def getTimeCreated(self):
#         return str(self.time_created)

    # def updateEventLog(self, event: str, assetIndex: int = None):
    #     ''' pass in position of asset to be updated. If position is  not defined, update entire batch event log'''
    #     # reset cursor
    #     self.list_iterator.first()

    #     while self.list_iterator.hasNext():

    #         theNode = self.list_iterator.next()

    #         pos = self.list_iterator.getPosition()

    #         if(assetIndex <= pos):

    #             newEvent = Event(theNode.getUnitOfMeasure(), event)

    #             eventTuple = (newEvent.getAsset(),
    #                           newEvent.getEvent(), newEvent.getTimeOfLog())

    #             theNode.updateEventLog(eventTuple)

    #     # reset cursor
    #     self.list_iterator.first()

#     def getEventLog(self):
#         event_log_collection = []
#         for node in self:
#             event_log_collection.append(node.getEventLog())
#         return event_log_collection

    # def getListIterator(self):
    #     return self.list_iterator

    # def getBatchTable(self):
    #     data = []
    #     for i in self:
    #         data.append([i.unitOfMeasure, i.product.name])

    #     return tabulate(data, headers=[
    #         "Unit of Measure", "Product"], tablefmt="github", numalign="left")
    # def getEventLogTable(self):
    #     eventLog = self.getEventLog()
    #     data = []
    #     for i in eventLog:
    #         for j in i:
    #             data.append([j[0], j[1], j[2]])
    #     return tabulate(data, headers=["Asset", "Event", "Time of Log"])
batch_name = "test"
product = Product("foo")

palletCount = 2

caseCount = 4

itemCount = 8

batch = Asset(product, "batch", [Asset(product, "pallet", [Asset(product, "case", [Asset(product, "item", None)
                                                                                   for item in range(itemCount)]) for case in range(caseCount)]) for pallet in range(palletCount)], batchName=batch_name)

li = batch.getListIterator()


def recurseAndPrintTables(li):
    asset: Asset = li.next()
    print("")
    print(asset.getAssetTable())
    li = asset.getListIterator()
    if li.hasNext():
        recurseAndPrintTables(li)


print(batch.getAssetTable())
print("")
recurseAndPrintTables(li)
# for i in palletList:
#     for child in i.assetChildren:
#         child = Asset()


# def buildTopology(assetChildren):

#     if len(assetChildren) > 0:
#         assetChildren = LinkedList(assetChildren)
#         buildTopology(assetChildren)

# base case is, no more asset children
# recursive case is, has asset children


# palletList = [pallet for i in range(pallet.getBatchCount())]
# caseList = [case for i in range(case.getBatchCount())]
# itemList = [item for i in range(item.getBatchCount())]
