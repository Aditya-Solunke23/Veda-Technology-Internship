
print("================================================")
print("             SHOPPING BILL GENERATOR")
print("================================================")


def calculate_subtotal(products):
    subtotal = 0
    for product in products:
        subtotal += product["quantity"] * product["price"]
    return subtotal


def calculate_discount(subtotal, discount_rate):
    return subtotal * discount_rate / 100


def calculate_tax(amount, tax_rate):
    return amount * tax_rate / 100


def display_bill(products, subtotal, discount, tax, total):
    print("\n" + "=" * 60)
    print("                    SHOPPING BILL")
    print("=" * 60)
    print(f"{'Product':<20}{'Qty':>5}{'Price':>12}{'Amount':>12}")
    print("-" * 60)

    for product in products:
        amount = product["quantity"] * product["price"]
        print(
            f"{product['name']:<20}"
            f"{product['quantity']:>5}"
            f"{product['price']:>12.2f}"
            f"{amount:>12.2f}"
        )

    print("-" * 60)
    print(f"{'Subtotal:':>43} Rs. {subtotal:>8.2f}")
    print(f"{'Discount:':>43} Rs. {discount:>8.2f}")
    print(f"{'Tax:':>43} Rs. {tax:>8.2f}")
    print("=" * 60)
    print(f"{'FINAL AMOUNT:':>43} Rs. {total:>8.2f}")
    print("=" * 60)


products = []

try:
    number_of_products = int(input("\nEnter the number of products: "))

    if number_of_products <= 0:
        print("Error: Enter at least one product.")
    else:
        for i in range(number_of_products):
            print(f"\nProduct {i + 1}")

            name = input("Enter product name: ").strip()
            if not name:
                raise ValueError("Product name cannot be empty.")

            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item (Rs.): "))

            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")

            if price < 0:
                raise ValueError("Price cannot be negative.")

            products.append({
                "name": name,
                "quantity": quantity,
                "price": price
            })

        subtotal = calculate_subtotal(products)

        discount_rate = float(
            input("\nEnter discount percentage (0-100): ")
        )
        tax_rate = float(input("Enter tax percentage (0-100): "))

        if not 0 <= discount_rate <= 100:
            raise ValueError("Discount must be between 0 and 100.")

        if not 0 <= tax_rate <= 100:
            raise ValueError("Tax must be between 0 and 100.")

        discount = calculate_discount(subtotal, discount_rate)
        taxable_amount = subtotal - discount
        tax = calculate_tax(taxable_amount, tax_rate)
        total = taxable_amount + tax

        display_bill(products, subtotal, discount, tax, total)

except ValueError as error:
    print(f"\nError: {error}")
