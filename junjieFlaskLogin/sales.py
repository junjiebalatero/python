import sqlite3 as lite
import sys

sales = (
    ('john', 22000),
    ('Peter', 27000),
    ('Simon', 12000),
    ('Joseph', 25600),
    ('mathhew', 82000),
    ('lawrence', 62000),
    ('junjie', 29000),
    ('harry', 32000),
    ('anthony', 5000),
    ('Jojo', 800)
)

con = lite.connect('sales.db')

with con:

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS reps")
    cur.execute("CREATE TABLE reps(rep_name TEXT, amount INT)")
    cur.executemany("INSERT INTO reps VALUES(?, ?)", sales)