import json

def load_menu(path: str) -> dict:
    try:
        with open (path, "r") as file:
            menu = json.load(file)
            return menu # dosya varsa menü dönüyor
    except:
        return {"items": {} } #dosya yoksa boş bir menu dict oluşturuyor
    
def save_menu(path,menu): #menüde değişiklik olursa kaydetmek için 
    with open (path, "w") as file:
        json.dump(menu, file,)
