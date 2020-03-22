import os
import requests                                                                       #Python requests library to do http get reques
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning                                  #This is to ignore SSL Certificates for unsecured sites

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)            #This is to ignore SSL Certificates for unsecured sites


if __name__ == "__main__":                                                             #Enter main part of the code

    token = "7e6fb173a7e9c60b3f1650b4c8158271727922f5"                                 #Read the documentation to understand how to generate token
    url = "https://api.github.com/user"
    http_headers = {"accept": "application/json; version=2.4;"}                        #Read the documentation to understand how to generate these values
    if token:
        http_headers["authorization"] = "Token {}".format(token)

    response = requests.get(url, headers=http_headers, verify=False)                  #verify false is to not verify SSL certificate
    response = response.json()

    print()
    pprint(response)
    print()