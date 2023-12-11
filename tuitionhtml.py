#Name: Michael Kent

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

outfile = 'tuition.html'

####

def main():
    open_outfile()
    more = True
    
    while more:
        get_data()
        calc()
        show_results()
        reset()
        yesno = input( "\n Would you like to calculate for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            more = False
            f.write('</body></html>')
            f.close()
            
def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Tuition Results </title>\n')
    f.write('<style> td{text-align: center} </style> </head>\n')
    f.write('<body style ="background-color: #ffffff; background-image: url(https://www.pvcc.edu/sites/default/files/2023-08/pvcc_hrz_color_notagline.png); color: #a20045;">\n')

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
    balance=totalcost-scholarshipamt 
    
def show_results():
    moneyf = '8.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "
    if inout==1:
        f.write('\n<table border="3"   style ="width:40%;background-color: #ffffff;  font-family: arial; margin: auto;text-align: center;">\n')            
        f.write(colsp + '\n')
        f.write('<h2>PVCC RECIEPT</h2></td></tr>')
        f.write(colsp + '\n')
        f.write('*** Tuition Calculations ***\n')
        
        f.write(tr + 'Institution Fee' + endtd + format(instamt, moneyf) + endtr)
        f.write(tr + 'Activity Fee' + endtd + format(activityamt, moneyf) + endtr)
        f.write(tr + 'Tuition Amount ' + endtd +  format(tuitionamt, moneyf)  + endtr)

        f.write(tr + 'Total' +  endtd + sp + endtd + format(totalcost, moneyf)  + endtr)     
        f.write(tr + 'Scholarship' + endtd + sp + endtd + format(scholarshipamt, moneyf) + endtr)
        f.write(tr + 'Balance' +     endtd + sp + endtd + format(balance, moneyf) + endtr)
        
        f.write(colsp + 'Date/Time: '+ day_time + endtr)
        f.write('</table><br />')
    else:
        f.write('\n<table border="3"   style ="width:40%;background-color: #ffffff;  font-family: arial; margin: auto;text-align: center;">\n')            
        f.write(colsp + '\n')
        f.write('<h2>PVCC RECIEPT</h2></td></tr>')
        f.write(colsp + '\n')
        f.write('*** Tuition Calculations ***\n')
        
        f.write(tr + 'Institution Fee' + endtd + format(instamt, moneyf) + endtr)
        f.write(tr + 'Capital Fee' + endtd + format(capitalamt, moneyf) + endtr)
        f.write(tr + 'Activity Fee' + endtd + format(activityamt, moneyf) + endtr)
        f.write(tr + 'Tuition Amount ' + endtd +  format(tuitionamt, moneyf)  + endtr)

        f.write(tr + 'Total' +  endtd + sp + endtd + format(totalcost, moneyf)  + endtr)     
        f.write(tr + 'Scholarship' + endtd + sp + endtd + format(scholarshipamt, moneyf) + endtr)
        f.write(tr + 'Balance' +     endtd + sp + endtd + format(balance, moneyf) + endtr)
        
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