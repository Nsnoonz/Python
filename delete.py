import connect
import select
def delete_data():
    try:
        while True:
            print("\n Menu")
            print("[1] delete Product")
            print("[2] delete Product Type")
            print("[3] Exit")
            input_choice = int(input("Choose Menu  : "))
            if (input_choice == 1):
                print("-"*30,"delete Product","-"*30)
                delete_product()
                print("-"*73)
            elif (input_choice == 2):
                print("-"*30,"delete Product Type","-"*30)
                delete_type()
                print("-"*74)
            elif (input_choice == 3):
                break
            else:
                print(">>> Please input number 1-3 !!!")
    except:
        print(">>> Error Please input number 1-3")
        delete_data()

def delete_product():
    db, conn = connect.connect_db()
    select.show_product()
    input_productID = int(input("input productID: "))
    sql2 = "SELECT * FROM product WHERE productID =%s "
    chk = (input_productID)
    conn.execute(sql2,chk)
    data_all = conn.fetchall()
    if data_all ==():
        print(">>Prouduct ID not correct ! ")
        print("Please Try again later")
    elif data_all != ():
        print(data_all[0])
        cf = input('Comfirm Delete Data ? y/n: ').lower()
        if(cf == 'y'):
            sql = "Delete From product where productID = %s"
            delete_datas = (input_productID)
            conn.execute(sql, delete_datas)
            db.commit()
            print(">>>Delete successful<<<<")
            select.show_product()
        else:
            print(">>>See you later")
    db.close()

def delete_type():
    db, conn = connect.connect_db()
    select.all_type()
    input_typeID = int(input("input typeID: "))
    sql3 = "SELECT * FROM producttype WHERE typeID =%s "
    chk = (input_typeID)
    conn.execute(sql3,chk)
    data_all = conn.fetchall()
    if data_all ==():
        print(">>Type ID not correct ! ")
        print("Please Try again later")
    elif data_all != ():
        sql2 = "select * from producttype,product where  (product.typeID Like %s) AND producttype.typeID = product.typeID"
        chk2 = (input_typeID)
        conn.execute(sql2,chk2)
        data_all2 = conn.fetchall()
        i = []
        for data in data_all2 :
            if i != data[6]:
                print(">>Failed to delete . This Type have product.")
                i = data[6]
            print("Type :",data[0],data[1],"Id:", data[2], "Name :", data[3], "\tAmount :", data[5])
        if data_all2 ==():
            for data in data_all:
                print("Type :",data[0],"| Name :",data[1])
            cf = input('Comfirm Delete Data ? y/n: ').lower()
            if(cf == 'y'):
                sql = "Delete From producttype where typeID = %s"
                delete_datas = (input_typeID)
                conn.execute(sql, delete_datas)
                db.commit()
                print(">>>Delete successful<<<<")
                select.all_type()
            else:
                print(">>>See you later")
    db.close()
