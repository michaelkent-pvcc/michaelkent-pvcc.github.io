#Name: Michael Kent
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
            elif room_type =="DR":
                subtotal = ROOM_RATES[1] * num_nights
            else:
                subtotal = ROOM_RATES[2] * num_nights
                
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total     = subtotal + occupancy + salestax
             
            grandtotal += total
        
#STUDENTS: ADD THE REST OF THE append statements after this one       
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)



def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: center} </style> </head>\n')
    f.write('<body style ="background-color: #ffffff; background-image: url(https://i.pinimg.com/564x/d6/d4/9f/d6d49ffb61916b6684c1273051961448.jpg); color: #1baca2;">\n')
    
def create_output_html():
    global f
    
    moneyf="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "8">'

    f.write('\n<table border="3"   style ="width:40%;background-color: #ffffff;  font-family: arial; margin: auto;text-align: center;">\n')            
    f.write(colsp + '\n')
    f.write('<h2>Emerald Beach Hotel & Resort Ledger</h2></td></tr>')
    
    f.write(tr+'Last Name'+td+'First Name'+td+'Room Type'+td+'Num Nights'+td+'Subtotal'+td+'Sales Tax'+td+'Occupancy Tax'+td+'Total'+endtr)

    for i in range(len(guest)): #           first               room                nights                      subtotal                sales tax                            occ tax                         total
        f.write(tr+str(guest[i][0])+td+str(guest[i][1])+td+str(guest[i][2])+td+str(guest[i][3])+td+format(guest[i][4], moneyf)+td+format(guest[i][5], moneyf)+td+format(guest[i][6], moneyf)+td+format(guest[i][7], moneyf)+endtr)
    
    f.write('<tr><td colspan= "8" style ="text-align: right;">Grandtotal: '+ format(grandtotal, moneyf) + endtr)
    f.write('<tr><td colspan= "8" style ="text-align: right;">Report Date: '+ day_time + endtr)
    
    f.write('</table><br />')
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')

##call on main program to execute##
main()
