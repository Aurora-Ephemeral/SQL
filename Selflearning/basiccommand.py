import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute("create table user(id varchar(20) primary key, name varchar(20), score int)")
insert_stmt =(
    "insert into user(id, name, score) values(?,?,?)"
)
data = [('A-001','Adam',95),('A-002', 'Bart', 62),('A-003', 'Lisa', 78)]
for i in data:
    cursor.execute(insert_stmt,i)
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('select * from user where score >= ? and score <= ?',(low, high))
    values=cursor.fetchall()
    cursor.close()
    conn.close()
    return values


