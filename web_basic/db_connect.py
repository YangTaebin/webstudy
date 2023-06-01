import pymysql
import xml.etree.ElementTree as ET

user = "root"

def db():
    login_data = ET.parse("DB_login_data.xml").getroot()
    db = pymysql.connect(host="localhost", user=user, password=login_data.find(user).find("pw").text)
    db_cursor = db.cursor(pymysql.cursors.DictCursor)
    return db, db_cursor

if __name__ == "__main__":
    db, cursor = db()
    cursor.execute("insert into dreamhack.test (uid, upw) values ('admin','admin')")
    db.commit()

    cursor.execute("select * from dreamhack.test")
    data = cursor.fetchall()
    print(data)