from bs4 import BeautifulSoup
import time 
import csv
import requests 

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
time.sleep(10)
solar_data=[]
new_solar_data=[]
url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)
soup = bs(page.text,'htm.parser')
star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')
headers=["star_name","Distance_data","Mass","Radius"]
solar_data=[]
def scrape():
    for i in range(0,489):
        soup = BeautifulSoup("html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index==0 :
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            solar_data.append(temp_list)

def scrape_more_data(hyperlink):
    page=requests.get(hyperlink)
    soup=BeautifulSoup(page.content,"html.parser")
    for tr_tag in soup.find_all("tr", attrs={"class":"fact_row"}):
        td_tags = tr_tag.find_all("td")
        temp_list=[]
        for td_tag in td_tags:
            try:
                temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0])
            except:
                temp_list.append("")
                new_solar_data.append(temp_list)
scrape()
for data in solar_data:
    scrape_more_data(data[5])

final_solar_data=[]
for index,data in enumerate(solar_data):
    final_solar_data.append(data+final_solar_data[index])

with open("final.csv","w") as f:
    csvwriter= csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerow(final_solar_data)
 