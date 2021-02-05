# Written by: Brian Figg
# Graders note: Use your Own API key for google maps
from api_keys import google_maps_key
import requests
import os
import datetime as dt
import time
import json
import matplotlib.pyplot as plt
import pandas as pd


# Crime data files
CA_crime_filepath = "data/CA_State Crime_by_County.csv"
NY_Crime_Filepath = "data/NYPD_Shooting_Data.csv"
# population data files
LA_pop_filepath = "data/LA_population_total.csv"
NYC_pop_filepath = "data/NYC_Total_population.csv"

# Creates DataFrames
CACrime_df = pd.read_csv(CA_crime_filepath)
NYCrime_Df = pd.read_csv(NY_Crime_Filepath)


# Filters Data for Crimes across State by County in 2019
CACrime_2019 = CACrime_df[CACrime_df['Year'] == 2019]

# Filters Data for Crimes in LA by County in 2019
LACrime_2019 = CACrime_2019[CACrime_2019['County'] == "Los Angeles County"]

# Filters Data for Gun Crime in LA by County in 2019
LAGunCrime_2019 = LACrime_2019[["FROBact_sum", "FASSact_sum"]]

# Converts date occur_date to datetime format
NYCrime_Df['OCCUR_DATE'] = pd.to_datetime(NYCrime_Df['OCCUR_DATE']).dt.date

# filters NYC Crime by year 2019(note: since NYC Data is all shooting data it needs no conversion to gun crime only)
NYCrime_2019 = NYCrime_Df[pd.DatetimeIndex(NYCrime_Df['OCCUR_DATE']).year == 2019]

# totals all firearm involved robberies and assaults
LATotalGunCrimeperType = LAGunCrime_2019.sum()

# adds total robberies and assaults involving firearms to give yearly total gun crime incidents
LATotalGunCrime = LATotalGunCrimeperType.sum()

# counts all NYC shooting Data Slides(note:selects max quantity as IncidentID is inculded in count and thus represents size of data set)
NYCTotalGunCrime = max(NYCrime_2019.count())
# sets different cities geographical election for googles geographic requirements
BoiseID_coordinates = "43.6187102, -116.2146068"
NYCID_coordinates = "40.6943  -73.9249"
LAID_coordinates = "34.1139 -118.4068"
ChicID_coordinates = "41.8373 -87.6862"

# sets up Search terms
target_search = "Gun"
target_radius = 50000
target_type = "store"



# base url for resoponse to use
base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# preps multi page gmaps search
invalid_requests_found = 0
next_page = None
NYC_ALLDATA = []
LA_ALLDATA = []
# THANK GOD ZACK FOR ALL THIS. HE GETS AN ENTIRE COOKIE FACTORY. Runs multi page gmaps search
while True:

    la_params = \
        {
            "location": LAID_coordinates,
            "keyword": target_search,
            "radius": target_radius,
            "type": target_type,
            "key": google_maps_key
        }

    nyc_params = \
        {
        "location": NYCID_coordinates,
        "keyword": target_search,
        "radius": target_radius,
        "type": target_type,
        "key": google_maps_key
        }
    try:
        la_params['pagetoken'] = next_page
        nyc_params['pagetoken'] = next_page
        time.sleep(2)
        LA_response = requests.get(base_url, params=la_params).json()
        LA_ALLDATA.append(LA_response)

        NYC_response = requests.get(base_url, params=nyc_params).json()
        NYC_ALLDATA.append(NYC_response)
        # query_result = google_places.nearby_search(
        #     location={'lat':  , 'lng': event['longitude']},
        #     radius=event['radius'],
        #     pagetoken=query_result_next_page,
        #     request_count=request_count)
        # If there are additional result pages, lets get it on the next while step
        # print(NYC_response)
        if 'next_page_token' in NYC_response.keys():
            next_page = NYC_response['next_page_token']

        else:
            break
        if 'next_page_token' in LA_response.keys():
                next_page = LA_response['next_page_token']

        else:
            break

    except Exception as e:
            # If the key is over the query limit, try a new one
            # Sometimes the Places API doesn't create the next page
            # despite having a next_page_key and throws an INVALID_REQUEST.
            # We should just sleep for a bit and try again.
        if str(e).find('INVALID_REQUEST') != -1:
            # Maximum of 4 INVALID_REQUEST responses
            invalid_requests_found = invalid_requests_found + 1
            if invalid_requests_found > 4:
                raise e

            time.sleep(1)
            continue
        # If it is another error, different from zero results, raises an exception
        elif str(e).find('ZERO_RESULTS') == -1:
            raise e
        else:
            break




        # query_result = google_places.nearby_search(
        #     location={'lat':  , 'lng': event['longitude']},
        #     radius=event['radius'],
        #     pagetoken=query_result_next_page,
        #     request_count=request_count)
        # If there are additional result pages, lets get it on the next while step
        # print(NYC_response)









# reads pop stats for 2019
la_pop_df = pd.read_csv(LA_pop_filepath)
nyc_pop_df = pd.read_csv(NYC_pop_filepath)
# population data frame creation
LA_pop_2019 = la_pop_df['Los Angeles County, California!!Estimate'].max()
NYC_pop_2019 = nyc_pop_df['New York city, New York!!Estimate'].max()

# makes list for gunstore names
StoreNamesLA = []
StoreNamesNYC = []
# gets all gun store names and credit to KING JAKE PERRY and ZACK for being the GOATS
for all in LA_ALLDATA:

    for x in all["results"]:
        StoreNamesLA.append(x["name"])

for all in NYC_ALLDATA:
    for x in all["results"]:
        StoreNamesNYC.append(x["name"])

# calculates total gunstores by using length of store names above
Total_GunstoresLA = len(StoreNamesLA)
Total_GunstoresNYC = len(StoreNamesNYC)

# takes commas out of city pop totals
LA_pop_2019 = 10039107
NYC_pop_2019 = 8336817
# adds per 100k rate for population
LA_percapita = LA_pop_2019/100000
NYC_percapita = NYC_pop_2019/100000
LAGuncrime_percapita = LATotalGunCrime/LA_percapita
NYCGuncrime_percapita = NYCTotalGunCrime/NYC_percapita

# makes visualized data
x = ["LA Gun Crime" , "LA Gunstores"]
y = [LAGuncrime_percapita, Total_GunstoresLA]
x1 = ["NYC Gun Crime", "NYC Gunstores"]
y1 = [NYCGuncrime_percapita, Total_GunstoresNYC]
x2 = ["LA population/100k", "LA Gun Crime"]
y2 = [LA_percapita, LAGuncrime_percapita]
x3 = ["NYC population/100k", "NYC Gun Crime"]
y3 = [NYC_percapita, NYCGuncrime_percapita]
LA = plt.bar(x, y)
plt.title("LA Gun Crime vs. Gun Stores")
plt.savefig("visuals/LA_guncrime_vs_gunstores.png")
plt.show()

NY = plt.bar(x1, y1)
plt.title("NYC Gun Crime vs. Gun Stores")
plt.savefig("visuals/new_york_guncrime_vs_gunstores.png")
plt.show()
LA_POP = plt.bar(x2, y2)
plt.title("LA Population per 100k vs. Gun Crime")
plt.savefig("visuals/LA_Pop_vs_gunstores.png")
plt.show()
NYC_POP = plt.bar(x3, y3)
plt.title("NYC Population per 100k vs. Gun Crime")
plt.savefig("visuals/NYC_Pop_vs_gunstores.png")
plt.show()

