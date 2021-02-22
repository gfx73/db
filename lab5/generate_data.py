import psycopg2
import random
from faker import Faker

con = psycopg2.connect(database="postgres", user="postgres", password="12345678", host="127.0.0.1", port="5432")

cur = con.cursor()

fake = Faker()
for i in range(100000):
    print(i)
    cur.execute("INSERT INTO CUSTOMER (ID, NAME, ADDRESS, AGE, REVIEW) VALUES ('" + str(i) + "','" + fake.name()+"','" +
                fake.address() + "','" + str(int(random() * 100)) + "','" + fake.text()+"')")
    con.commit()

con.close()
