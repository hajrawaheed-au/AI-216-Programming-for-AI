# AI-216 – Programming for AI

## Lab 06 – Web Scraping, SQLite & Ethical Data Collection

---

##  Overview

This lab focuses on building a simple data pipeline that includes:

* Web scraping
* Data storage using SQLite
* Database querying
* Ethical considerations in data collection

---

## 🔹 How Data Was Scraped

The data was scraped from a quotes website using Python.

### Tools Used:

* `requests` → to send HTTP request and get webpage
* `BeautifulSoup` → to parse HTML content

### Process:

1. Sent a request to the website using `requests.get()`
2. Parsed HTML using BeautifulSoup
3. Extracted:

   * Quote text
   * Author name
4. Stored extracted data in a list of tuples

Example:

```python
text = q.find("span", class_="text").get_text()
author = q.find("small", class_="author").get_text()
```

---

## 🔹 SQLite Database Structure

The scraped data was stored in an SQLite database named **quotes.db**.

### Table Name:

`quotes`

### Table Schema:

| Column | Type    | Description                  |
| ------ | ------- | ---------------------------- |
| id     | INTEGER | Primary Key (Auto Increment) |
| quote  | TEXT    | Stores quote text            |
| author | TEXT    | Stores author name           |

### SQL Table Creation:

```sql
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote TEXT,
    author TEXT
);
```

### Data Insertion:

* Used parameterized queries (`?`)
* Inserted multiple records using `executemany()`

---

## 🔹 Ethical Concern in Web Scraping

One major ethical concern in web scraping is **ignoring the website’s rules defined in robots.txt**.

### Why it matters:

* Some parts of a website are restricted for bots
* Scraping restricted data may violate terms of service
* It can lead to IP blocking or legal issues

### Solution:

Before scraping:

* Always check the website’s `robots.txt` file
* Respect `Disallow` rules
* Avoid overloading the server

---



##  Conclusion

In this lab, we learned how to:

* Extract data from websites
* Store structured data in SQLite
* Perform queries for analysis
* Follow ethical scraping practices

---
