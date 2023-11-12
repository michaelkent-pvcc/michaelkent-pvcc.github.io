#Name: Michael Kent

import datetime
###
BORD=30
DAPP=35
INFLU=48
LEPT=21
LYME=41
RABIES=25
DOGFULLPACK=(BORD+DAPP+INFLU+LEPT+LYME+RABIES)*.85
LEUK=35
RHINO=30
FRABIES=25
CATFULLPACK=(RHINO+LEUK+FRABIES)*.90
HRTSML= 9.99
HRTMED= 11.99
HRTLRG= 13.99
HRTCAT= 8


###
pet_name = "Pet"
dog = False
pet_weight = 0
vactotal = 0
discount= False
chewtotal=0
total=0
bordT = False
dappT = False
influT = False
leptT = False
lymeT = False
rabiesT = False
leukT = False
rhinoT = False
frabiesT = False




####

def main():
    more = True
    while more:
        get_data()
        calc()
        show_results()
        reset()
        yesno = str(input( "\nWould you like to purchase for another pet? (Y/N): "))
        if yesno.upper() == "n":
            more = False
            

def get_data():
    global pet_name, dog, pet_weight
    vacT=False
    chewT=False
    pet_name = str(input("Name of your pet: "))
    catxdogQ = str(input("Is "+pet_name+" a cat or dog?: "))
    if catxdogQ in ['c', 'C', 'cat', 'Cat', 'CAT']:
        dog= False
    elif catxdogQ in ['d', 'D', 'dog', 'Dog', 'DOG']:
        dog= True
    else:
        print("Incorrect input. Please try again.\n")
        get_data()
    vac = str(input("Would you like to view the vaccines we offer? (Y/N): "))
    if vac in ['y', 'Y']:
        vacT=True
        vaccinesurvey()
    chew = str(input("Would you like to view our Anti-Heartworm Chewables? (Y/N): "))
    if chew in ['y', 'Y']:
        chewT=True
        chewsurvey()
    if chewT==False and vacT==False:
        print("Please select an option to view.\n")
        get_data()

        

    
def vaccinesurvey():
    global vactotal, bordT, dappT, influT, leptT, lymeT, rabiesT, leukT, rhinoT, rabiesT
    moneyf = '8.2f'
    if dog==True:
        print('-----------------------------------')
        print('         Available Vaccines        ')
        print('-----------------------------------')
        print('Bordatella        $ ' + format(BORD, moneyf))
        print('DAPP              $ ' + format(DAPP, moneyf))
        print('Influenza         $ ' + format(INFLU, moneyf))
        print('Leptospirosis     $ ' + format(LEPT, moneyf))
        print('Lyme Disease      $ ' + format(LYME, moneyf))
        print('Rabies            $ ' + format(RABIES, moneyf))
        print('-----------------------------------')
        print('         Special Discount!         ')
        print('              15% OFF              ')
        print(' Upon the purchase of all vaccines ')
        print('-----------------------------------')
        print('Please indicate which vaccines you\nwould like to purchase (Y/N):\n')
        bordT = False
        bordQ = input("Bordatella Vaccine: ")
        if bordQ in ['y', 'Y']:
            vactotal= vactotal+BORD
            bordT=True
        dappT = False
        dappQ = input("DAPP Vaccine: ")
        if dappQ in ['y', 'Y']:
            vactotal= vactotal+DAPP
            dappT = True
        influT = False
        influQ = input("Influenza Vaccine: ")
        if influQ in ['y', 'Y']:
            vactotal= vactotal+INFLU
            influT = True
        leptT = False
        leptQ = input("Leptospirosis Vaccine: ")
        if leptQ in ['y', 'Y']:
            vactotal= vactotal+LEPT
            leptT = True
        lymeT = False
        lymeQ = input("Lyme Disease Vaccine: ")
        if lymeQ in ['y', 'Y']:
            vactotal= vactotal+LYME
            lymeT = True
        rabiesT = False
        rabiesQ = input("Rabies Vaccine: ")
        if rabiesQ in ['y', 'Y']:
            vactotal= vactotal+RABIES
            rabiesT = True
        if rabiesT and lymeT and leptT and influT and dappT and bordT:
            print("15% discount applied!")
            vactotal= DOGFULLPACK
            discount= True
    else:
        print('-----------------------------------')
        print('         Available Vaccines        ')
        print('-----------------------------------')
        print('Feline Leukemia    $ ' + format(LEUK, moneyf))
        print('Rhinotracheitis    $ ' + format(RHINO, moneyf))
        print('Rabies             $ ' + format(FRABIES, moneyf))
        print('-----------------------------------')
        print('         Special Discount!         ')
        print('              10% OFF              ')
        print(' Upon the purchase of all vaccines ')
        print('-----------------------------------')
        print('Please indicate which vaccines you\nwould like to purchase (Y/N):\n')
        leukQ = input("Feline Leukemia Vaccine: ")
        if leukQ in ['y', 'Y']:
            vactotal= vactotal+LEUK
            leukT=True
        rhinoQ = input("Rhinotracheitis Vaccine: ")
        if rhinoQ in ['y', 'Y']:
            vactotal= vactotal+RHINO
            rhinoT = True
        frabiesQ = input("Rabies Vaccine: ")
        if frabiesQ in ['y', 'Y']:
            vactotal= vactotal+FRABIES
            frabiesT = True
        if leukT==True and rhinoT==True and frabiesT==True:
            print("10% discount applied!")
            vactotal= CATFULLPACK
            discount= True


def chewsurvey():
    global chewtotal
    if dog:
        pet_weight = int(input("How much does "+pet_name+" weigh?: "))
        if pet_weight < 26:
            chewp = HRTSML
        elif pet_weight <51:
            chewp = HRTMED
        else:
            chewp = HRTLRG
        chewQ = str(input("\nIt is recommended for "+pet_name+" to take a chewable every month.\nWould you like to purchase a chewable subscription for $"+str(chewp)+"/month? (Y/N): "))
        if chewQ in ['y', 'Y']:
            chewtotal= chewp
    else:
        chewQ = str(input("\nIt is recommended for "+pet_name+" to take a chewable every month.\nWould you like to purchase a chewable subscription for $"+str(HRTCAT)+"/month? (Y/N): "))
        if chewQ in ['y', 'Y']:
            chewtotal= HRTCAT

            

def calc():
    global total
    total=chewtotal+vactotal
    
def show_results():
    moneyf = '5.2f'
    print(CATFULLPACK)
    print(DOGFULLPACK)
    print(discount)
    print(frabiesT)
    print(rhinoT)
    print(        '-------------------------------------')
    print(        '             Pet Reciept             ')
    print(        '-------------------------------------')
    if bordT==True:
        print(    'Bordatella Vaccine      $ ' + format(BORD, moneyf))
    if dappT==True:
        print(    'DAPP Vaccine            $ ' + format(DAPP, moneyf))
    if influT==True:
        print(    'Influenza Vaccine       $ ' + format(INFLU, moneyf))
    if leptT==True:
        print(    'Leptospirosis Vaccine   $ ' + format(LEPT, moneyf))
    if lymeT==True:
        print(    'Lyme Disease Vaccine    $ ' + format(LYME, moneyf))
    if rabiesT==True:
        print(    'Rabies Vaccine          $ ' + format(RABIES, moneyf))
    if leukT==True:
        print(    'Feline Leukemia Vaccine $ ' + format(LEUK, moneyf))
    if rhinoT==True:
        print(    'Rhinotracheitis Vaccine $ ' + format(RHINO, moneyf))
    if frabiesT==True:
        print(    'Feline Rabies Vaccine   $ ' + format(FRABIES, moneyf))
    if discount==True:
        if dog==True:
            print('         -15% OFF VACCINES-          ')
        if dog==False:
            print('         -10% OFF VACCINES-          ')
    if chewtotal>0:
        print(    '-------------------------------------')
        print(    'Chewables Subscription  $ ' + format(chewtotal, moneyf)+"/month")
    print(        '-------------------------------------')
    print(        'Due now:                $ '+  format(total, moneyf))
    print(        '-------------------------------------')
    print(str(datetime.datetime.now()))

def reset():
    global vactotal, bordT, dappT, influT, leptT, lymeT, rabiesT, leukT, rhinoT, rabiesT, pet_name, dog, pet_weight, vactotal, discount, chewtotal, total
    pet_name = "Pet"
    dog = False
    pet_weight = 0
    vactotal = 0
    discount= False
    chewtotal=0
    total=0
    bordT = False
    dappT = False
    influT = False
    leptT = False
    lymeT = False
    rabiesT = False
    leukT = False
    rhinoT = False
    frabiesT = False
main()
            
        
        
        
