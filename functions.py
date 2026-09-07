from db import get_connection
from datetime import date


def print_medicines(medicines, header_title="MEDICINE DETAILS"):
    for medicine in medicines:
        print(f"================== {header_title} ====================")
        print(f"Medicine ID : {medicine[0]}")
        print(f"Medicine Name : {medicine[1]}")
        print(f"Stock : {medicine[2]}")
        print(f"Price per unit : rs. {medicine[3]}")
        print(f"Expiry date : {medicine[4]}")
        print("========================================================")

def print_prescriptions(prescriptions):
    for rx in prescriptions:
        print("================ PRESCRIPTION DETAILS ================")
        print(f"Prescription ID : {rx[0]}")
        print(f"Patient Name : {rx[1]}")
        print(f"Medicine ID : {rx[2]}")
        print(f"Quantity Dispensed : {rx[3]}")
        print(f"Total Cost : rs. {rx[4]}")
        print(f"Issue Date : {rx[5]}")
        print("========================================================")


def view_inventory():
    connection = get_connection()
    query = "select * from inventory"
    cursor = connection.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    print_medicines(res, "INVENTORY DETAILS")
    cursor.close()
    connection.close()

def issue_prescription():
    patient_name = input("Enter Patient Name: ")
    med_id = int(input("Enter Medicine ID: "))
    quantity = int(input("Enter Quantity: "))

    connection = get_connection()
    cursor = connection.cursor()
    
   
    query = "select * from inventory where med_id = %s"
    cursor.execute(query, (med_id,))
    medicine = cursor.fetchone()

    if medicine is None:
        print("Medicine ID not found!")
        cursor.close()
        connection.close()
        return

    m_name = medicine[1]
    m_stock = medicine[2]
    m_price = medicine[3]
    m_expiry = medicine[4]

    
    if m_expiry <= date.today():
        print(f"Cannot dispense! {m_name} is expired.")
        cursor.close()
        connection.close()
        return

    
    if m_stock < quantity:
        print(f"Insufficient stock! Only {m_stock} available.")
        cursor.close()
        connection.close()
        return

    total_cost = m_price * quantity

    update_query = "update inventory set stock = stock - %s where med_id = %s"
    cursor.execute(update_query, (quantity, med_id))

   
    insert_query = "insert into prescriptions (patient_name, med_id, quantity_dispensed, total_cost) values (%s, %s, %s, %s)"
    cursor.execute(insert_query, (patient_name, med_id, quantity, total_cost))

    connection.commit()
    print("Prescription issued successfully!!!")
    print(f"Total Bill: rs. {total_cost}")

    cursor.close()
    connection.close()

def check_low_stock():
    threshold = 10
    connection = get_connection()
    query = "select * from inventory where stock <= %s"
    cursor = connection.cursor()
    cursor.execute(query, (threshold,))
    res = cursor.fetchall()
    
    if len(res) == 0:
        print("All medicines are sufficiently stocked!")
    else:
        print_medicines(res, "LOW STOCK WARNING")

    cursor.close()
    connection.close()

def check_expired_stock():
    connection = get_connection()
    today = date.today()
    query = "select * from inventory where expiry_date <= %s"
    cursor = connection.cursor()
    cursor.execute(query, (today,))
    res = cursor.fetchall()

    if len(res) == 0:
        print("No expired medicines found.")
    else:
        print_medicines(res, "EXPIRED MEDICINE WARNING")

    cursor.close()
    connection.close()

def view_prescriptions():
    connection = get_connection()
    query = "select * from prescriptions"
    cursor = connection.cursor()
    cursor.execute(query)
    res = cursor.fetchall()

    if len(res) == 0:
        print("No prescription records found.")
    else:
        print_prescriptions(res)

    cursor.close()
    connection.close()

def create_medicine_in_db():
    med_name = input("Enter medicine name: ")
    stock = int(input("Enter initial stock: "))
    unit_price = float(input("Enter price per unit: "))
    expiry_date = input("Enter expiry date (YYYY-MM-DD): ").strip().replace(" ", "")

    connection = get_connection()
    query = "insert into inventory (med_name, stock, unit_price, expiry_date) values (%s, %s, %s, %s)"
    cursor = connection.cursor()
    cursor.execute(query, (med_name, stock, unit_price, expiry_date))
    connection.commit()
    
    print("Medicine added to inventory successfully!!!!")
    cursor.close()
    connection.close()

def restock_medicine_in_db():
    med_id = int(input("Enter Medicine ID to restock: "))
    add_stock = int(input("Enter quantity to add: "))

    connection = get_connection()
    query = "update inventory set stock = stock + %s where med_id = %s"
    cursor = connection.cursor()
    cursor.execute(query, (add_stock, med_id))
    connection.commit()
    
    print("Stock updated successfully!!!!")
    cursor.close()
    connection.close()

def delete_medicine_from_db():
    med_id = int(input("Enter Medicine ID to delete: "))
    
    connection = get_connection()
    query = "delete from inventory where med_id = %s"
    cursor = connection.cursor()
    cursor.execute(query, (med_id,))
    connection.commit()
    
    print("Medicine deleted from inventory successfully!!!!")
    cursor.close()
    connection.close()

def search_medicine_by_name():
    name = input("Enter medicine name to search: ")
    
    connection = get_connection()
    query = "select * from inventory where med_name like %s"
    cursor = connection.cursor()
    cursor.execute(query, (f"%{name}%",))
    res = cursor.fetchall()
    
    if len(res) == 0:
        print("No matching medicines found!")
    else:
        print_medicines(res, "SEARCH RESULT")
        
    cursor.close()
    connection.close()

def get_total_sales_report():
    connection = get_connection()
    query = "select count(*), sum(total_cost) from prescriptions"
    cursor = connection.cursor()
    cursor.execute(query)
    res = cursor.fetchone()
    
    total_prescriptions = res[0]
    total_revenue = res[1] if res[1] else 0.0
    
    print("\n================ FINANCIAL SUMMARY ================")
    print(f"Total Prescriptions Issued : {total_prescriptions}")
    print(f"Total Revenue Generated    : rs. {total_revenue}")
    print("===================================================")
    
    cursor.close()
    connection.close()

def update_medicine_price():
    med_id = int(input("Enter Medicine ID: "))
    new_price = float(input("Enter new price per unit: "))
    
    connection = get_connection()
    query = "update inventory set unit_price = %s where med_id = %s"
    cursor = connection.cursor()
    cursor.execute(query, (new_price, med_id))
    connection.commit()
    
    print("Medicine price updated successfully!!!!")
    cursor.close()
    connection.close()