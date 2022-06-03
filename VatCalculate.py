print("-----------------------------------------")
print("       Welcome to Purit's Shop")
print("-----------------------------------------")
price = input("เมื่อซื้อสินค้าในราคา (THB) : ")
vat = float(price) * (7/100)
total = float(price) + vat
print("ราคาเมื่อรวมภาษีแล้ว :", total, "THB")
