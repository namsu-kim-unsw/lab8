from src.CarRentalSystem import CarRentalSystem
from src.Location import Location
from src.Customer import Customer
from src.Car import Car, SmallCar
from src.Booking import BookingError
import pytest

# Tests for function "CarRentalSystem.make_booking()"
system = CarRentalSystem()

customer            = Customer("username", "password", "license")
empty_start_date    = ""
empty_end_date      = ""
car                 = SmallCar("name", "model", "rego")
location_no_pickup  = Location("", "dropoff")
location_no_dropoff = Location("pickup", "")
location            = Location("pickup", "dropoff")

def test_empty_input_1():
    with pytest.raises(BookingError) as err: 
        system.check_booking_period(empty_start_date, "2018-05-15")
    
def test_empty_input_2():
    with pytest.raises(BookingError) as err: 
        system.check_booking_period("2018-05-15", empty_end_date)

def test_empty_input_3():
    with pytest.raises(BookingError) as err: 
        system.make_booking(customer, 5, car, location_no_pickup)
    
def test_empty_input_4():
    with pytest.raises(BookingError) as err: 
        system.make_booking(customer, 5, car, location_no_dropoff)

def test_impossible_dates():
    with pytest.raises(BookingError) as err: 
        system.check_booking_period("2018-05-15", "2018-05-10")
    
def test_incorrectly_formatted_date():
    with pytest.raises(ValueError) as err:
        system.check_booking_period("2018-05-", "2018-05-10")

