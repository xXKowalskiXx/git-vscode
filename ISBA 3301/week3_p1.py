# -----------------------------------------------------------------
#                             Part 1
# -----------------------------------------------------------------
# first_name = input("enter your first name: ")
# last_name = input("enter your last name: ")
# email = input("enter your email: ")
# department = input("name department: ")
# customer_id =input("entern customer id: ")
# -----------------------------------------------------------------
#                             Part 2
# -----------------------------------------------------------------
first_name = input("enter your first name: ").strip().title()
last_name = input("enter your last name: ").strip().title()
email = input("enter your email: ").strip().lower()
department = input("department name: ").strip().title()
customer_id =input("enter customer id: ").strip().upper()
# -----------------------------------------------------------------
#                             Part 3
# -----------------------------------------------------------------
full_name = first_name + " " + last_name
account_prefix = customer_id[0:3]
at_position = email.find("@")
email_domain = email[at_position +1:]
# -----------------------------------------------------------------
#                             Part 4
# -----------------------------------------------------------------
# -------------------------- V1 --------------------------

# print(f"Name: {full_name}")
# print(f"Email: {email}")
# print(f"Domain: {email_domain}")
# print(f"Department: {department}")
# print(f"Customer ID: {customer_id}")
# print(f"Account: {account_prefix}")

# -------------------------- V2 --------------------------

# print("------------CUSTOMER PROFILE-------------")
# print(f"Name: {full_name}")
# print(f"Email: {email}")
# print(f"Domain: {email_domain}")
# print(f"Department: {department}")
# print(f"Customer ID: {customer_id}")
# print(f"Account: {account_prefix}")
# print("------------CUSTOMER PROFILE-------------")

# -------------------------- V3 --------------------------

print(f"""------------CUSTOMER PROFILE-------------
Name:{full_name}
Email:{email}
Domain:{email_domain}
Department:{department}
Customer ID:{customer_id}
Account:{account_prefix}
# ------------CUSTOMER PROFILE-------------""")


