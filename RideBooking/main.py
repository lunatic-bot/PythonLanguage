from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role():
        pass

class Ride:
    def __init__(self, origin, destination, fare):
        self.origin = origin
        self.destination = destination
        self.fare = fare
        self._available = True  ## Protected


    def book(self):
        if self._available:
            self._available = False
            return True
        return False
    
    def cancle(self):
        self._available = True
        return True
    
    def __str__(self):
        return f"Ride from {self.origin} to {self.destination} is ({'Availabe' if self._available else 'Not available'})"
    

class Passenger(User):
    def get_role(self):
        return "Passenger"
    
class Driver(User):
    def get_role(self):
        return "Driver"
    

class RideManager:
    def __init__(self):
        self.rides = []

    def add_ride(self, ride):
        self.rides.append(ride)

    def show_rides(self):
        if not self.rides:
            print("No rides to show.")
        else:
            for ride in self.rides:
                print(ride)

    def __len__(self):
        return len(self.rides)
    
    def __contains__(self, destination):
        return any(ride.destination == destination for ride in self.rides)
    
    @staticmethod
    def is_location_valid(origin, destination):
        return bool(origin.strip()) and bool(destination.strip()) ## non empty
    
    @classmethod
    def from_ridelist(cls, ride_list):
        rm = cls()
        for ride in ride_list:
            rm.add_ride(ride)

        return rm

    

if __name__ == "__main__":
    # pass

    r1 = Ride("BookStore", "Station", "$50")
    r2 = Ride("Airport", "Beach", "$20")
    r3 = Ride("Mall", "Airport", "$20")
    rides_list = [r1, r2, r3]

    rm2 = RideManager.from_ridelist(rides_list)
    rm2.show_rides()
    print("Total rides in rm2:", len(rm2)) 


    # rm = RideManager()
    # rm.add_ride(r1)
    # rm.add_ride(r2)
    # rm.add_ride(r3)
    # print(RideManager.is_location_valid("Airport", "Downtown"))  # True
    # print(RideManager.is_location_valid(""))          # False


    ##############################################################################


    # r1 = Ride("BookStore", "Station", "$50")
    # r2 = Ride("Airport", "Beach", "$20")
    # r3 = Ride("Mall", "Airport", "$20")

    # rm = RideManager()
    # rm.add_ride(r1)
    # rm.add_ride(r2)
    # rm.add_ride(r3)

    # rm.show_rides()

    # # Test __len__ magic method
    # print("Total rides:", len(rm))  # 2

    # # Test __contains__ magic method
    # print("Airport in rides?", "Airport" in rm)  # True
    # print("Beach in rides?", "Beach" in rm)      # False




    ###############################################################################

    # r1 = Ride("Point A", "Point B", "$50")
    # r2 = Ride("Point A", "Point B", "$50")

    # p1 = Passenger("Alice")
    # d1 = Driver("Bob")
    # print(p1.get_role())
    # print(d1.get_role())

    # # Test that abstract class cannot be instantiated
    # try:
    #     u = User("Someone")  # Should raise TypeError
    # except TypeError as e:
    #     print(e)


    ################################################################
    ## class Ride
    # r1 = Ride("Point A", "Point B", "$50")
    # print(r1)
    # r1.book()
    # print(r1)
    # r1.cancle()
    # print(r1)


