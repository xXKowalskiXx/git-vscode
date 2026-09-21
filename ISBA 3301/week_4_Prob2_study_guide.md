# Week 4 Problem 2 Study Guide: understanding my own code

This walks through `week_4_Prob2.py` from top to bottom. It is built the same
way as Problem 1, so the ideas repeat. That is the point of a "transfer" exercise.

---

## The big picture

The program does these things, in order:

1. Ask for five answers and clean them up.
2. Turn the age into a number, but only if it is safe.
3. Make five True/False checks (one per answer).
4. Run ONE chain: show the first error, OR deny an adult with no photo ID, OR continue.
5. Pick a ticket price (first true rule wins).
6. Print the approved ticket.

The key ideas are the same as Problem 1: **check first, convert safely, first true rule wins.**

---

## Section 1: collect and clean (Parts 1 and 2)

```python
attendee_name = input("Please enter your name: ").strip().title()
age_text = input("Please enter your age (whole number, 0 to 120): ").strip()
affiliation = input("Are you a student, employee, or guest? ").strip().lower()
photo_id = input("Do you have a photo ID? (yes/no): ").strip().lower()
ticket_type = input("Do you want a standard or premium ticket? ").strip().lower()
```

- `input(...)` always returns **text**, even if the user types a number.
- `.strip()` removes spaces at the ends. `.title()` capitalizes each word. `.lower()` makes lowercase.
- Name gets title case. Affiliation, photo ID, and ticket type get lowercase, so `"STUDENT"` and `"student"` count the same.
- `age_text` is text on purpose. It stays text until we know it is safe to convert.

| Variable | Holds | Type |
|---|---|---|
| `attendee_name` | cleaned name | text |
| `age_text` | what the user typed for age | **text** |
| `affiliation` | student, employee, or guest | text |
| `photo_id` | yes or no | text |
| `ticket_type` | standard or premium | text |

---

## Section 2: the safe age conversion

```python
if age_text.isdigit():
    age_number = int(age_text)
else:
    age_number = -1
```

- `.isdigit()` is `True` only if every character is 0-9.
  - `"25"` gives True. `"abc"`, `"12.5"`, `"-3"`, and `""` give False.
- If it is all digits, convert it: `age_number = int(age_text)`.
- If not, use `-1`. This is a **placeholder** so later lines that compare
  `age_number` (like `age_number <= 120`) don't crash. `-1` is never a real age,
  and the validation catches it before it is ever used for pricing.
- `age_text` is what the user typed. `age_number` is the number version. Never mix them up.

---

## Section 3: Boolean checks (Part 3)

```python
name_valid = attendee_name != ""
age_valid = age_text.isdigit() and age_number <= 120
affiliation_valid = affiliation in ["student", "employee", "guest"]
photo_id_valid = photo_id in ["yes", "no"]
ticket_valid = ticket_type in ["standard", "premium"]
```

Each line makes a **Boolean**, meaning only `True` or `False`.

- `!=` means "not equal to". So `name_valid` is True when the name is NOT empty.
- `age_valid` needs BOTH things true (`and`): the text is digits, AND the number is 120 or less.
  - Age `"121"`: digits, but 121 > 120, so False.
  - Age `"abc"`: not digits, so False. (And `age_number` is -1 here, which is why the placeholder matters.)
  - A minus sign or a decimal point makes `.isdigit()` False, so those are rejected too.
- `in [...]` asks "is the answer one of these items?"

These lines only CHECK. They don't change anything.

---

## Section 4: validation and admission chain (Parts 3 and 4)

```python
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
    ...
```

- `not` flips a Boolean. `not name_valid` is True when the name is **bad**.
- It is ONE `if`/`elif` chain. Python goes from the top and runs only the FIRST
  branch that is true, then skips the rest. That is why you only see one message.
- The first five branches are the error checks, in the same order as the inputs.
- The **sixth** branch is the admission rule (Part 4): deny if the person is at
  least 18 (`>= 18`) AND (`and`) said `"no"` to a photo ID.
  - It sits AFTER the five error checks, so it only runs if everything is valid.
    That way `age_number` is guaranteed to be a real age.
- The `else` runs only if there were no errors and no denial. That is where pricing goes.

**Nice thing to notice:** when an adult is denied, the program never reaches the
pricing code, so no price is calculated. That is exactly what the assignment asks.

---

## Section 5: pick the ticket price (Part 5)

```python
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
```

- **First true rule wins.** The order matters a lot here. Read it top to bottom like a checklist.
- `==` compares (asks a question). A single `=` stores a value.
- `and` needs both sides true. `or` needs at least one.
- **The parentheses in rule 2 matter:**
  `(affiliation == "student" or affiliation == "employee") and ticket_type == "premium"`
  - The parentheses group "student or employee" into one yes/no answer, which is then combined with premium.
  - Without them, `and` is checked before `or`, and the meaning changes: it would
    accept ANY student (even with a standard ticket) or a premium employee.
- Rule 3 says "employee with a remaining standard ticket". "Remaining" means a
  student standard ticket was already caught by rule 1, and premium tickets were
  caught by rule 2. You don't need to re-check those.
- Rule 4 is the age discount: 12 or younger, OR 65 or older. It only matters for
  people who didn't match rules 1-3. So a child GUEST gets $12.00.
- Rule 5: any premium ticket that is still left over. Rule 6 (`else`): everything left over.

**Rule order example:** a 10-year-old guest with a premium ticket.
- Rule 1: not a student. Skip.
- Rule 2: not student/employee. Skip.
- Rule 3: not an employee. Skip.
- Rule 4: age 10 <= 12, TRUE. Price is $12.00 (Age discount ticket). Stop.
- Rule 5 (premium, $25) is never reached, because rule 4 came first.

---

## Section 6: display the ticket (Part 6)

```python
    print(f"Attendee: {attendee_name}, Age: {age_number}")
    print(f"Affiliation: {affiliation.upper()}")
    print(f"Ticket type: {ticket_type.upper()}")
    print("Admission status: APPROVED")
    print(f"Price category: {price_category}")
    print(f"Ticket price: ${ticket_price:.2f}")
```

- `f"..."` is an f-string: variables inside `{ }` are replaced with their values.
- `.upper()` makes text UPPERCASE: `"student"` becomes `"STUDENT"`.
- `"Admission status: APPROVED"` has no variable, so it is a normal string (no `f` needed).
- `${ticket_price:.2f}`:
  - the `$` is just a dollar sign character
  - `:.2f` means "show exactly 2 decimal places", so `8` shows as `8.00`
- These lines are indented 4 spaces, so they are inside the last `else`. They
  only run for approved tickets.

---

## Full traces

**Trace 1:** `  sam lee `, `20`, `STUDENT`, `yes`, `standard`

1. Cleaned: name `"Sam Lee"`, age_text `"20"`, affiliation `"student"`, photo_id `"yes"`, ticket_type `"standard"`.
2. `"20".isdigit()` is True, so `age_number = 20`.
3. All five Booleans are True.
4. All the `not ...` branches are False. Adult check: `20 >= 18` is True, but `photo_id == "no"` is False, so `and` gives False. Falls to `else`.
5. Pricing: student AND standard matches rule 1. Price is 8.00.
6. Output: STUDENT, STANDARD, APPROVED, Student standard ticket, $8.00.

**Trace 2:** `Al`, `30`, `student`, `no`, `standard`

1. All five entries are valid.
2. Adult check: `30 >= 18` True, AND `photo_id == "no"` True. So the denial branch runs.
3. Prints "Admission denied: photo ID is required for adults." The `else` is skipped, so no price is calculated.

**Trace 3:** `Al`, `abc`, `guest`, `yes`, `standard`

1. `"abc".isdigit()` is False, so `age_number = -1`.
2. `age_valid` is False.
3. The chain reaches `elif not age_valid` and prints the age error. Nothing else runs.

---

## Likely quiz questions (with answers)

**1. Why do we keep age as text before converting?**
`int()` crashes on things like `"abc"`. We check with `.isdigit()` first so the
conversion only happens when it is safe.

**2. Why set `age_number = -1` when the age isn't digits?**
So later Boolean lines that use `age_number` can still run without crashing.
`-1` is a placeholder that is never a real age, and the validation catches it before pricing.

**3. Why is `age_valid` written with `and`?**
The age must be numeric AND no greater than 120. Both must be true.

**4. What does `not age_valid` mean?**
`age_valid` is True when age is fine. `not` flips it, so `not age_valid` is True when the age is BAD.

**5. Why is the photo ID denial after the five error checks?**
So it only runs when all inputs are valid, and `age_number` is a real number.

**6. What do the parentheses do in the "student or employee" premium rule?**
They group `student or employee` into one condition before combining with `and`
premium. Without them, the `and` binds first and the rule changes meaning.

**7. Why is the age discount rule before the general premium rule?**
First true rule wins. A child guest with a premium ticket should get $12.00, not $25.00.

**8. What happens if an 18-year-old says `no` to photo ID?**
`age_number >= 18` is True and `photo_id == "no"` is True, so they are denied.
An age of 17 is NOT denied, because `17 >= 18` is False.

**9. Change the adult age limit from 18 to 21.**
Change `age_number >= 18` to `age_number >= 21` in the denial `elif`.

**10. Change the student standard price to $9.50.**
In rule 1, change `ticket_price = 8.00` to `ticket_price = 9.50`.

**11. Change the senior age from 65 to 60.**
In rule 4, change `age_number >= 65` to `age_number >= 60`.

**12. Add "alumni" as a fourth affiliation.**
Add `"alumni"` to the list in `affiliation_valid` and update the error message.
It would fall through to the general rules unless you add a specific rule.

**13. What does `.upper()` do and where is it used?**
Makes text uppercase. It is used in the display lines for affiliation and ticket type.

**14. What happens if the user types age `121`? What about `12.5`?**
`121`: digits, but greater than 120, so `age_valid` is False. `12.5`: has a dot,
so `.isdigit()` is False. Both print the age error.

**15. What does `:.2f` do?**
Shows a number with exactly 2 digits after the decimal point, like `8.00`.

**16. Why does an adult with no photo ID never get a price?**
The denial branch runs and the chain stops. The pricing code is inside the `else`,
which is skipped.

---

## Quick cheat sheet

| Symbol / word | Meaning |
|---|---|
| `=` | store a value |
| `==` | equal to (a question) |
| `!=` | not equal to |
| `>=` / `<=` | greater than or equal / less than or equal |
| `and` | both must be true |
| `or` | at least one must be true |
| `not` | flips True/False |
| `in [...]` | is it one of these items? |
| `( ... )` | group conditions so they are checked together first |
| `.strip()` | remove spaces at the ends |
| `.title()` | Capitalize Each Word |
| `.lower()` / `.upper()` | all lowercase / all uppercase |
| `.isdigit()` | True if every character is a digit |
| `int(x)` | convert text to a whole number |
| `:.2f` | show 2 decimal places |
