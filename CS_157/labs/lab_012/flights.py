import pickle

# class file name: flights.py


class flights(object):
    """ description of class """

    flightCount = 0

    def __init__(self, date, time, destination, cost, airline=None):

        self.date = date
        self.time = time
        self.destination = destination
        self.cost = cost
        self.airline = airline

        flights.flightCount += 1

    """ end class description """

# class file includes these flights objects


myFlight = [
    flights("12/13", 1200, "SFO", 170.00, "United"),
    flights("12/13", 1500, "SAT", 220.00, "United"),
    flights("12/14", 1300, "JFK", 150.00, "Spirit"),
    flights("12/15", 1100, "LAX", 190.00, "Spirit"),
    flights("12/15", 1200, "JNU", 550.00, "Alaska"),
    flights("12/16", 800, "MSY", 320.00, "American"),
    flights("12/16", 1000, "CLE", 70.00, "JetBlue"),
    flights("12/17", 2000, "DFW", 320.00, "Spirit"),
    flights("12/18", 2200, "ATL", 200.00, "JetBlue"),
]

# save the data to a file
pickle.dump(myFlight, open("target.p", "wb"))
