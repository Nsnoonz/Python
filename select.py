import connect
def show_data():
    try:
        run_out()
        while True:
            print("\n Menu")
            print("[1] All Product")
            print("[2] Product Name")
            print("[3] All  Type")
            print("[4] Product Type")
            print("[5] Product Almost ran out")
            print("[6] Exit")
            input_choice = int(input("Choose Data  : "))
            if (input_choice == 1):
                show_product()
            elif (input_choice == 2):
                show_productName()
            elif (input_choice == 3):
                all_type()
            elif (input_choice == 4):
                show_Type()
            elif (input_choice == 5):
                run_out()
            elif (input_choice ==6):
                break
            else:
                print("\n>>> Please input number 1-6 !!!\n")
    except:
        print("\n>>> Error Please input number 1-6 !!!\n")
        show_data()

def show_product():
    db, conn = connect.connect_db()
    sql = "SELECT * FROM product, producttype WHERE product.typeID = producttype.typeID order by productID"
    conn.execute(sql)
    data_all = conn.fetchall()
    print("-"*30,"All Product","-"*30)
    for data in data_all:
        print("Id:", data[0], "| Name :", data[1], "\t| Price :", data[2], "| Amount :", data[3],"\t| Type :", data[6])
    print("-"*73)
    db.close()
    
def show_productName():
    db, conn = connect.connect_db()
    sql = "SELECT * FROM product order by productName "
    conn.execute(sql)
    data_all = conn.fetchall()
    print("-"*30,"Product Name","-"*30)
    for data in data_all:
        print( "Name :", data[1])
    print("-"*74)
    db.close()

def all_type():
    db, conn = connect.connect_db()
    sql = "SELECT * FROM producttype order by typeID "
    conn.execute(sql)
    data_all = conn.fetchall()
    print("-"*30,"All Type","-"*30)
    for data in data_all:
        print( "ID :",data[0],"Name :", data[1])
    print("-"*74)
    db.close()

def show_Type():
    db, conn = connect.connect_db()
    sql = "SELECT * From producttype,product WHERE producttype.typeID = product.typeID ORDER BY producttype.typeID "
    conn.execute(sql)
    data_all = conn.fetchall()
    i = []
    print("-"*30,"Product Type","-"*30)
    for data in data_all:
        if i != data[1]:
            print("\n\tID:",data[0],"Type:",data[1])
            i = data[1]
        print("\tId:", data[2], "Name :", data[3], "\tPrice :", data[4], "Amount :", data[5])
    print("-"*74)
    db.close()

def run_out():
    db, conn = connect.connect_db()
    sql = "SELECT * FROM product WHERE productAmount<=5"
    conn.execute(sql)
    data_all = conn.fetchall()
    print("="*40)
    print(">>> Warning !! Product Almost ran out")
    for data in data_all:
        print("Id:", data[0], "| Name :", data[1], "\t| Among :", data[3])
    print("="*40)
    db.close()
