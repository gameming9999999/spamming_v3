#import os, sys, time
#from time import sleep as timeout
#python 2.7.15
#korn Hodsusnayworld
import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()        
print ""
print "\033[37;1m             reply Y  only once "
A = raw_input("you want to go back SPAM SMS? (Y/n) :  ")
if A == "Y" or A == "y":

  os.system("python2 a.py")

  
elif A == "N" or A == "n":

  os.system("python2 ch4")




elif A == "5" or A == "05":

    os.system("python spamsms5")

  
elif A == "0" or A == "00":
    sys.exit()
    
else:
     print ""
     print ""
     print "     \033[37;1m[\033[31m!\033[37;1m]\033[31m incorrect"
     timeout(5)
     restart_program()

     
 
