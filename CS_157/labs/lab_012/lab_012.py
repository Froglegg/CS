import pickle

from flights import *

from datetime import datetime


def standTime(militaryTime):
    # Datetime library formats explained:
    # %H - Hour (24-hour fomrat)
    # %M - Minute
    # %I - Hour (12-hour format)
    # %p - AM or PM
    time = datetime.strptime(str(militaryTime), '%H%M').strftime('%I:%M %p')
    return time


def main():
    fl = pickle.load(open("target.p", "rb"))

    response = "Y"

    while (response == "Y" or response == "y"):

        answer = input("How would you like to sort the available flights?"
                       "\n1) Date"
                       "\n2) Destination"
                       "\n3) Cost"
                       "\n4) Airline"
                       "\n5) Time\n"
                       )

        if (answer == "1"):
            d = input("Please enter a date (MM/DD)\n")
            match = False
            for i in range(len(fl)):
                if (d == fl[i].date):
                    match = True
                    print(
                        fl[i].date, standTime(fl[i].time),
                        fl[i].destination, "$", "%.2f" % fl[i].cost, fl[i].airline)
            if (match == False):
                print("No matches found")

        elif (answer == "2"):
            dest = input("Please enter a US airport code\n")
            for i in range(len(fl)):
                if (dest == fl[i].destination):
                    print(
                        fl[i].date, standTime(fl[i].time),
                        fl[i].destination, "$", "%.2f" % fl[i].cost, fl[i].airline)

        elif (answer == "3"):
            c = float(input("Please enter a cost in US dollars\n"))
            for i in range(len(fl)):
                if (c >= fl[i].cost):
                    print(
                        fl[i].date, standTime(fl[i].time),
                        fl[i].destination, "$", "%.2f" % fl[i].cost, fl[i].airline)

        elif (answer == "4"):
            airline = input("Please enter an Airline\n")
            for i in range(len(fl)):
                if (airline == fl[i].airline):
                    print(
                        fl[i].date, standTime(fl[i].time),
                        fl[i].destination, "$", "%.2f" % fl[i].cost, fl[i].airline)

        elif (answer == "5"):
            time = (
                input("Please enter a time (Standard US format, e.g., 12:00 PM)\n"))
            for i in range(len(fl)):
                if (time == standTime(fl[i].time)):
                    print(
                        fl[i].date, standTime(fl[i].time),
                        fl[i].destination, "$", "%.2f" % fl[i].cost, fl[i].airline)
        else:
            print("------------------------------------\n"
                  "Invalid Response. Please try again."
                  "\n------------------------------------")

        response = input("Would you like to go again (Y/N)? ")


main()
