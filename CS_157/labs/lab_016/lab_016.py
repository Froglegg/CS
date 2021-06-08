# Richard Hayes Crowley
# CSC_157_lab_016
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
import numpy as np


class UserOptionException(Exception):
    pass


class PeriodSelectionException(Exception):
    pass


class SalesPeriod:
    def __init__(self, period: str, location: str, start_date: DateTime, anticipated_units_sold: tuple[int, int], cd_vinyl_price: tuple[float, float], accumulated_units_sold: tuple[int, int] = (0, 0), end_date: DateTime = None):
        self.period = period
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.anticipated_units_sold = anticipated_units_sold
        self.cd_vinyl_price = cd_vinyl_price
        self.accumulated_units_sold = tuple(
            np.add(anticipated_units_sold, accumulated_units_sold))

    def get_period(self):
        return self.period

    def get_location(self):
        return self.location

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_anticipated_units_sold(self):
        return self.anticipated_units_sold

    def get_cd_vinyl_price(self):
        return self.cd_vinyl_price

    def get_accumulated_units_sold(self):
        return self.accumulated_units_sold

    def __str__(self):
        return f"\nPeriod: {self.period}\nStart Date: {self.start_date.strftime('%m-%d-%Y')}\nEnd Date: {self.end_date.strftime('%m-%d-%Y')}\nLocation: {self.location}\nAnticipated CDs and Vinyl sold this period (CDs, Vinyl): {str(self.anticipated_units_sold)}\nAccumulated sales up to this period (CDs / Vinyl): {str(self.accumulated_units_sold)}\nPrice (CDs, Vinyl): {str(self.cd_vinyl_price)}"


def addDays(date: DateTime, days: int):
    return date + TimeDelta(days)


def calculatePeriodSales():
    print("calc")


def main():
    global user_option, start_date
    exit_condition = True
    start_date = DateTime.today()

    #  instantiate sales period objects
    period1 = SalesPeriod(period="1", location="Front Store Entrance", start_date=start_date,
                          anticipated_units_sold=(25, 32), cd_vinyl_price=(17.00, 32.00), end_date=addDays(
                              start_date, 46))

    period2 = SalesPeriod(period="2", location="CD Racks", start_date=addDays(
        start_date, 46), anticipated_units_sold=(15, 19), cd_vinyl_price=(15.00, 36.00), accumulated_units_sold=period1.get_accumulated_units_sold(), end_date=addDays(
        start_date, 91))

    period3 = SalesPeriod(period="3", location="Bargain CD Music Bins", start_date=addDays(
        start_date, 91), anticipated_units_sold=(37, 46), cd_vinyl_price=(9.00, 21.00), accumulated_units_sold=period2.get_accumulated_units_sold(), end_date=addDays(
        start_date, 136))

    while True:
        try:
            user_option = input(
                f"\nPlease select an option from the following\n1. View entire timeline for new CD placement\n2. See info for specific period\n3. Calculate anticipated units sold for Period 4\n4. Exit program\n\rYour Choice: ").strip()
            if not user_option or user_option not in ["1", "2", "3", "4"]:
                raise UserOptionException
            if user_option == "1":
                [print(period) for period in [period1, period2, period3]]

            elif user_option == "2":
                global selection
                periods = (period1, period2, period3)
                while True:
                    try:
                        selection = input(
                            f"Which period would you like to select?\n{[period.get_period() for period in periods]}").strip()
                        if not selection or selection not in [period.get_period() for period in periods]:
                            raise PeriodSelectionException
                        break
                    except PeriodSelectionException:
                        print(
                            f"Please enter one of the following: {[period.get_period() for period in periods]}")

                print(periods[int(selection) - 1])

            elif user_option == "3":
                accumulated_sales_from_last_period = period3.get_accumulated_units_sold()
                predicted_cd_sales = int(
                    (period3.get_accumulated_units_sold()[0] / 3) * 1.1)
                predicted_vinyl_sales = int(
                    (period3.get_accumulated_units_sold()[1] / 3) * 1.1)

                print(
                    f"\nAccumulated sales from last period (CDs / Vinyl): {str(accumulated_sales_from_last_period)}\n\rPredicted CD sales for period 4: {str(predicted_cd_sales)}\nPredicted Vinyl sales for period 4: {str(predicted_vinyl_sales)}\n\rNOTE: Predicted sales are calculated by the average of the last three periods multiplied by a factor of 1.1")

            else:
                print("\nGoodbye!")
                break

        except UserOptionException:
            print("Please input 1, 2, 3, or 4.")


# if __name__ == "__main__" enables exports of functions from this file without firing off the main script.
if __name__ == "__main__":
    main()
