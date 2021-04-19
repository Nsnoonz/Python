import connect
import select
def update_data():
    try:
        while True:
            print("\n Menu")
            print("[1] update Product")
            print("[2] update Product Type")
            print("[3] update")
            print("[4] Exit")
            input_choice = int(input("Choose Menu  : "))
            if (input_choice == 1):
                print("-"*30,"update Product","-"*30)
                update_product()
                print("-"*73)
            elif (input_choice == 2):
                print("-"*30,"update Product Type","-"*30)
                update_type()
                print("-"*74)
            elif (input_choice == 3):
                print("-"*30,"update ","-"*30)
                update()
            elif (input_choice == 4):
                break
            else:
                print(">>> Please input number 1-4 !!!")

    except:
        print(">>> Error Please input number ")
        update_data()

def update_product():
    db, conn = connect.connect_db()
    select.show_product()
    input_productName = input("please input Name : ").capitalize()
    input_productPrice = input("please input Price : ")
    input_productAmount = input("please input Amount : ")
    select.all_type()
    input_typeID = int(input("please input typeID : "))
    input_productID = int(input("input productID: "))
    sql2 = "SELECT * FROM product,producttype WHERE product.productID =%s AND producttype.typeID =%s "
    chk = (input_productID,input_typeID)
    conn.execute(sql2,chk)
    data_all = conn.fetchall()
    if data_all ==():
        print(">>Prouduct ID or Type ID not correct ! ")
        print("Please Try again later")
    elif data_all != ():
        cf = input('Comfirm Update Data ? y/n: ').lower()
        if(cf == 'y'):
            sql = "Update  product Set productName=%s,productPrice=%s,productAmount=%s,typeID=%s where productID = %s "
            update_datas = (input_productName, input_productPrice, input_productAmount,input_typeID,input_productID)
            conn.execute(sql, update_datas)
            db.commit()
            print(">>>Update successful<<<<")
            select.show_product()
        else:
            print(">>>See you later")
    db.close()



def update_type():
    db, conn = connect.connect_db()
    select.all_type()
    input_typeName = input("please input Name : ").capitalize()
    input_typeID = int(input("input id: "))
    sql2 = "SELECT * FROM producttype WHERE typeID =%s "
    chk = (input_typeID)
    conn.execute(sql2,chk)
    data_all = conn.fetchall()
    if data_all ==():
        print(">>Type ID not correct ! ")
        print("Please Try again later")
    elif data_all != ():
        cf = input('Comfirm Update Data ? y/n: ').lower()
        if(cf == 'y'):
            sql = "Update  producttype Set typeName = %s where typeID = %s "
            update_datas = (input_typeName,input_typeID)
            conn.execute(sql,update_datas)
            db.commit()
            print(">>>Update successful<<<<")
            select.all_type()
        else:
            print(">>>See you later")
    db.close()

def update():
    db, conn = connect.connect_db()
    select.show_product()
    productID = int(input("input productID: "))
    sql = "select * from product where productID = %s"
    conn.execute(sql,productID)
    data_all = conn.fetchall()
    if data_all == ():
        print(">>productID not correct!")
    for data in data_all:
            cf1 = input('Do you want to Update Name ? y/n: ').lower()
            if(cf1 == 'y'):
                productName = input("please input Name : ").capitalize()
            elif(cf1 == 'n'):
                productName = data[1]
            cf2 = input('Do you want to Update Price ? y/n: ').lower()
            if(cf2 == 'y'):
                productPrice = input("please input Price : ")
            elif(cf2 == 'n'):
                productPrice = data[2]
            cf3 = input('Do you want to Update Amount ? y/n: ').lower()
            if(cf3 == 'y'):
                productAmount = input("please input Amount : ")
            elif(cf3 == 'n'):
                productAmount = data[3]

            select.all_type()
            typeID = int(input("please input typeID : "))
            sql2 = "SELECT * FROM producttype WHERE producttype.typeID =%s "
            conn.execute(sql2,typeID)
            data_all2 = conn.fetchall()
            if data_all2 ==():
                print(">>Type ID not correct ! ")
                print("Please Try again later")
            elif data_all2 != ():
                print("Id:",productID , "| Name :",productName , "| Price :", productPrice, "| Amount :", productAmount,"| Type :", typeID)
                cf = input('Comfirm Update Data ? y/n: ').lower()
                if(cf == 'y'):
                    sql3 = "Update  product Set productName=%s,productPrice=%s,productAmount=%s,typeID=%s where productID = %s "
                    update_datas = (productName, productPrice, productAmount,typeID,productID)
                    conn.execute(sql3, update_datas)
                    db.commit()
                    print(">>>Update successful<<<<")
                    select.show_product()
                else:
                    print(">>>See you later")
    db.close()
