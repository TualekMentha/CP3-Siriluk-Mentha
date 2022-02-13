def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result
price = int(input("price:"))
print(vatCalculate(price))
