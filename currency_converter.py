currency = {
    "USD" : 1,
    "EUR": 0.92,
    "INR": 83.15,
    "JPY": 150.75,
    "NPR": 132.55,
    "AUD": 1.52 
}

amt = float(input("Enter the amount:"))
source = input("From currency(NPR, INR, USD, AUD, EUR, JPY):").upper()
target = input("To currency(NPR, INR, USD, AUD, EUR, JPY):").upper()
if source not in currency or target not in currency:
    print("Not valid currency!")
else:
    if source == "USD":
        result = amt * currency[target]
    else:
        usd = amt / currency[source]
        result = usd * currency[target]
    print(f"{source} {amt} = {target} {result}")
