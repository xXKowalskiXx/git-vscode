# Week 4 Study Guide: understanding my own code

This walks through `week_4_Prob1&2.py` from top to bottom. The code is shown in
pieces, with what each piece does and why.

---

## The big picture

The program does five things, in this order:

1. Ask the user for four answers and clean them up.
2. Check each answer and store True/False results.
3. If any answer is bad, show ONE error and stop.
4. If all answers are good, pick a discount (first true rule wins).
5. Calculate and print the final total.

The most important idea: **check first, convert later.** The order total stays
as text until we know it is all digits. Only then is it safe to turn it into a
number with `int()`.

---

## Section 1: collect and clean (Parts 1 and 2)

```python
customer_name = input("Enter your name: ").strip().title()
membership_level = input("Enter your membership level (standard, silver, gold): ").strip().lower()
order_text = input("Enter your order total in whole dollars: ").strip()
coupon_response = input("Do you have a coupon? (yes/no): ").strip().lower()
```

- `input(...)` shows a prompt and returns whatever the user types, **always as text**.
- Methods can be chained. Each one works on the result of the one before it:
  - `.strip()` removes spaces at the start and end: `"  ann  "` becomes `"ann"`
  - `.title()` capitalizes each word: `"ann lee"` becomes `"Ann Lee"`
  - `.lower()` makes everything lowercase: `"GOLD"` becomes `"gold"`
- Why lowercase membership and coupon? So `"Gold"`, `"GOLD"`, and `"gold"` all count as the same answer.
- `order_text` only gets `.strip()`. Numbers have no case, so nothing else is needed. It stays text on purpose.

| Variable | Holds | Type at this point |
|---|---|---|
| `customer_name` | cleaned name | text |
| `membership_level` | cleaned membership | text |
| `order_text` | what the user typed for the total | **text** |
| `coupon_response` | cleaned coupon answer | text |

---

## Section 2: Boolean checks (Part 3)

```python
name_valid = customer_name != ""
membership_valid = membership_level in ["standard", "silver", "gold"]
order_valid = order_text.isdigit()
coupon_valid = coupon_response in ["yes", "no"]
```

Each line makes a **Boolean**, a value that is only `True` or `False`.

- `customer_name != ""` means "the name is NOT empty." `!=` means "not equal to."
- `membership_level in [...]` means "is the membership one of the items in this list?"
- `order_text.isdigit()` is `True` only if every character is a digit 0-9. That means:
  - `"150"` gives `True`
  - `"abc"` gives `False`
  - `"12.5"` gives `False` (the dot is not a digit)
  - `"-5"` gives `False` (the minus sign is not a digit)
  - `""` gives `False`
- `coupon_response in ["yes", "no"]` is the same idea as membership, with two options.

These lines only CHECK. They don't change the inputs.

---

## Section 3: validation chain (Part 4, first half)

```python
if not name_valid:
    print("Error: name cannot be empty.")
elif not membership_valid:
    print("Error: membership must be standard, silver, or gold.")
elif not order_valid:
    print("Error: order total must be a whole number.")
elif not coupon_valid:
    print("Error: coupon must be yes or no.")
else:
    ...
```

- `not` flips a Boolean. `not name_valid` is `True` when the name is **bad**.
- So each branch reads: "if this thing is bad, show its error."
- `if` / `elif` / `else` is **one chain**. Python checks from the top and runs
  only the FIRST branch that is true, then skips the rest.
  - That is why you see only one error, even if everything is wrong.
  - If these were four separate `if` statements, you could get four errors.
- The `else` runs only when none of the errors were true, meaning everything is valid.

---

## Section 4: convert and pick a discount (inside the `else`)

```python
    order_amount = int(order_text)
```

- Now it is safe to convert. We know `order_text` is all digits, so `int()` won't crash.
- Trying `int("abc")` earlier would crash the program. That is why we validate first.
- `order_amount` is the number version. `order_text` is still the text version.

```python
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
```

- `==` **compares** two things (asks a question). A single `=` **stores** a value.
- `and` needs BOTH sides true. `or` needs at least ONE side true.
- The order matters: the first true rule wins.
  - A gold member with a $250 order matches rule 1 (20%), so rules 2-4 are never checked.
    That is why they get 20% and not 5%.
- Every branch sets the same two variables and prints nothing. The printing
  happens once, after the chain.
- The final `else` has no condition. It runs only if nothing above matched.

---

## Section 5: calculate and print

```python
    final_total = order_amount * (1 - discount_rate)
    print(f"Customer: {customer_name}")
    print(f"Membership: {membership_level}")
    print(f"Original total: ${order_amount:.2f}")
    print(f"Discount: {discount_rate * 100:.0f}% ({discount_reason})")
    print(f"Final total: ${final_total:.2f}")
```

**The math:**
- `discount_rate` is a decimal: 20% = `0.20`.
- `(1 - discount_rate)` is the share the customer still pays. With 20% off, they pay 80%: `1 - 0.20 = 0.80`.
- `order_amount * 0.80` is the final price.

| Case | Calculation | Result |
|---|---|---|
| Gold, $150 | `150 * (1 - 0.20)` | 120.00 |
| Standard, $250 | `250 * (1 - 0.05)` | 237.50 |
| Standard, $50 | `50 * (1 - 0.0)` | 50.00 |

**The f-strings:**
- `f"..."` lets you put variables inside `{ }` and they are replaced by their values.
- `$` before `{` is just a dollar sign character in the text.
- After a colon inside `{ }`, you control how a number looks:
  - `:.2f` means 2 decimal places (`120` shows as `120.00`)
  - `:.0f` means 0 decimal places (`20.0` shows as `20`)
- `discount_rate * 100` turns `0.20` into `20`, so it prints as a percent.

**Indentation matters here:** these lines are indented 4 spaces, the same level
as the discount `if`. That means they run after the discount is chosen. If they
were indented 8 spaces, they would sit inside the last `else` and only run when
there is no discount.

---

## Full trace: what happens with these inputs

User types: `  ann lee `, `GOLD`, `150`, `no`

1. After cleaning: name `"Ann Lee"`, membership `"gold"`, order_text `"150"`, coupon `"no"`.
2. Booleans: `name_valid` True, `membership_valid` True, `order_valid` True, `coupon_valid` True.
3. Every `not ...` is False, so all the errors are skipped and the `else` runs.
4. `order_amount` becomes the number `150`.
5. Gold and 150 >= 100, so `discount_rate` is 0.20 and the reason is "Gold member...".
6. `final_total` is `150 * 0.80` = 120.0.
7. Output: 20% discount, final total `$120.00`.

User types: `Bob`, `platinum`, `50`, `no`

1. `membership_valid` is False.
2. The first branch (`not name_valid`) is False, skip. The second (`not membership_valid`) is True, so it prints the membership error and the chain stops.
3. No discount code runs at all.

---

## Likely quiz questions (with answers)

**1. Why do we keep `order_text` as text until validation passes?**
`int()` crashes on input like `"abc"`. We check with `.isdigit()` first, so the
conversion is only reached when it is safe.

**2. What is the difference between `=` and `==`?**
`=` stores a value in a variable. `==` compares two values and gives True or False.

**3. Why `elif` and not separate `if` statements?**
With `elif`, only the first true branch runs, so the user sees one error (and only
one discount is chosen). Separate `if`s would each be checked on their own.

**4. Why is the gold rule listed before the coupon rule?**
The first true rule wins. A gold member with a big order should get 20%, not 5%.
If the coupon rule came first, they would get only 5%.

**5. What does `not order_valid` mean?**
`order_valid` is True when the text is all digits. `not` flips it, so
`not order_valid` is True when the text is NOT all digits.

**6. What does `:.2f` do?**
Shows a number with exactly 2 digits after the decimal point.

**7. Change the silver discount to 15%. What do you edit?**
In the silver branch, change `discount_rate = 0.10` to `discount_rate = 0.15`.

**8. Change the large-order threshold from $200 to $300.**
In the coupon branch, change `order_amount >= 200` to `order_amount >= 300`.

**9. Add a fourth membership level called "platinum".**
Add `"platinum"` to the list in `membership_valid` (and update the error message).
Then add a discount branch for it if the assignment says it gets one.

**10. What happens if the user types `12.5` for the order total?**
`"12.5".isdigit()` is False because of the dot, so `order_valid` is False and the
program prints "Error: order total must be a whole number." No conversion happens.

**11. What happens if the user types `Gold ` (capital G, trailing space)?**
`.strip()` removes the space and `.lower()` makes it `"gold"`, so it is accepted.

**12. Where would you change the coupon rule to be worth 8%?**
In the coupon/large-order branch, change `discount_rate = 0.05` to `0.08`.

**13. Why are the print lines outside the discount `if` chain?**
So they run once for every valid order, no matter which discount was chosen.
Writing them once, after the chain, avoids repeating them in every branch.

---

## Quick cheat sheet

| Symbol / word | Meaning |
|---|---|
| `=` | store a value |
| `==` | equal to (question) |
| `!=` | not equal to |
| `>=` | greater than or equal to |
| `and` | both must be true |
| `or` | at least one must be true |
| `not` | flips True/False |
| `in [...]` | is it one of these items? |
| `.strip()` | remove spaces at the ends |
| `.title()` | Capitalize Each Word |
| `.lower()` | make lowercase |
| `.isdigit()` | True if all characters are digits |
| `int(x)` | convert text to a whole number |
| `:.2f` | show 2 decimal places |
| `:.0f` | show 0 decimal places |
