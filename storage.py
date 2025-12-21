import json
import os

# Bu dosya, programdaki bilgileri json dosyalarına kaydetmek için.

# Siparişleri orders.json dosyasına kaydeden fonksiyon
def save_orders(data_dir, orders):
   path = os.path.join(data_dir, "orders.json")

   with open(path, "w") as file:
       json.dump(orders, file, indent=4)

# Siparişleri dosyadan tekrar yüklemek için fonksiyon
def load_orders(data_dir):
   path = os.path.join(data_dir, "orders.json")

   try:
       with open(path, "r") as file:
           orders = json.load(file)
           return orders
   except:
       return []   # dosya yoksa boş liste dönsün
