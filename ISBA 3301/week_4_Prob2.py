# -----------------------------------------------------------------
#                    Parts 1 and 2: collect and clean
# -----------------------------------------------------------------
# .strip() removes extra spaces, .title() capitalizes names, .lower() makes text lowercase
attendee_name = input("Please enter your name: ").strip().title()
age_text = input("Please enter your age (whole number, 0 to 120): ").strip()   # still text for now
affiliation = input("Are you a student, employee, or guest? ").strip().lower()
photo_id = input("Do you have a photo ID? (yes/no): ").strip().lower()
ticket_type = input("Do you want a standard or premium ticket? ").strip().lower()

# Turn age into a number only if it is all digits.
# Otherwise use -1 so the checks below can still run without crashing.
if age_text.isdigit():
    age_number = int(age_text)
else:
    age_number = -1

# -----------------------------------------------------------------
#                    Part 3: Boolean checks (True or False)
# -----------------------------------------------------------------
name_valid = attendee_name != ""
age_valid = age_text.isdigit() and age_number <= 120
affiliation_valid = affiliation in ["student", "employee", "guest"]
photo_id_valid = photo_id in ["yes", "no"]
ticket_valid = ticket_type in ["standard", "premium"]

# -----------------------------------------------------------------
#          Parts 3 and 4: validate, then check admission
# -----------------------------------------------------------------
# Only the FIRST true branch runs. The last elif is the photo ID rule (Part 4).
if not name_valid:
    print("Error: name cannot be empty.")
elif not age_valid:
    print("Error: age must be a whole number from 0 to 120.")
elif not affiliation_valid:
    print("Error: affiliation must be student, employee, or guest.")
elif not photo_id_valid:
    print("Error: photo ID must be yes or no.")
elif not ticket_valid:
    print("Error: ticket type must be standard or premium.")
elif age_number >= 18 and photo_id == "no":
    print("Admission denied: photo ID is required for adults.")
else:
    # -------------------------------------------------------------
    #    Part 5: pick the ticket price (first true rule wins)
    # -------------------------------------------------------------
    if affiliation == "student" and ticket_type == "standard":
        ticket_price = 8.00
        price_category = "Student standard ticket"
    elif (affiliation == "student" or affiliation == "employee") and ticket_type == "premium":
        ticket_price = 14.00
        price_category = "Campus affiliate premium ticket"
    elif affiliation == "employee" and ticket_type == "standard":
        ticket_price = 10.00
        price_category = "Employee standard ticket"
    elif age_number <= 12 or age_number >= 65:
        ticket_price = 12.00
        price_category = "Age discount ticket"
    elif ticket_type == "premium":
        ticket_price = 25.00
        price_category = "General premium ticket"
    else:
        ticket_price = 18.00
        price_category = "General standard ticket"

    # -------------------------------------------------------------
    #                Part 6: show the approved ticket
    # -------------------------------------------------------------
    # .upper() makes text UPPERCASE; :.2f shows 2 decimal places
    print(f"Attendee: {attendee_name}, Age: {age_number}")
    print(f"Affiliation: {affiliation.upper()}")
    print(f"Ticket type: {ticket_type.upper()}")
    print("Admission status: APPROVED")
    print(f"Price category: {price_category}")
    print(f"Ticket price: ${ticket_price:.2f}")
