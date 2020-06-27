'''Program will extract name, email, phone from a given html file, required only the information inside the html is changed
and not the format of whole html file'''
'''BeautifulSoup(bs4) is a Python package for parsing HTML documents'''
import bs4
import json

# First we open the html file which we have to parse
with open("New Lead .html") as html:
    # here we convert the content of html file to a soup object which is used to extract information
    soup = bs4.BeautifulSoup(html,"lxml")

#find_all method will help to locate all the mentioned elements.
data1 = soup.find_all("td", {"class": "aligncenter"})       # In this case find_all will look for all occurances of tag td which has class: aligncenter and we store that data in a list
#find() helps to locate 1st occurance of element in soup
name = data1[3].find("strong").text                         # Then after checking the list we can extract our required information

# Similar steps are done to extract email and phone
data2 = soup.find_all("td", {"class": "width280"})          # Here I looked for some exclusive arguments inside tags that would narrow down the scope so class was that exclusive argument inside td tag
email = data2[0].find("a", {"style": "color: #d92228; text-decoration:none;"}).text     # Then inside data2 list I used find() to locate email. I got that after noticing the color of email text which was red so i used that as exclusive argument
phone = data2[0].find("a", {"style": "text-decoration:none;border:none;color:#fff;"}).text  # Similarly phone number had a different color so i used that to extract data

# Finally insert all the extracted data in a dictionary
buyer = {'Name':name, 'email':email, 'phone':phone}

# Using dumps method from json we cast the dictionary into json format
s = json.dumps(buyer)
# Then we write it in a json file
with open("output.json","w") as fp:
    fp.write(s)
