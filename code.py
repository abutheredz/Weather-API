import requests
import pandas as pd
from datetime import datetime
from IPython.display import display

API_KEY = "kNU1mUkOJIF1FqjRg7BRsEQlF3w8DJvv"


#City Search

def city_search(api_key,q):
  end_point = "http://dataservice.accuweather.com/locations/v1/cities/search"
  params = {
      "apikey":api_key,
      "q":q
  }

  response =requests.get(end_point,params = params)

  if response.status_code == 200:
    return response.json()
  else:
    return "Error"

##Alternative if u want to print the actual result data
#city_result1= city_search(API_KEY,"kuala lumpur")
#print(city_result1)


#2 - Current Conditions


def get_current_condition(api_key,location_key):

  endpoint = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}"
  params = {
      "apikey":api_key,

  }
  response =requests.get(endpoint,params = params)


  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: {response.status_code}")
    return "Error"


### 1 DAY OF DAILY FORECAST


def get_daily_forecast(api_key,location_key):

  endpoint = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}"
  params = {
      "apikey":api_key,

  }
  response =requests.get(endpoint,params = params)


  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error: {response.status_code}")
    return "Error"



