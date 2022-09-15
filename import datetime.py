import datetime

class BikeRental:
    def __init__(self, stock=0):
        self.stock = stock
    
    def displaystock(self):
        print("We have currently {} bikes available for rent in the shop.")
        return self.stock

    def rentbikehourly(self, n):
        if n<=0:
            print("Number of bikes should be positive.")
            return None
        elif n>self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now=datetime.datetime.now()
            print("You have rented {} bike(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $7 for each hour per bike.")
            print("Enjoy!")

            self.stock -=n
            return now

    def rentbikedaily(self, n):
        if n<=0:
            print("Number of bikes should be positive.")
            return None
        elif n>self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now=datetime.datetime.now()
            print("You have rented {} bike(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $15 for each hour per bike.")
            print("Enjoy!")

            self.stock -=n
            return now

    def rentbikeweekly(self, n):
        if n<= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now=datetime.datetime.now()
            print("You have rented {} bike(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $45 for each hour per bike.")
            print("Enjoy!")

            self.stock -=n
            return now
    
    

    def returnbike(self, request):
        rentaltime, rentalbasis, numberofbikes = request
        bill = 0

        if rentaltime and rentalbasis and numberofbikes:
            self.stock += numberofbikes
            now=datetime.datetime.now()
            rentalperiod=now - rentaltime

            if rentalbasis == 1:
                bill = round(rentalperiod.seconds / 3600) * 5 * numberofbikes

            elif rentalbasis == 2:
                bill = round(rentalperiod.days) * 20 * numberofbikes

            elif rentalbasis == 3:
                bill=round(rentalperiod.days / 7) * 60 * numberofbikes

            if (3<=numberofbikes<=5):
                print("You are eligible for family rental promotion of 30% discount")
                bill=bill*0.7

            print("Thanks for returning your bike.")
            print("The cost is ${}".format(bill))
            return bill

        else:
            print("Are you sure you rented a bike with us?")
            return None


class Customer:

    def __init__(self):
        self.bikes=0
        self.rentalbasis=0
        self.rentaltime=0
        self.bill=0

    def requestbike(self):
        bikes=input("How many bikes would you like to rent?")
        try:
            bikes=int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if bikes<1:
            print("Invalid input.\nNumber of bikes should be grater than zero!")
            return -1
        else:
            self.bikes=bikes
            return self.bikes
    
    def returnbike(self):
        if self.rentalbasis and self.rentaltime and self.bikes:
            return self.rentaltime, self.rentalbasis, self.bikes
        else:
            return 0,0,0