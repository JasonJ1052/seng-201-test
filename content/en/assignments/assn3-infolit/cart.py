def calculate_cart_total(cart_items, tax_rate):
    """Calculate total cart cost including tax."""
    subtotal = sum(item["price"] * item["quantity"] for item in cart_items)
    return subtotal + (subtotal * tax_rate)

def display_cart_summary(cart_items, tax_rate):
    """Display a summary of the cart."""
    total_cost = calculate_cart_total(cart_items, tax_rate)
    print(f"Total cost (including tax): ${total_cost:.2f}")

def main():
    """Main function to simulate a shopping cart."""
    cart = [
        {"name": "Laptop", "price": 1000.0, "quantity": 1.0},
        {"name": "Headphones", "price": 200.0, "quantity": 2.0},
        {"name": "Mouse", "price": 50.0, "quantity": 1.0},
        {"name": "Keyboard", "price": 150.0, "quantity": 1.0},
        {"name": "Monitor", "price": 300.0, "quantity": 1.0},
        {"name": "HDMI Cable", "price": 10.0, "quantity": 2.0},
        {"name": "USB Drive", "price": "20.0", "quantity": 3.0},
        {"name": "External Hard Drive", "price": 100.0, "quantity": 1.0},
    ]
    tax_rate = 0.07  # 7% sales tax
    display_cart_summary(cart, tax_rate)

if __name__ == "__main__":
    main()
