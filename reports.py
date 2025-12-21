# Bu dosya rapor almak için 

#toplam kaç sipariş var
def total_order_count(orders):
    return len(orders)
    
#toplam ciroyu hesaplama
def total_revenue(orders):
    total = 0
    for order in orders:
        total += order.get("total", 0)
    return total
