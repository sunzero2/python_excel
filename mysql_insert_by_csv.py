import mysql.connector
import csv

def insert_value(values) :
  sql = "INSERT INTO HARDWARE (TYPE_ID, BRAND, MODEL, CAPACITY) VALUES ({typeId}, '{brand}', '{model}', {capacity})"

  # print(sql.format(typeId=values[0], brand=values[1], model=values[2], capacity=values[3]))
  mycursor.execute(sql.format(typeId=values[0], brand=values[1], model=values[2], capacity=values[3]))

mydb = mysql.connector.connect (
  host="127.0.0.1",
  user="root",
  password="1234",
  database="ngle_pc"
)

mycursor = mydb.cursor()

with open('/Users/leehyeyeong/ngle-pc-csv.csv') as csvfile :
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader :
    insert_value(row)
  mydb.commit()

