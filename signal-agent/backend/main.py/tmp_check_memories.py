import sqlite3
conn = sqlite3.connect('database/signal_agent.db')
cur = conn.cursor()
cur.execute('select category,key,value,confidence from memories order by id desc limit 20')
for row in cur.fetchall():
    print(row)
conn.close()
