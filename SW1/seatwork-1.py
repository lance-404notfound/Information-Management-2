def dollar_to_other_currencies(usd):
    rate_inr = 83.50
    rate_gbp = 0.76
    rate_cny = 7.30

    rupee = usd * rate_inr
    pound = usd * rate_gbp
    yuan = usd * rate_cny

    return rupee, pound, yuan


stop = False
while not stop:
    dollars_input = input("Enter Dollar values (use @ to separate, * to exit): ")

    if dollars_input == "*":
        print("Exiting Program... Goodbye!")
        stop = True
    else:
        dollar_list = dollars_input.split("@")
        print("\n$ (USD)\t\tRupee (INR)\tPound (GBP)\tYuan (CNY)")

        for value in dollar_list:
            try:
                value = float(value)
                r, p, y = dollar_to_other_currencies(value)
                print(f"{value:8.2f}\t{r:10.2f}\t{p:10.2f}\t{y:10.2f}")
            except ValueError:
                print(f"'{value}' is not a valid number, skipping...")

        print("-" * 50)
