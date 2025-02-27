dollar_amount = float(input("How much dollar do you have? "))

currency_data = {}
with open("ACT4\currency.csv", "r") as file:
    lines = file.readlines()[1:]  
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 3: 
            code, name, value = parts
            try:
                currency_data[code] = float(value)
            except ValueError:
                continue 

print("Available currencies:")
count = 0
for key in currency_data:
    print(f"{key:10}", end=' ')
    count += 1
    if count % 10 == 0:
        print()
if count % 10 != 0:
    print()

currency = input("What currency do you want to have? ").strip().upper()

if currency in currency_data:
    converted_amount = dollar_amount * currency_data[currency]
    print(f"\nDollar: {dollar_amount} USD")
    print(f"{currency}: {converted_amount}")
else:
    print("Currency not found in the exchange rate list.")
