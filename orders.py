from datetime import datetime

def open_order(table_number:int) -> dict: # yeni bir sipariş oluşturuyor.
    order = {
        "table_number": table_number,
        "items": [],   # siparişteki ürünler burada tutulacak
        "opened_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return order


#siparişe ürün eklemek için
#menu_item bir dict olacak
def add_item_to_order(order: dict, menu_item: dict, quantity: int, note: str = "") -> dict:
    item = {
        "id": menu_item["id"],      # ürünün id'si
        "name": menu_item["name"],  # ürün adı
        "price": menu_item["price"],
        "qty": quantity,
        "status": "ordered",        # ürünün durumu
        "note": note
    }

    order["items"].append(item)    # item'i sipariş listesine ekliyorum
    return order


#siparişten ürün silmek için
def remove_item_from_order(order: dict, item_id: str) -> dict:
    new_list = []
    for it in order["items"]:
        if it["id"] != item_id:   # aynı id değilse yeni listeye ekliyorum
            new_list.append(it)

    order["items"] = new_list
    return order


#durumunu güncellemek için 
def update_item_status(order: dict, item_id: str, status: str) -> dict:
    for it in order["items"]:
        if it["id"] == item_id:
            it["status"] = status   # durumunu değiştiriyorum
    return order
