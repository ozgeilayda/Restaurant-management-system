
import json 

def initialize_tables(path: str) -> list: #dodyayı okuyup masa listesine çeviriyorum
    try:
        with open(path, "r") as file: #dosyayı okuma modunda açıyorum
            tables = json.load(file) # json -> python listesine çeviriyorum
            return tables 
    except:
        return [] # dosya yoksa veya hatalıysa boş liste 
        
def add_table(tables:list, table_data: dict) -> list: 
    tables.append(table_data) #listeye yeni masa ekliyorum 
    return tables
    
def save_tables(path: str,tables: list) -> None #masayı kaydetmek için 
    with open(path, "w") as file:
        json.dump(tables, file) 

def assign_table(tables: list, table_number: int, party_size: int): #masayı dolu olarak atamak için
    for table in tables:
        if table["table_number"] == table_number and table["capacity"] >= party_size:
            table["status"] = "occupied"
            return table
    return None

def release_table(tables: list, table_number: int) -> bool: #masayı boşaltmak için
    for table in tables:
        if table["table_number"] == table_number:
            table["status"] = "free"
            return True
    return False 

def update_server(tables: list, table_number: int, server_name: str): #masaya garson atamak için
    for table in tables:
        if table["table_number"] == table_number:
            table["server"] = server_name
            return table
    return None 

