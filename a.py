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
os.system("clear")
os.system("sh logo")
print "\033[90m> \033[32;1mFacebook:\033[37;1m Naranan Leejaroen"
print "\033[90m> \033[32;1mYouTube :\033[37;1m Nothing YT"
print
print "         \033[37;1m[\033[32;1m01\033[37;1m]\033[36;1m Thai language (show phon) "  
print "         \033[37;1m[\033[32;1m02\033[37;1m]\033[36;1m English (show phon) "  

print "         \033[37;1m[\033[32;1m03\033[37;1m]\033[36;1m Thai language (no show phon) "  
print "         \033[37;1m[\033[32;1m04\033[37;1m]\033[36;1m English (no show phon) "  
print ""
print "         \033[37;1m[\033[32;1m05\033[37;1m]\033[36;1m Thai (special) "  
print "         \033[37;1m[\033[32;1m06\033[37;1m]\033[36;1m English (special) "  
print "         \033[37;1m[\033[32;1m66\033[37;1m]\033[36;1m Thai (special\033[31;1m!\033[36;1m) "  
print""
print " \033[37;1m[\033[31;1m00\033[37;1m] exit "
print "\033[36;1m"
A = raw_input("> choose : ")

if A == "1" or A == "01":

  os.system("python spamsms")

  
elif A == "2" or A == "02":

    os.system("python spamsms2")


elif A == "3" or A == "03":

    os.system("python spamsms3")


elif A == "4" or A == "04":

    os.system("python spamsms4")



elif A == "5" or A == "05":

    os.system("python spamsms5")


elif A == "55" or A == "55":

    os.system("python spam55")

elif A == "6" or A == "06":

    os.system("python spamsms6")



elif A == "66" or A == "66":

    os.system("python spam6.py")

  
  
elif A == "0" or A == "00":
    sys.exit()
    
else:
     print ""
     print ""
     print "     \033[37;1m[\033[31m!\033[37;1m]\033[31m Enter the correct number"
     timeout(5)
     restart_program()

     
 
