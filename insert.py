import connect
import select
def insert_data():
    try:
        while True:
            print("\n Menu")
            print("[1] insert Product")
            print("[2] insert Product Type")
            print("[3] Exit")
            input_choice = int(input("Choose Menu  : "))
            if (input_choice == 1):
                print("-"*30,"insert Product","-"*30)
                insert_product()
                print("-"*73)
            elif (input_choice == 2):
                print("-"*30,"insert Product Type","-"*30)
                insert_type()
                print("-"*74)
            elif (input_choice == 3):
                break
            else:
                print(">>> Please input number 1-3 !!!")

    except:
        print(">>> Error Please input number 1-3 !!!")
        insert_data()

def insert_product():
    db, conn = connect.connect_db()
    print("=== Insert Product ===")
    input_productName = input("please input Name : ").capitalize()
    input_productPrice = input("please input Price : ")
    input_productAmount = input("please input Amount : ")
    select.all_type()
    input_typeID = input("please input typeID : ")
    sql2 = "SELECT * FROM producttype WHERE typeID =%s "
    chk = (input_typeID)
    conn.execute(sql2,chk)
    data_all = conn.fetchall()
    if data_all ==():
        print(">>Type ID not correct ! ")
        print("Please Try again later")
    elif data_all != ():
        cf = input('Comfirm insert Data ? y/n: ').lower()
        if(cf == 'y'):
            sql = "insert into product(productName , productPrice,productAmount,typeID) VALUES(%s,%s,%s,%s) "
            insert_datas = (input_productName, input_productPrice, input_productAmount,input_typeID)
            conn.execute(sql, insert_datas)
            db.commit()
            print(">>>insert successful<<<<")
            select.show_product()
        else:
            print(">>>See you later")
    db.close()
    
def insert_type():
    db, conn = connect.connect_db()
    print("=== Insert Type of Product ===")
    input_typeName = input("please input Name : ").capitalize()
    cf = input('Comfirm insert Data ? y/n: ').lower()
    if(cf == 'y'):
        sql = "insert into producttype(typeName)VALUE(%s)"
        insert_datas = (input_typeName)
        conn.execute(sql,insert_datas)
        db.commit()
        print(">>>insert successful<<<<")
        select.all_type()
    else:
        print(">>>See you later")
    db.close()
