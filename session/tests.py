price = 100
session_discount_percentage = 10
number_discount = 10
profit_percantage = 2
company_discount = 10
final_price = (((100-session_discount_percentage-number_discount)/100) * price ) * ((100-company_discount)/100)

sportclub_portion = ((100-session_discount_percentage-profit_percantage-number_discount)/100) * price

company_portion = final_price - sportclub_portion

print('final_price: ',final_price,'sportclub_portion: ',sportclub_portion,'company_portion ',company_portion)
