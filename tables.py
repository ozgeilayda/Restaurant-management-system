
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
