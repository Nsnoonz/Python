import connect
import select
def search_data():
        try:
            while True:
                print("\n Menu")
                print("[1] Search Product")
                print("[2] Search Product Type")
                print("[3] Search Product Price")
                print("[4] Exit")
                input_choice = int(input("Choose Menu  : "))
                if (input_choice == 1):
                    print("-"*30,"Search Product","-"*30)
                    search_product()
                    print("-"*73)
                elif (input_choice == 2):
                    print("-"*30,"Search Product Type","-"*30)
                    search_type()
                    print("-"*74)
                elif (input_choice == 3):
                    print("-"*30,"Search Product Price","-"*30)
                    search_price()
                    print("-"*74)
                elif (input_choice == 4):
                    break
                else:
                    print(">>> Please input number 1-3 !!!")
        except:
            print(">>> Error Please input number 1-3")
            search_data()

def search_product():
    db, conn = connect.connect_db()
    input_search = input("Search Product Name  : ")
    sql = "select * from product,producttype where product.typeID = producttype.typeID \
    and (product.productName LIKE %s ) "
    search=['%'+input_search+'%']
    conn.execute(sql,search)
    data_all = conn.fetchall()
    print("result>>",conn.rowcount)
    for data in data_all:
        print("Found | Id:", data[0], "| Name :", data[1], "\t| Price :", data[2], "| Amount :", data[3],"\t| Type :", data[6])
    if data_all == ():
        print(">>",input_search,"is Not Found !!")
    print("\n")
    db.close()

def search_price():
    db, conn = connect.connect_db()
    input_price1 = input("Input price (Start)  : ")
    input_price2 = input("Input price (Stop)  : ")
    if (input_price1 <= '0') or (input_price2 <= '0'):
        print("input price not correct !")
    else:
        sql = "select * from product,producttype where (product.productPrice Between %s AND %s) \
                AND (product.typeID = producttype.typeID) order by product.productPrice asc  "
        input_price =(input_price1,input_price2)
        conn.execute(sql,input_price)
        data_all = conn.fetchall()
        print("result>>",conn.rowcount)
        for data in data_all:
            print("Found | Price :", data[2], "| Id:", data[0], "| Name :", data[1], "\t| Amount :", data[3],"\t| Type :", data[6])
        if data_all == ():
            print(">>",input_search,"is Not Found !!")
            print("\n")
    db.close()

def search_type():
    db, conn = connect.connect_db()
    select.all_type()
    input_search = input("input typeID or typeName : ")
    sql = "select * from producttype,product where producttype.typeID = product.typeID and (product.typeID Like %s or producttype.typeName Like %s) "
    search=['%'+input_search+'%']
    keyword = (input_search,search)
    conn.execute(sql,keyword)
    data_all = conn.fetchall()
    if data_all != ():
        print("\n\tProduct in Type",input_search,">> result : ",conn.rowcount)
        for data in data_all:
            print("\tType :",data[1],"Id:", data[2], "Name :", data[3], "\tPrice :", data[4], "Amount :", data[5])
    if data_all == ():
        print(">> Error input not correct , Please try again")
    print("\n")
    db.close()
