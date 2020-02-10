from Air_Craft import Air_craft
from Buildings import Buildings
from Employers import Employers
from Flight import Flight
from Helicopter import Helicopter
from Passengers import Passengers
from People import People
from Plane import Plane
from Runways import Runways
from Terminals import Terminals

passengers = ['Passengers:']
airplane = []
flights = []


# As a check-in assistant, i want to be able to register passengers. Acceptance Criteria: Must be initialised with a name and passport.

passengers_class = Passengers('Jack1', 'B10000001')

passengers.append(passengers_class.name)
passengers.append(passengers_class.passport)

passengers_class = Passengers('Jack2', 'B10000002')
passengers.append(passengers_class.name)
passengers.append(passengers_class.passport)

passengers_class = Passengers('Jack3', 'B10000003')
passengers.append(passengers_class.name)
passengers.append(passengers_class.passport)

passengers_class = Passengers('Jack4', 'B10000004')
passengers.append(passengers_class.name)
passengers.append(passengers_class.passport)

passengers_class = Passengers('Jack5', 'B10000005')
passengers.append(passengers_class.name)
passengers.append(passengers_class.passport)

passengers_class = Passengers('Jack6', 'B10000006')
passengers.append(passengers_class.name)
passengers.append(passengers_class.passport)



# As a checking-assistant, i want to be able to list all flights.

flight_class = Flight('1111','London', 'Jamacia', '17/02/2020')
flights.append(flight_class.flight_list())

flight_class = Flight('1112','Jamaica', 'Brazil', '17/02/2020')
flights.append(flight_class.flight_list())

flight_class = Flight('1113','Brazil', 'Uganda', '17/02/2020')
flights.append(flight_class.flight_list())

# for flight in flights:
#     print(flight)

# As a check-in assistant, i want to be able to add a passenger to a flight.

flight_class.add_a_passenger('Jack1', '1111')
airplane.append(flight_class.list_of_passengers)
flight_class.add_a_passenger('Jack2', '1112')
airplane.append(flight_class.list_of_passengers)
flight_class.add_a_passenger('Jack3', '1113')
airplane.append(flight_class.list_of_passengers)
flight_class.add_a_passenger('Jack4', '1111')
airplane.append(flight_class.list_of_passengers)
flight_class.add_a_passenger('Jack5', '1112')
airplane.append(flight_class.list_of_passengers)
flight_class.add_a_passenger('Jack6', '1113')
airplane.append(flight_class.list_of_passengers)


# List all the passengers on a flight

flight_to_check = flights[0]

print(flight_to_check)
for x in range(0,len(airplane)):
    if int(airplane[x][-4:]) == int(flight_to_check[:5]):
        print(airplane[x])


