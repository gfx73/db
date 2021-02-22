import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="12345678", host="127.0.0.1", port="5432")

cur = con.cursor()
cur.execute('''CREATE TABLE CUSTOMER
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      ADDRESS        TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      REVIEW         TEXT);''')

con.commit()
con.close()
