import json

def load_menu(path: str) -> dict:
    try:
        with open (path, "r") as file:
            menu = json.load(file)
            return menu # dosya varsa menü dönüyor
    except:
        return {"items": {} } #dosya yoksa boş bir menu dict oluşturuyor
    
def save_menu(path: str, menu: dict) -> None: #menüde değişiklik olursa kaydetmek için 
    with open (path, "w") as file:
        json.dump(menu, file, indent=4)

def add_menu_item(menu: dict, item_id: str, item_data: dict): #masaya yeni bir ürün eklemek için
    menu["items"][item_id] = item_data  #item_data ürün bilgilerini tutan sözlük
    return menu

def update_menu_item(menu: dict, item_id: str, new_data: dict): #var olan menü ürününü güncellemek için fiyat değişirse veya ürün aktif/pasif olursa
    if item_id in menu["items"]:                              
        menu["items"][item_id].update(new_data)
        return True
    return False

def filter_menu(menu: dict, category: str): #menüdeki ürünleri kategoriye göre filtrelemek için
    result = {}
    for item_id, item in menu["items"].items():
        if item.get("category") == category:
            result[item_id] = item
    return result
