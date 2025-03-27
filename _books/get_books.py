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
    books['year_group'] = books['Date Started'].dt.year
    
    yml = "# encoding: utf-8\n"

    years = sorted(books['year_group'].unique(), reverse = True)

    for year in years:
        header = f"- title: {year}\n  type: list\n  contents:\n"
        yml = yml + header
        for index, row in books.sort_values(by=['Date Started'], ascending=False).iterrows():
            if row['year_group'] == year:
                entry = create_yml(row)
                yml = yml + entry

    filename = "../_data/books.yml"
    print(filename)

    with open(filename, 'w', encoding="utf-8") as y:
        y.write(yml)

def create_yml(row):
    if row['Gave Up']:
        status = "Gave Up"
        year = row['Date Finished'].year
        return("") # Don't add a new row for DNF books
    elif pd.isnull(row['Date Finished']):
        status = "In Progress"
        year = row['Date Started'].year
    else:
        status = "Finished"
        year = row['Date Finished'].year

    yml = f'    - "<i>{row["Title"]}</i> - {row["Author"]} - {status}"\n'

    return(yml)

    

if __name__ == "__main__":
    main()