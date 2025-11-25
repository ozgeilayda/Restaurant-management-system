from tables import initialize_tables, add_table, save_tables
from menu import load_menu
from orders import open_order, add_item_to_order
import os   # klasör var mı yok mu kontrol etmek için kullandım

DATA_DIR = "data"
TABLE_PATH = os.path.join(DATA_DIR, "tables.json")
MENU_PATH = os.path.join(DATA_DIR, "menu.json")

current_order = None   # week2: aktif bir sipariş tutmak için 

def prepare_data_folder(): # eğer data klasörü veya json dosyaları yoksa burada oluşturuyorum.
    if not os.path.exists(DATA_DIR):   
        os.makedirs(DATA_DIR)
        
    if not os.path.exists(TABLE_PATH):
        with open(TABLE_PATH, "w") as f:
            f.write("[]")

    if not os.path.exists(MENU_PATH):
        with open(MENU_PATH, "w") as f:
            f.write('{"items":{}}')


def show_menu(): #ana menü 
    print("\n---- Restaurant System (Week 1) ----")
    print("1 - List Tables")
    print("2 - Add Table")
    print("3 - Load Menu")
    print("4 - Exit")
    print("5 - Open Order")        #week2
    print("6 - Add Item To Order") #week2
    return input("Choice: ")


def list_tables(tables): #masaları ekrana listelemek için
    if len(tables) == 0:
        print("No tables yet.")   # hiç masa eklenmediyse bunu yazdırıyorum
        return
    for table in tables: # her masayı döngüyle yazdırıyorum
        print(f"Table {table['table_number']} | Capacity: {table['capacity']} | Status: {table['status']}")

def add_table_cli(tables):
    number = int(input("Table number: "))   # kullanıcıdan masa numarasını alır
    capacity = int(input("Capacity: "))       # kullanıcıdan masa kapasitesini alır

    #masa bilgisi
    table_data = {
        "table_number": number,
        "capacity": capacity,
        "server": "",
        "status": "free",
        "start_time": None
    }

    add_table(tables, table_data)   # tables.py'daki fonksiyonu çağırıyorum
    save_tables(TABLE_PATH, tables) # masayı kaydediyorum
    print("Table added.")           

def main():
    global current_order
    
    prepare_data_folder()   # önce data klasörünü kontrol ettirdim
    tables = initialize_tables(TABLE_PATH)   # masaları dosyadan yüklediö
    menu = load_menu(MENU_PATH)             # menüyü dosyadan yükledim

    while True:
        choice = show_menu()

        if choice == "1":
            list_tables(tables)
        elif choice == "2":
            add_table_cli(tables)
        elif choice == "3":
            print("Menu loaded. Item count:", len(menu["items"]))
        elif choice == "4":
            print("Goodbye.")
            break
        elif choice == "5":
             table_number = int(input("Table number for order: "))
             current_order = open_order(table_number)
             print("Order opened:", current_order)
        elif choice == "6":
            if current_order is None:
                print("No order open.")
            else:
                item_id = input("Menu item ID: ")

                if item_id in menu["items"]:
                    menu_item = menu["items"][item_id]
                    qty = int(input("Quantity: "))
                    add_item_to_order(current_order, menu_item, qty)
                    print("Item added.")
                else:
                    print("Item not found in menu.")
        
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
