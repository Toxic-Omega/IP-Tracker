
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

print("""
IP-Tracker





""")


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        b = lgreen+bold+"[+]"
        print (a, "Victim :", data['query'])
        print (a, "ISP :", data['isp'])
        print (a, "Organisation :", data['org'])
        print (a, "City :", data['city'])
        print (a, "Region :", data['region'])
        print (a, "Longitude :", data['lon'])
        print (a, "Latitude :", data['lat'])
        print (a, "Time Zone :", data['timezone'])
        print (a, "Zip Code :", data['zip'])

except KeyboardInterrupt:
        print ("Exiting...")
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print ("Please Chack Your Internet Connection!")
sys.exit(1)
