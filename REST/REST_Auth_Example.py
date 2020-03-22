import os
import getpass
import requests                                                                       #Python requests library to do http get request
from requests.auth import HTTPBasicAuth
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning                                  #This is to ignore SSL Certificates for unsecured sites

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)            #This is to ignore SSL Certificates for unsecured sites


if __name__ == "__main__":                                                             #Enter main part of the code

    username = "derahul9@gmail.com"
    password = getpass.getpass()                                                       #Getpass only works from terminal as pycharm and getpass have a different terminal window
    url = f"https://api.github.com/user"
    http_headers = {"accept": "Accept: application/vnd.github.v3+json"}                #Read the documentation to understand how to generate these values

    response = requests.get(url, headers=http_headers, auth=HTTPBasicAuth(username, password), verify=False)                   #verify false is to not verify SSL certificate
    response = response.json()

    print()
    pprint(response)
    print()