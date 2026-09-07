💊 Digital Prescription & Pharmacy Stock Management System

A Python and MySQL-based Pharmacy Management System designed to digitize prescription handling and efficiently manage medicine inventory, stock levels, expiry dates, sales, and pharmacy records.

The system provides a simple command-line interface (CLI) through which pharmacy staff can manage medicines, issue digital prescriptions, monitor stock, and generate sales summaries.

📌 Project Overview

Managing pharmacy inventory manually can lead to problems such as stock shortages, expired medicines, incorrect billing, and difficulty maintaining prescription records.

The Digital Prescription & Pharmacy Stock Management System addresses these challenges by integrating prescription management with a centralized pharmacy inventory database.

When a prescription is issued, the system automatically:

Validates the medicine
Checks its expiry status
Checks available stock
Calculates the total cost
Deducts the dispensed quantity from inventory
Stores the prescription record

This creates a more organized and reliable pharmacy management workflow.

✨ Features


🏥 Prescription Management
Issue digital prescriptions
Store patient name and prescription details
Record medicine quantity dispensed
Automatically calculate prescription cost
View prescription history


💊 Medicine Inventory Management
View all medicines
Add new medicines
Restock existing medicines
Search medicines by name
Update medicine prices
Delete medicines from inventory


⚠️ Stock & Expiry Monitoring
Identify medicines with low stock
Detect expired medicines
Prevent dispensing of expired medicines
Prevent dispensing when sufficient stock is unavailable

The system uses a low-stock threshold of 10 units for inventory monitoring.

📊 Sales & Revenue Reporting
Calculate total prescriptions issued
Calculate total revenue generated
Display a financial summary

The sales report is generated directly from prescription records using the total prescription count and accumulated prescription cost.

🛠️ Tech Stack

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| **Python**       | Application logic and CLI      |
| **MySQL**        | Database management            |
| **PyMySQL**      | Python-MySQL connectivity      |
| **SQL**          | Data manipulation and querying |
| **Git & GitHub** | Version control                |


🏗️ Project Structure
Digital-Prescription-Pharmacy-Stock-Management/
│
├── app.py
├── functions.py
├── db.py
└── README.md

app.py

Acts as the main entry point of the application.

It provides the command-line menu and calls the appropriate functionality based on the user's selection.

functions.py

Contains the core application functionality, including:

Inventory management
Prescription issuing
Stock checking
Expiry checking
Medicine searching
Restocking
Price updating
Prescription history
Revenue reporting
db.py

Handles the connection between Python and MySQL using PyMySQL. The application connects to the pharmacy_db database.

🔄 System Workflow


             ┌──────────────────────┐
             │       Start App      │
             └──────────┬───────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │    Main Menu / CLI   │
             └──────────┬───────────┘
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
   Inventory       Prescription     Reports & Alerts
   Management       Management
        │               │                │
        ▼               ▼                ▼
   Add / Search     Validate Stock    Low Stock
   Restock          Check Expiry      Expired Stock
   Update Price     Calculate Bill    Revenue Report
   Delete           Deduct Stock
        │               │
        └───────────────┼────────────────┘
                        ▼
                ┌──────────────┐
                │ MySQL Database│
                └──────────────┘


🗄️ Database

The application uses MySQL as its backend database.

Main Tables
inventory

Stores medicine information such as:

Medicine ID
Medicine name
Available stock
Unit price
Expiry date

The application retrieves and manages inventory records directly from the inventory table.

prescriptions

Stores prescription transaction details such as:

Prescription ID
Patient name
Medicine ID
Quantity dispensed
Total cost
Issue date

💻 Application Menu
=== PHARMACY MANAGEMENT SYSTEM ===

1. View All Inventory
2. Issue Digital Prescription
3. Check Low Stock Items
4. Check Expired Medicines
5. View Prescription History
6. Add New Medicine to Inventory
7. Restock Existing Medicine
8. Search Medicine by Name
9. Update Medicine Price
10. Delete Medicine from Inventory
11. View Total Revenue & Sales Report
12. Exit
These are the current operations implemented in the application.

🧾 Prescription Processing

When issuing a prescription, the system follows these steps:
Enter Patient Name
        ↓
Enter Medicine ID
        ↓
Enter Quantity
        ↓
Check Medicine Exists
        ↓
Check Expiry Date
        ↓
Check Available Stock
        ↓
Calculate Total Cost
        ↓
Deduct Quantity from Inventory
        ↓
Store Prescription
        ↓
Display Total Bill

The system refuses to dispense a medicine if it is expired or if the requested quantity exceeds available stock.

📈 Revenue Calculation

The system generates a financial summary containing:
Total Prescriptions Issued
Total Revenue Generated

Revenue is calculated from the total cost stored in prescription records.

💊 Digital Prescription & Pharmacy Stock Management System

A Python and MySQL-based Pharmacy Management System designed to digitize prescription handling and efficiently manage medicine inventory, stock levels, expiry dates, sales, and pharmacy records.

The system provides a simple command-line interface (CLI) through which pharmacy staff can manage medicines, issue digital prescriptions, monitor stock, and generate sales summaries.

📌 Project Overview

Managing pharmacy inventory manually can lead to problems such as stock shortages, expired medicines, incorrect billing, and difficulty maintaining prescription records.

The Digital Prescription & Pharmacy Stock Management System addresses these challenges by integrating prescription management with a centralized pharmacy inventory database.

When a prescription is issued, the system automatically:

Validates the medicine
Checks its expiry status
Checks available stock
Calculates the total cost
Deducts the dispensed quantity from inventory
Stores the prescription record

This creates a more organized and reliable pharmacy management workflow.

✨ Features

🏥 Prescription Management
Issue digital prescriptions
Store patient name and prescription details
Record medicine quantity dispensed
Automatically calculate prescription cost
View prescription history

💊 Medicine Inventory Management
View all medicines
Add new medicines
Restock existing medicines
Search medicines by name
Update medicine prices
Delete medicines from inventory

⚠️ Stock & Expiry Monitoring
Identify medicines with low stock
Detect expired medicines
Prevent dispensing of expired medicines
Prevent dispensing when sufficient stock is unavailable

The system uses a low-stock threshold of 10 units for inventory monitoring.

📊 Sales & Revenue Reporting
Calculate total prescriptions issued
Calculate total revenue generated
Display a financial summary

The sales report is generated directly from prescription records using the total prescription count and accumulated prescription cost.

🛠️ Tech Stack
| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| **Python**       | Application logic and CLI      |
| **MySQL**        | Database management            |
| **PyMySQL**      | Python-MySQL connectivity      |
| **SQL**          | Data manipulation and querying |
| **Git & GitHub** | Version control                |


🏗️ Project Structure
Digital-Prescription-Pharmacy-Stock-Management/
│
├── app.py
├── functions.py
├── db.py
└── README.md

app.py

Acts as the main entry point of the application.

It provides the command-line menu and calls the appropriate functionality based on the user's selection.

functions.py

Contains the core application functionality, including:

Inventory management
Prescription issuing
Stock checking
Expiry checking
Medicine searching
Restocking
Price updating
Prescription history
Revenue reporting
db.py

Handles the connection between Python and MySQL using PyMySQL. The application connects to the pharmacy_db database.

🔄 System Workflow 


             ┌──────────────────────┐
             │       Start App      │
             └──────────┬───────────┘
                        │
                        ▼
             ┌──────────────────────┐
             │    Main Menu / CLI   │
             └──────────┬───────────┘
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
   Inventory       Prescription     Reports & Alerts
   Management       Management
        │               │                │
        ▼               ▼                ▼
   Add / Search     Validate Stock    Low Stock
   Restock          Check Expiry      Expired Stock
   Update Price     Calculate Bill    Revenue Report
   Delete           Deduct Stock
        │               │
        └───────────────┼────────────────┘
                        ▼
                ┌──────────────┐
                │ MySQL Database│
                └──────────────┘


🗄️ Database

The application uses MySQL as its backend database.

Main Tables
inventory

Stores medicine information such as:

Medicine ID
Medicine name
Available stock
Unit price
Expiry date

The application retrieves and manages inventory records directly from the inventory table.

prescriptions

Stores prescription transaction details such as:

Prescription ID
Patient name
Medicine ID
Quantity dispensed
Total cost
Issue date

💻 Application Menu
=== PHARMACY MANAGEMENT SYSTEM ===

1. View All Inventory
2. Issue Digital Prescription
3. Check Low Stock Items
4. Check Expired Medicines
5. View Prescription History
6. Add New Medicine to Inventory
7. Restock Existing Medicine
8. Search Medicine by Name
9. Update Medicine Price
10. Delete Medicine from Inventory
11. View Total Revenue & Sales Report
12. Exit
These are the current operations implemented in the application.

🧾 Prescription Processing

When issuing a prescription, the system follows these steps:
Enter Patient Name
        ↓
Enter Medicine ID
        ↓
Enter Quantity
        ↓
Check Medicine Exists
        ↓
Check Expiry Date
        ↓
Check Available Stock
        ↓
Calculate Total Cost
        ↓
Deduct Quantity from Inventory
        ↓
Store Prescription
        ↓
Display Total Bill

The system refuses to dispense a medicine if it is expired or if the requested quantity exceeds available stock.

📈 Revenue Calculation

The system generates a financial summary containing:
Total Prescriptions Issued
Total Revenue Generated

Revenue is calculated from the total cost stored in prescription records.

🎯 Project Objectives

The main objectives of this project are:

Digitize pharmacy prescription management
Maintain centralized medicine inventory
Reduce manual stock-management errors
Prevent dispensing of expired medicines
Monitor low-stock medicines
Maintain prescription transaction history
Automate billing calculations
Generate basic pharmacy revenue reports

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/Digital-Prescription-Pharmacy-Stock-Management.git

Navigate to the project directory:

cd Digital-Prescription-Pharmacy-Stock-Management
2. Install Required Package

Install PyMySQL:

pip install pymysql
3. Configure MySQL

Create the database:

CREATE DATABASE pharmacy_db;

Create the required inventory and prescriptions tables according to the fields used by the application.

4. Configure Database Connection

Update the MySQL connection details in db.py.

connection = connect(
    host='localhost',
    user='root',
    password='YOUR_PASSWORD',
    database='pharmacy_db'
)
5. Run the Application
python app.py
🚀 Future Enhancements

The project can be further enhanced with:

🔐 User authentication and role-based access
🖥️ Web-based interface
👨‍⚕️ Doctor management
👤 Patient management
📄 Prescription PDF generation
🔔 Automatic low-stock notifications
📅 Expiry-date alerts
📊 Advanced sales dashboards
📈 Monthly and yearly sales analytics
🧾 Invoice generation
🔍 Advanced medicine filtering
☁️ Cloud database integration
🧠 Key Concepts Demonstrated

This project demonstrates practical knowledge of:

Python Programming
SQL
MySQL
PyMySQL
CRUD Operations
Database Connectivity
Functions & Modular Programming
Inventory Management
Transaction Processing
Input Validation
Business Logic
👩‍💻 Author

Suvarna

B.Tech – Computer Science & Engineering (AI & ML)
