##
## apility.py -- Interfacing with the Apility.io API
##

from .exonerator import HTTPGET
import requests, json

def sendRequestWithAuthToken(url):
    token = open("apility-api-key.txt", "r").readline()
    token = token[:len(token) - 1] # Cut off the newline
    headers = {'Accept': 'application/json', 'X-Auth-Token': token}
    response = requests.get(url, headers=headers)
    return response

def ipIsInBlacklist(ip):
    apiResponse = sendRequestWithAuthToken("https://api.apility.net/badip/" + ip)

    # apility returns 200 if the IP was found in a blacklist, plus some json
    # describing which blacklist it was found in
    return (apiResponse.status_code == 200, apiResponse.text)

def ipGeoLocation(ip):
    apiResponse = sendRequestWithAuthToken("https://api.apility.net/geoip/" + ip)

    apiResponseJSON = json.loads(apiResponse.text)

    distilledGeoInfo = {}
    try:
        distilledGeoInfo["country"] = apiResponseJSON["ip"]["country_names"]["en"]
        distilledGeoInfo["continent"] = apiResponseJSON["ip"]["continent_names"]["en"]
        distilledGeoInfo["latitude"] = apiResponseJSON["ip"]["latitude"]
        distilledGeoInfo["longitude"] = apiResponseJSON["ip"]["longitude"]

        return distilledGeoInfo
    except:
        return None

if __name__=="__main__":
    ipIsInBlacklist("86.59.21.38")
    ipIsInBlacklist("8.8.8.8")

    ipGeoLocation("86.59.21.38")
    ipGeoLocation("8.8.8.8")
