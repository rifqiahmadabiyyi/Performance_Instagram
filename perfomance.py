from tabulate import tabulate
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_sma2"
)

mycursor = mydb.cursor()

sql = "select ig_username, follower_count, url from tbl_scraping where follower_count=(select max(follower_count) from tbl_scraping) or follower_count=(select min(follower_count) from tbl_scraping) limit 2"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print(tabulate(myresult, headers=["Username","Follower", "Url"], tablefmt="github"))