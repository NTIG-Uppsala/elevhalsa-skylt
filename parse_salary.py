#!/usr/bin/python3
import requests, csv, subprocess
from bs4 import BeautifulSoup

def get_salary(profession):
    try:
        page = requests.get('https://www.framtid.se/yrke/' + profession)

        soup = BeautifulSoup(page.text, 'html.parser')

        salaryElem = soup.find(class_="salary-amount")

        return salaryElem.contents[0]
    except Exception as err:
        print(err)
        return "Okänt"

def makeUrlFriendly(text):
    text = text.lower()
    new_text = text.replace("å", "a").replace("ä", "a").replace("ö", "o")
    return new_text

data = []
with open("site/_data/professions.csv") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    headings = []
    for idx, row in enumerate(spamreader):
        if idx == 0:
            for heading in row[0].split(","):
                headings.append(heading)
        else:
            current_row = " ".join(row)
            profession = makeUrlFriendly(current_row.split(",")[0])
            salary = get_salary(profession)
            current_row += "," + salary
            data.append(current_row)

    headings.append('BRUTTOLON')
    data.insert(0, ",".join(headings))

with open("site/_data/professions.csv", "w") as fd:
    for i in range(len(data)):
        fd.write(data[i] + "\n")
