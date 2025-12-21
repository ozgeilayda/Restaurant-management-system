# bu dosya projedeki bazı temel fonksiyonları test etmek için

from orders import calculate_bill

def test_calculate_bill_simple():
    order = {"items": [{"price": 10, "qty": 2}, {"price": 5, "qty": 1}] }
    bill = calculate_bill(order, 0.1, 0.1)
    
    assert bill["subtotal"] == 25
    
    assert bill["tax"] == 2.5 
    
    assert bill["tip"] == 2.5 
    
    assert bill["total"] == 30
