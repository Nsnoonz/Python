import pymysql
def connect_db():
    try:
        db = pymysql.connect(user="root",password="",host="localhost",database="py_62011270006",
                             use_unicode=True,charset="utf8")
        conn = db.cursor()
        return db, conn
    except:
        print("Error")
