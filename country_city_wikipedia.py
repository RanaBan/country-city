import requests 
from bs4 import BeautifulSoup 
import os
import re
import pandas as pd

def country_city_pair():
    url='https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_'
    cities=[]
    countries=[]
    alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for a in alpha:
        u=url+a
        resp=requests.get(u) 

        #http_respone 200 means OK status 
        if resp.status_code==200: 
                
            # Python built-in HTML parser. 
            soup=BeautifulSoup(resp.content,'html.parser')     

            all_texts=soup.find_all("td") 
            # print(all_texts)
            i=1

            for txt in all_texts:

                place=''
                t=txt.find_all('a')
                if t:
                    place=re.sub(r'<[^>]+>','',str(t[0]))

                if i==1:
                    cities.append(place)
                    i=0
                else:
                    countries.append(place)
                    i=1
        else:
            print('error')
        print(a)
    return cities, countries

cities, countries = country_city_pair()
if len(cities) and len(countries):
    city_country=pd.DataFrame({'countries': countries, 'cities': cities})
    # city_country.to_csv('city_country.csv')
    print(len(city_country))
