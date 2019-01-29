#!/usr/bin/python3.6

import sqlite3
conn = sqlite3.connect("cinema_db.sqlite")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS movies (
rowid INTEGER,
date DATETIME,
format TEXT,
mpaa TEXT,
stars TEXT,
synopsis TEXT,
theater TEXT,
title TEXT,
time1 TEXT,
time2 TEXT,
time3 TEXT,
time4 TEXT,
time5 TEXT,
time6 TEXT,
time7 TEXT,
time8 TEXT,
movieday TEXT,
cityaddy TEXT
)
""")

conn.commit()
conn.close()
