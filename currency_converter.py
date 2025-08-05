def convert_currency(amount, from_currency, to_currency):
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.91,
        "INR": 83.2,
        "BDT": 119.5
    }

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Currency not supported."

    usd_amount = amount / exchange_rates[from_currency]
    converted_amount = usd_amount * exchange_rates[to_currency]
    return round(converted_amount, 2)

print(convert_currency(100, "USD", "BDT"))
print(convert_currency(500, "BDT", "EUR"))
