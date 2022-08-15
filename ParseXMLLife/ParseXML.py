import xml.etree.ElementTree as ET
import mysql.connector

#pip install mysql-connector-python
#install MySQL https://dev.mysql.com/downloads/windows/installer/8.0.html
#fill in 'user' 'password' 'host' 'database' with your own things
conn = mysql.connector.connect(user='root', password='1234',
                              host='localhost',database='company')
if conn:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")

tree = ET.ElementTree(file="api.xml")
root = tree.getroot()
cursor = conn.cursor()
#create whatever table's name, data types you want
# cursor.execute("CREATE TABLE Journal (title VARCHAR(500),author VARCHAR(1000), venue VARCHAR(50), volume VARCHAR(500), pages VARCHAR(50), year VARCHAR(10), Type VARCHAR(50), access VARCHAR(10), Keyy VARCHAR(100), doi VARCHAR(100), ee VARCHAR(100), url VARCHAR(100))")
# some variables to store information of each element
title = ''
venue = ''
volume = ''
pages = ''
year = ''
typee = ''
access =''
Keyy = ''
doi = ''
ee = ''
url = ''
author = ''
# traverse the children with the name 'info' in api.xml and get the information of each element
for child in root.findall("./hits/hit/info"):
    author = ''
    title = child[1].text.encode('unicode-escape').decode('utf-8')2 3
    venue = child[2].text.encode('unicode-escape').decode('utf-8')
    volume = child[3].text.encode('unicode-escape').decode('utf-8')
    pages = child[4].text.encode('unicode-escape').decode('utf-8')
    year = child[5].text.encode('unicode-escape').decode('utf-8')
    typee = child[6].text.encode('unicode-escape').decode('utf-8')
    access = child[7].text.encode('unicode-escape').decode('utf-8')
    Keyy = child[8].text.encode('unicode-escape').decode('utf-8')
    doi = child[9].text.encode('unicode-escape').decode('utf-8')
    ee = child[10].text.encode('unicode-escape').decode('utf-8')
    url = child[11].text.encode('unicode-escape').decode('utf-8')
    for a in child[0]:
        author += a.text + "\n"
    #insert info into the table
    employee = "INSERT INTO Journal (title, author, venue, volume, pages, year, type, access, Keyy, doi, ee, url) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(employee,(title, author, venue, volume, pages, year, typee, access, Keyy, doi, ee, url))
    conn.commit()
    print("Data inserted successfully.")
    # cursor.execute("SELECT * FROM Journal")
    # for x in cursor:
    #     print(x)


# print(title)
# print(venue)
# print(volume)
# print(pages)
# print(year)
# print(typee)
# print(Keyy)
# print(doi)
# print(ee)
# print(url)
# print(author)
