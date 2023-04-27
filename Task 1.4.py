#Task 1.4

VAT = 0.2

#Users to input the price in pounds of the item without VAT
priceNoVAT = float(input("Please enter the price in pounds of the item without VAT: "))

#Define VAT and price with VAT variable.
VATprice = 0.2*priceNoVAT
priceWithVAT = priceNoVAT + VATprice

#print the VAT 
print("VAT:",VATprice)

#print item price inc VAT
print("Item price inc VAT: %.2f"% priceWithVAT)
