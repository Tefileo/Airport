class Flight():

    def __init__(self, flight_number,origin,destination,date_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.date_time = date_time
        self.list_of_passengers = []

    def flight_list(self):
        return self.flight_number + ' ' + self. origin+ ' '  + self.destination + ' '  + self.date_time

    def add_a_passenger(self, passenger, flight):
        self.list_of_passengers = passenger + ' ' + flight
