#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#instructs the shell and points to the correct interpreter/location - #!/usr/bin/python2

#python modules (socket module handles data channels and functions for network related tasks such as server name conversion to IP)
#sys module
import subprocess
import socket
import sys
import datetime

#class is used to group together different data points and methods
#colour classes applied to output using specified variables
class portcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

#define a function called "interface" then call the function once created from within the code
#specify port scanner target and port range in format script[arg0] ip [arg1], start port [arg2], end port [arg3]
def interface():
        print
        print "="*65
        print portcolors.RED + " ︻╦╤─-- - RaILGuN+ v1.0 - Initialising Target Options - --─╦╤︻ " + portcolors.ENDC
        print "="*65
        print portcolors.OKBLUE + "             <ip-address> <start-port> <end-port>" + portcolors.ENDC
        print "="*65

#(\n) creates/print on newline
#take the command line argument 3 and 4 passed by the user from inside argv[2] and argv[3] 

#defining a function called menu
#startPort and endPort are pushed inside of an interger function using (int)
def menu():
        startPort = int(sys.argv[2])
        endPort = int(sys.argv[3])
        
        #print below options
        print "Select Scan Type..."
        print
        print "1): TCP Scan (FULL CONN)\n2): TCP Scan (TOP PORTS)"
        print
        #the variable menu selection is equal to raw_input allowing for a defined user input using the raw_input function
        menuselection = raw_input(" Enter Selection: ")
        print

        #"if statement" can test a condition if "1" is entered then continue with full tcpscan if not true check the second condition "elif" if none of these are true then execute the else statement and print "Invalid Option Entered"
        #if menuselection is == (equal two) 1 then carryout tcpscan else if equal to option 2 then carry out top ports scan else print "invalid Option" and exit
        if menuselection == "1":
                tcpscan(startPort, endPort)
        elif menuselection == "2":
                topports(startPort, endPort)
        #else statement to print invalid input
        else:
                print portcolors.BOLD + "Invalid Input Entered - Please Enter (1) or (2)" + portcolors.ENDC
                print
                sys.exit()

#start port and endport are a parameter arguments of our function tcpscan - parameter acts as a variable names for a passed in argument
def tcpscan(startPort, endPort):
        #Check what time the scan started
        t1 = datetime.datetime.now()

        #grab 3rd(2) adn 4th(3) argument startPort/endPort and convert to integers using int()

        #create an empty list to store ports
        portlist = []
        currentPort = startPort
        ip = sys.argv[1]

        #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) - use socket family (AF_INET) IPv4    and create stream socket (SOCK_STREAM = TCP Connections)
        #"while" loop is similar to if statement. It executes the code/block of statements inside if some condition is true 
        #"while" loop will continue to execute a block of statements over and over until a given statement is true
        #"if" loop inside of the while loop will run tcpscan and print open ports 
        while currentPort <= endPort:
                try:    #code blocks are formed with indentation, anything belonging to the if will be indented to the right.
                        if currentPort >= startPort and currentPort <= endPort: 
                                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                sock.connect((ip,currentPort))
                                print portcolors.OKGREEN + portcolors.BOLD + ("PORT %s is Op3n!"%(currentPort)) + portcolors.ENDC
                                portlist.append(currentPort)
                                sock.close()
                except:
                        #do nothing placeholder - move to next port
                        pass
        
                #count up one each time 1,2,3,4...during the while loop
                currentPort += 1

        #Check what time the scan started
        t2 = datetime.datetime.now()

        #Calculates the time difference, to see how long the scan took
        total = t2 - t1

        print "=" *65
        print
        #String substitution is for total, startPort and endPort using %s specifying what start and end port was specified. port list will display what open ports were found
        print portcolors.YELLOW + "Target IP: %s\nTotal Scan Duration: %s\nYour Start Port Was %s And Your End Port Was %s" % (ip, total, startPort, endPort) + portcolors.ENDC
        print
        print portcolors.OKGREEN + "%s Open Port(s)" %(portlist) + portcolors.ENDC
        print
        #Repeated sequence using (*)
        print "=" *65 

def topports(startPort, endPort):
        portList = [21,22,23,25,42,43,49,53,67,79,80,109,110,115,118,123,137,138,139,143,156,161,162,389,443,445,512,513,514,563,636,1433,3389,5900,2049]

        #check what time the scan started
        t1 = datetime.datetime.now()

        #create an empyty list
        found_openports = []
        ip = sys.argv[1]

        #for loops are used when you have a piece of code which you want to repeat a number of times/interate
        #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) - use socket family (AF_INET) IPv4 and create stream socket (SOCK_STREAM = TCP Connections)
        #for loop will loop through dictionary called portList containing specified ports
        #nested try: has to be within the for loop
        #assign portList to port

        for port in portList:
                try:
                        if port >= startPort and port <= endPort:
                                #for port loop connect if open, if closed goto except and print port closed
                                #creating variable as sock to be equal to (SOCK_STREAM)
                                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                #socket.connect specifies IP and target ports as specified in the for (port) eg. (sys argv = 10.129.121.10 and port = 514 etc.)
                                sock.connect((sys.argv[1],port))
                                print portcolors.OKGREEN + portcolors.BOLD + ("PORT %s is Op3n!"%(port)) + portcolors.ENDC
                                #appends open ports in the function port in portlist to list found_openports
                                found_openports.append(port)
                                sock.close()
                except:
                                print portcolors.RED + "PORT %s is Clos3d!"%port + portcolors.ENDC

        #check what time the scan started
        t2 = datetime.datetime.now()

        #calculates the time difference, to see how long the scan took
        total = t2 - t1

        print "=" *65
        print
        #string substitution is for total, port1, port2 using %s specifying what start and end port was specified
        print portcolors.YELLOW + "%s\nTotal Scan Duration: %s\nYour Start Port was %s And Your End Port was %s" % ('Target IP: ' + str(ip), total, startPort, endPort) + portcolors.ENDC
        print
        print portcolors.OKGREEN + "%s Open Port(s)" %(found_openports) + portcolors.ENDC
        print
        #repeated sequence using (*)
        print "=" *65

################################################################################
#each time command is run clear kali terminal
subprocess.call(['clear'])
interface()

#if argument length is less than 4 print error

#print len(sys.argv)
if len(sys.argv) == 4: 
        menu()

#call the function menu to implement menu if inputs are valid
else:
        print
        print portcolors.YELLOW + portcolors.BOLD + "Invalid Input Arguments" + portcolors.ENDC
        print
        sys.exit()
################################################################################

#variable is a reference to a object
