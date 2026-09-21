# -----------------------------------------------------------------
#                    Parts 1 and 2:
# -----------------------------------------------------------------
# .strip() removes extra spaces, .title() capitalizes names, .lower() makes text lowercase
customer_name = input("Enter your name: ").strip().title()
membership_level = input("Enter your membership level (standard, silver, gold): ").strip().lower()
order_text = input("Enter your order total in whole dollars: ").strip()   # still text for now
coupon_response = input("Do you have a coupon? (yes/no): ").strip().lower()

# -----------------------------------------------------------------
#                    Part 3: Boolean checks (True or False)
# -----------------------------------------------------------------
name_valid = customer_name != ""
membership_valid = membership_level in ["standard", "silver", "gold"]
order_valid = order_text.isdigit()
coupon_valid = coupon_response in ["yes", "no"]

# -----------------------------------------------------------------
#                    Part 4: validate, then pick the discount
# -----------------------------------------------------------------
if not name_valid:
    print("Error: name cannot be empty.")
elif not membership_valid:
    print("Error: membership must be standard, silver, or gold.")
elif not order_valid:
    print("Error: order total must be a whole number.")
elif not coupon_valid:
    print("Error: coupon must be yes or no.")
else:
    # Everything is valid, so it is now safe to turn the text into a number
    order_amount = int(order_text)

    # The first true rule wins
    if membership_level == "gold" and order_amount >= 100:
        discount_rate = 0.20
        discount_reason = "Gold member with qualifying order"
    elif membership_level == "silver" and order_amount >= 100:
        discount_rate = 0.10
        discount_reason = "Silver member with qualifying order"
    elif coupon_response == "yes" or order_amount >= 200:
        discount_rate = 0.05
        discount_reason = "Coupon or large order discount"
    else:
        discount_rate = 0.0
        discount_reason = "No discount"

    # Runs after the discount is chosen (same indent as the if above)
    # (1 - discount_rate) is the share you still pay: 20% off means you pay 80%, so 1 - 0.20 = 0.80
    # Multiplying the order amount by that share gives the final price: 150 * 0.80 = 120
    final_total = order_amount * (1 - discount_rate)
    # f"..." lets {variables} sit inside text; :.2f shows 2 decimal places, :.0f shows none
    print(f"Customer: {customer_name}")
    print(f"Membership: {membership_level}")
    print(f"Original total: ${order_amount:.2f}")
    print(f"Discount: {discount_rate * 100:.0f}% ({discount_reason})")
    print(f"Final total: ${final_total:.2f}")

