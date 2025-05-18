'''
Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways.

'''
from random import randint
class train:
    def __init__(self,trainno):
        self.trainno=trainno
    def book(self,fro,to):
        print(f"Ticket is booked in train no:{self.trainno} from {fro} to {to}")
    def getstatus(self):
        print(f"Train no:{self.trainno} is running on time")
    def getfare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainno}from {fro} to {to} is {randint(222,5555)}")

t=train(15713)
t.book("Katihar ","Patna")
t.getstatus()
t.getfare("Katihar ","Patna")