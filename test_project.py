# bu dosya projedeki bazı temel fonksiyonları test etmek için

from orders import calculate_bill

def test_calculate_bill(): #hesaplama fonksiyonu doğru çalışıyor mu kontrolü için
    order = {"items": [{"price": 10, "qty": 2}]}
    bill = calculate_bill(order, 0.1, 0.1)
    assert bill["total"] == 24

def test_split_bill(): #faturayı eşit bölüp bölmediğini kontrol etmek için
    assert split_bill(100,4) == 25

def test_split_bill_invalid(): #geçersiz bir kişi sayısı girildiğinde hata vermeden None döndürmesini kontrol etmek için
    assert split_bill(100,0) is None 
