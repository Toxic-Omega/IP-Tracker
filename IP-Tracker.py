
import argparse
import requests, json
import sys
from sys import argv
import os


parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

print("""\033[31m
██╗██████╗               ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗              ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝    █████╗       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝     ╚════╝       ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║                      ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝                      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  \033[92mV.1.0
                                                                                  
                              \033[96mCoded By Toxic - Omega                                                 
""")


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[+]"
        print (a, "\033[31mVictim :", data['query'])
        print (a, "\033[31mISP :", data['isp'])
        print (a, "\033[31mOrganisation :", data['org'])
        print (a, "\033[31mCity :", data['city'])
        print (a, "\033[31mRegion :", data['region'])
        print (a, "\033[31mLongitude :", data['lon'])
        print (a, "\033[31mLatitude :", data['lat'])
        print (a, "\033[31mTime Zone :", data['timezone'])
        print (a, "\033[31mZip Code :", data['zip'])
        print ("\033[0m")

except KeyboardInterrupt:
        print ("Exiting...")
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print ("Please Chack Your Internet Connection!")
sys.exit(1)
