from jb_60.function_example.utilitis import utilitis

utilitis_1=utilitis()

price_1 = "27$"
price_2 = "33$"
price_3 = "44$"
price_4 = 40.0
rate=3.4

new_price_1 = utilitis_1.getting_vat(price_1)
new_price_2 = utilitis_1.getting_vat(price_2)
new_price_3 = utilitis_1.getting_vat(price_3)
utilitis_1.add_suffix(new_price_1,rate=3.4)
utilitis_1.add_suffix(new_price_2,rate=3.4)
utilitis_1.add_suffix(new_price_3,rate=3.4)
utilitis_1.add_suffix(price_4,rate=4.1)


print("test end")

#find VAT (18%) per each price
#convert it to ILS

