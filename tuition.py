#Name: Elijah, Michael

import datetime
###

RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.5
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.9
IN_RATE = RATE_TUITION_IN + RATE_INSTITUTION_FEE + RATE_ACTIVITY_FEE
OUT_RATE = RATE_TUITION_OUT + RATE_CAPITAL_FEE + RATE_INSTITUTION_FEE + RATE_ACTIVITY_FEE

###

inout = 1
numcredits = 0
scholarshipamt = 0
totalcost = 0
balance = 0
tuitionamt = 0
capitalamt = 0
instamt = 0
activityamt = 0

####

def main():
    more = True
    while more:
        get_data()
        calc()
        show_results()
        reset()
        yesno = input( "\n Would you like to calculate for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more = False
            

def get_data():
    global inout, numcredits, scholarshipamt 
    inout = int(input("Enter a 1 for IN-STATE, enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = int(input("Scholarship amount recieved: "))

def calc():
    global inout, numcredits, scholarshipamt, totalcost, balance, tuitionamt, capitalamt, instamt, activityamt  
    instamt=numcredits*RATE_INSTITUTION_FEE
    activityamt=numcredits*RATE_ACTIVITY_FEE
    if inout==1:
        totalcost=numcredits*IN_RATE 
        tuitionamt=numcredits*RATE_TUITION_IN
    else:
        totalcost=numcredits*OUT_RATE 
        capitalamt=numcredits*RATE_CAPITAL_FEE
        tuitionamt=numcredits*RATE_TUITION_OUT
    balance=totalcost-scholarshipamt #works
    
def show_results():
    moneyf = '8.2f'
    if inout==1:
        print("                      ")
        print('-----------------------------------')
        print('           PVCC Reciept            ')
        print('-----------------------------------')
        print('Institution Fee  +$ ' + format(instamt, moneyf))
        print('Activity Fee     +$ ' + format(activityamt, moneyf))
        print('Tuition Amount   +$ ' + format(tuitionamt, moneyf))
        print('Total             $ ' + format(totalcost, moneyf))
        print('Scholarship      -$ ' + format(scholarshipamt, moneyf))
        print('Balance           $ ' + format(balance, moneyf))
        print('-----------------------------------')
        print(str(datetime.datetime.now()))
    else:
        print("                      ")
        print('-----------------------------------')
        print('           PVCC Reciept            ')
        print('-----------------------------------')
        print('In State Fee     +$ ' + format(instamt, moneyf))
        print('Capital Fee      +$ ' + format(capitalamt, moneyf))
        print('Activity Fee     +$ ' + format(activityamt, moneyf))
        print('Tuition Amount   +$ ' + format(tuitionamt, moneyf))
        print('Total             $ ' + format(totalcost, moneyf))
        print('Scholarship      -$ ' + format(scholarshipamt, moneyf))
        print('Balance           $ ' + format(balance, moneyf))
        print('-----------------------------------')
        print(str(datetime.datetime.now()))
        
def reset():
    inout = 1
    numcredits = 0
    scholarshipamt = 0
    totalcost = 0
    balance = 0
    tuitionamt = 0
    capitalamt = 0
    instamt = 0
    activityamt = 0

main()
            
        
        
        
