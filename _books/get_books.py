import pandas as pd
from datetime import datetime
import os

#TODO: I want a better way to show the books I have read and the rating I have assigned to them other than creating a separate page for each. I only want to create a separate page if I have written a review of the book. This script should generate the overall bookshelf page and use conditional logic to determine if a given book should have its own page generated as well. 

#TODO: Try to use javascript to add dynamic features to bookshelf (e.g. expand book card to show review.)

def main():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    id = "1HRUE1KFrSYlc8Dwd5KG8aQ03tgWFeMjPWMZIfJ65NIM"
    sheet = "books"
    url = f"https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:csv&sheet={sheet}"
    books = pd.read_csv(url)
    books['Date Started'] = pd.to_datetime(books['Date Started'])
    books['Date Finished'] = pd.to_datetime(books['Date Finished'])
    for index, row in books.iterrows():
        create_md(row)


def create_md(row):
    if row['Gave Up']:
        status = "abandoned"
        year = row['Date Finished'].year
    elif pd.isnull(row['Date Finished']):
        status = "reading"
        year = row['Date Started'].year
    else:
        status = "finished"
        year = row['Date Finished'].year
    desc = row['API Description']
    if type(desc) == str:
        desc = desc.encode('ascii', errors='ignore').decode('ascii')
    if pd.isnull(row['Stars']):
        stars = 0
    else:
        stars = row['Stars']
    if pd.isnull(row['cover']):
        cover = ""
    else:
        cover = f"'row['cover']'"
    md = (
        "---\n"
        "published: true\n"
        "layout: review\n"
        f"date-started: '{row['Date Started']}'\n"
        f"date-finished: '{row['Date Finished']}'\n"
        f"cover: {cover}\n"
        "olid:\n"
        f"isbn: {row['ISBN']}\n"
        f"title: '{row['Title']}'\n"
        f"year: {year}\n"
        f"status: {status}\n"
        f"stars: {stars}\n"
        f"type: {row['Type']}\n"
        f"language: {row['Language']}\n"
        "---\n"
        f"{desc}"
    )

    filename = f"{row['Title'].replace(' ', '-').replace('?','').replace(':','')[0:40]}.md"
    print(filename)

    with open(filename, 'w') as m:
        m.write(md)

    

if __name__ == "__main__":
    main()