#Name: Michael Kent
#Purpose: Find the price of visitng the movies
import datetime

#Global Variables
TAX_RATE=.055
TICKET_PRICE=10.99
POPCORN_PRICE=12.99
DRINK_PRICE=4.99
subtotal=0
numtickets=0
numpop=0
tickettotal=0
popcorntotal=0
total=0
taxval=0

#Functions
def main():
    
    ordermore=True
    while ordermore:
        userinput()
        calc()
        useroutput()
        
        askinput=input("\nWould you like to order again? (Y/N): ")
        if askinput.upper()=="N" or askinput=="n":
            ordermore=False
            print("Thank you for your order! Come back soon!")


def userinput():
    global numtickets, numpop
    numtickets=int(input("Number of tickets: "))
    numpop=int(input("Buckets of popcorn: "))

def calc():
    global subtotal, total, taxval, tickettotal, popcorntotal
    tickettotal=TICKET_PRICE*numtickets
    popcorntotal=POPCORN_PRICE*numpop
    subtotal=tickettotal+popcorntotal
    taxval=subtotal*TAX_RATE
    total=subtotal+taxval

def useroutput():
    line="----------------------------"
    priceformat='6,.2f'
    print(line)
    print("****** MOVIE  TICKETS ******")
    print("** Your local movie house **")
    print(line)
    print(str(numtickets)+"x Popcorn        $ "+format(popcorntotal,priceformat))
    print(str(numpop)+"x Tickets        $ "+format(tickettotal,priceformat))
    print(line)
    print("Subtotal           $ "+format(subtotal,priceformat))
    print("Sales Tax          $ "+format(taxval,priceformat))
    print("Total              $ "+format(total,priceformat))
    print(line)
    print(str(datetime.datetime.now()))

#Execution
main()
