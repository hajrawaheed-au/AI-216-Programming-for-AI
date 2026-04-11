#Task 1

import requests
from bs4 import BeautifulSoup

url="http://quotes.toscrape.com"
response=requests.get(url)
soup= BeautifulSoup(response.text,"html.parser")
quotes=soup.find_all("div",class_="quote")
quotes_data=[]
for q in quotes:
    text=q.find("span", class_="text").text
    Author=q.find("small",class_="author").text

quotes_data.append({
    "Quotes": text,
    "Authors": Author
})
print(quotes_data)

#Task 2

import requests
from bs4 import BeautifulSoup

all_data = []

for page in range(1, 4):

    url = f"http://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text

        all_data.append({
            "quote": text,
            "author": author
        })

print("Total Quotes:", len(all_data))

for item in all_data[:5]:
    print(item["quote"], "-", item["author"])
    
#Task 3

import sqlite3

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY,
    quote TEXT,
    author TEXT
)
""")

conn.commit()
conn.close()

print("Table created successfully!")

#task 4

import sqlite3

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

data_to_insert = []

for item in all_data:
    data_to_insert.append((item["quote"], item["author"]))

cursor.executemany(
    "INSERT INTO quotes (quote, author) VALUES (?, ?)",
    data_to_insert
)

conn.commit()
conn.close()

print("Data inserted successfully!")

#Task 5

import sqlite3

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM quotes")
all_quotes = cursor.fetchall()

print(" All Quotes ")
for row in all_quotes:
    print(row)

print("\nTotal number of quotes:", len(all_quotes))

cursor.execute("SELECT * FROM quotes LIMIT 10")
first_10 = cursor.fetchall()

print("\n=== First 10 Quotes ===")
for row in first_10:
    print(row)


# Task 6 

author_name = "Albert Einstein"   

cursor.execute("SELECT * FROM quotes WHERE author = ?", (author_name,))
author_quotes = cursor.fetchall()

print(f"\n Quotes by {author_name} ")
for row in author_quotes:
    print(row)

cursor.execute("""
SELECT author, COUNT(*) as total_quotes
FROM quotes
GROUP BY author
""")

quotes_per_author = cursor.fetchall()

print("\n Quotes Count per Author ")
for row in quotes_per_author:
    print("Author:", row[0], "| Quotes:", row[1])


cursor.execute("""
SELECT author, COUNT(*) as total_quotes
FROM quotes
GROUP BY author
ORDER BY total_quotes DESC
""")

sorted_authors = cursor.fetchall()

print("\n Authors Sorted by Number of Quotes ")
for row in sorted_authors:
    print("Author:", row[0], "| Quotes:", row[1])

conn.close()

import sqlite3

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

# Task 7 – Update Records

author_name = "Albert Einstein"

updated_name = author_name.upper()

cursor.execute("""
UPDATE quotes
SET author = ?
WHERE author = ?
""", (updated_name, author_name))

conn.commit()

print(f"Author '{author_name}' updated to '{updated_name}'")


# Task 8 

cursor.execute("""
DELETE FROM quotes
WHERE LENGTH(quote) < 30
""")

conn.commit()

print("Quotes with less than 30 characters deleted.")

cursor.execute("SELECT * FROM quotes LIMIT 10")
print("\nUpdated Data (First 10 Rows):")
for row in cursor.fetchall():
    print(row)

conn.close()

#Task 9:

url = "http://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

quotes = soup.find_all("div", class_="quote")

for q in quotes:
    text = q.find("span", class_="text").get_text()
    author = q.find("small", class_="author").get_text()
    quotes_data.append((text, author))

print("Scraping Done. Total scraped:", len(quotes_data))

conn = sqlite3.connect("quotes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote TEXT,
    author TEXT
)
""")

cursor.executemany("INSERT INTO quotes (quote, author) VALUES (?, ?)", quotes_data)

conn.commit()

print("Data stored in database.")

cursor.execute("SELECT COUNT(*) FROM quotes")
total_quotes = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(DISTINCT author) FROM quotes")
unique_authors = cursor.fetchone()[0]

cursor.execute("""
SELECT author, COUNT(*) as total
FROM quotes
GROUP BY author
ORDER BY total DESC
LIMIT 1
""")

top_author = cursor.fetchone()

print("\n REPORT ")
print("Total Quotes Stored:", total_quotes)
print("Total Unique Authors:", unique_authors)
print("Top Author:", top_author[0], "| Quotes:", top_author[1])

conn.close()

#Task 10: Ethical data collection

url = "https://github.com/robots.txt"
response = requests.get(url)

lines = response.text.split("\n")

print(" FIRST 20 LINES OF robots.txt\n")

for i in range(min(20, len(lines))):
    print(lines[i])

disallowed_paths = []

for line in lines:
    if line.startswith("Disallow"):
        path = line.split(":")[1].strip()
        if path != "":
            disallowed_paths.append(path)

print("\n DISALLOWED DIRECTORIES \n")

if len(disallowed_paths) == 0:
    print("No disallowed paths found.")
else:
    for i in range(min(2, len(disallowed_paths))):
        print(disallowed_paths[i])