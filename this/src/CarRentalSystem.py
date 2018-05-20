from .Booking  import Booking, BookingError
from .Location import Location
from .Customer import User, Customer
from .Car      import Car, SmallCar
from datetime import datetime
import pytest

class CarRentalSystem:
    def __init__(self):
        self._cars = []
        self._customers = []
        self._bookings = []

    def car_search(self, name=None, model=None):
        #  pass
        if name is None and model is None:
            return self._cars
        cars = []

        for car in self._cars:
            c_name = car.get_name()
            c_model = car.get_model()
            if name is not None and name.lower() in c_name.lower():
                cars.append(car)
            elif model is not None and model.lower() in c_model.lower():
                cars.append(car)
        return cars
        
    def make_booking(self, customer, period, car, location):
        
        if (location.pickup == ""):
            raise BookingError("start_location", "Specify a valid start location")
        if (location.dropoff == ""):
            raise BookingError("end_location", "Specify a valid end location")

        new_booking = Booking(customer, period, car, location)
        self._bookings.append(new_booking)
        car.add_booking(new_booking)
        return new_booking
    
   
    def check_booking_period(self, form_start_date, form_end_date):
        if (form_start_date == ""):
            raise BookingError("form_start_date", "Specify a valid start date")
        if (form_end_date == ""):
            raise BookingError("form_end_date", "Specify a valid end date")

        date_format = "%Y-%m-%d"
        start_date = datetime.strptime(form_start_date, date_format) 
        end_date = datetime.strptime(form_end_date, date_format)     
        diff = end_date - start_date 
        period = diff.days

        if (period < 0): 
            raise BookingError("period", "Specify a valid booking period") 
        return period
        
    def get_customer(self, username):
        """
        Just returns the first customer, should do a search but not
        needed for this use case. Will break if no customers in list
        """
        return self._customers[0]

    def add_car(self, car):
        self._cars.append(car)

    def new_customer(self, customer):
        self._customers.append(customer)

    def validate_login(self, username, password):
        for c in self._customers:
            if c.username == username and c.validate_password(password):
                return c
        return None

    def get_user_by_id(self, user_id):
        for c in self._customers:
            if c.get_id() == user_id:
                return c
        return None

    @property
    def cars(self):
        return self._cars

    def get_car(self, rego):
        for c in self._cars:
            if c.get_rego() == rego:
                return c
        return None