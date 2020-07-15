# An example to scrape information from a html document
Concepts: web scrapping, parsing

Clone the repository to desktop.
Run parser.py which is the main file which will extract name, email, phone, address, number of beds and baths from a given html file.

HTML file used in this example is a real estate networking website mail which has information of a potential property for sale. Considering these mails are auto generated we can use this script to any similar html file to scrape data from the file.


Running code on linux:
1: Install python
2: Open terminal
type:
3: pip3 install bs4
4: pip3 install lxml

5: Download the directory(Place both new lead.html and parser.py in same folder)
6: open terminal inside our folder
7: type- python3 parser.py
By running this file you will notice that a new file will be created with name output.json. This file will have details of name, email & phone no. from html file.
