
# currency_converter.py

# Static exchange rates (for simplicity)
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'JPY': 110.0,
    'GBP': 0.75,
    'AUD': 1.35,
    'CAD': 1.25,
    'CHF': 0.92,
    'CNY': 6.45,
    'SEK': 8.6,
    'NZD': 1.4
}

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Invalid currency code")
    amount_in_usd = amount / rates[from_currency]
    return amount_in_usd * rates[to_currency]

if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    from_currency = input("Enter from currency (e.g., USD): ").upper()
    to_currency = input("Enter to currency (e.g., EUR): ").upper()

    try:
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(e)
