#Need to import python libraries to scrape the Fortune Website
import requests, bs4
from datetime import date
import calendar
import os

#User inputs regarding the date in which they are seeking news
User_year=2018 #must be an integer
User_month=8 #must be an integer
User_day=10  #must be an integer
User_Output_Location="C:\Project1" #Where does the user want the data ouput?
#Program will not work when not a weekday


#Create a function that creates the forturne web url, based on the date from the user.
def scraping_url(year, month, day):
    mydate = date(year, month, day)

    Day_Of_Week = calendar.day_name[mydate.weekday()]
    #print(mydate)
    #print(Day_Of_Week)
    mymonth = calendar.month_name[mydate.month]
    if (month < 10):
        month = str(0) + str(month)
    if (day < 10):
        day1 = str(0) + str(day)
    if (day >= 10):
        day1=str(day)
    #print(mymonth)
    string = 'http://fortune.com/' + str(year) + "/" + str(month) + "/" + str(day1) + "/term-sheet-" + str(
        Day_Of_Week).lower() + "-" + str(mymonth).lower() + "-" + str(day)+"/"

    return(string)



#The previous function creates the url to scrape
Scrape_Url = scraping_url(User_year,User_month,User_day)

print(Scrape_Url)

request=str(Scrape_Url)
page = requests.get(request)
soup = bs4.BeautifulSoup(page.text, 'html.parser')
#print (soup)
value = soup.findAll("div", "listicle-text")
text=value[2].text
print(text)

#Header at the top of the articles.

Scrape_Date=str(User_month)+"/"+str(User_day)+"/"+str(User_year)
Scrape_Date_FileName=str(User_month)+"_"+str(User_day)+"_"+str(User_year)

#Location of the output files
os.chdir(User_Output_Location)

#Ouput the file

save_string="New_Financings_"+str(Scrape_Date_FileName)+".doc"
text_file = open(save_string, 'w')
text_file.write(Scrape_Date+"\n"+ text)
text_file.close()




