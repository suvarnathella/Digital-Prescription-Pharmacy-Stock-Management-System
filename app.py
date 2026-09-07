from functions import (
    view_inventory,
    issue_prescription,
    check_low_stock,
    check_expired_stock,
    view_prescriptions,
    create_medicine_in_db,
    restock_medicine_in_db,
    search_medicine_by_name,
    update_medicine_price,
    delete_medicine_from_db,
    get_total_sales_report
)


print("\n=== PHARMACY MANAGEMENT SYSTEM ===")
print("1. View All Inventory")
print("2. Issue Digital Prescription")
print("3. Check Low Stock Items")
print("4. Check Expired Medicines")
print("5. View Prescription History")
print("6. Add New Medicine to Inventory")
print("7. Restock Existing Medicine")
print("8. Search Medicine by Name")
print("9. Update Medicine Price")
print("10. Delete Medicine from Inventory")
print("11. View Total Revenue & Sales Report")
print("12. Exit")


while True:
    choice = input("Enter choice (1-12): ").strip()

    if choice == '1':
        view_inventory()
    elif choice == '2':
        issue_prescription()
    elif choice == '3':
        check_low_stock()
    elif choice == '4':
        check_expired_stock()
    elif choice == '5':
        view_prescriptions()
    elif choice == '6':
        create_medicine_in_db()
    elif choice == '7':
        restock_medicine_in_db()
    elif choice == '8':
        search_medicine_by_name()
    elif choice == '9':
        update_medicine_price()
    elif choice == '10':
        delete_medicine_from_db()
    elif choice == '11':
        get_total_sales_report()
    elif choice == '12':
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice, please select 1 to 12.")
