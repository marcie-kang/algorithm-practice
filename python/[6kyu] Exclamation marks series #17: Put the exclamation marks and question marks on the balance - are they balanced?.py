"""
Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two strings left and right on the balance - are they balanced?

If the left side is more heavy, return "Left"; if the right side is more heavy, return "Right"; if they are balanced, return "Balance".

Examples
"!!", "??"     -->  "Right"
"!??", "?!!"   -->  "Left"
"!?!!", "?!?"  -->  "Left"
"!!???!????", "??!!?!!!!!!!"  -->  "Balance"
"""

def balance(left, right):
    weight = {"!": 2, "?": 3}
    left_sum = sum(weight[mark] for mark in left)
    right_sum = sum(weight[mark] for mark in right)

    if left_sum > right_sum:
        return "Left"
    elif right_sum > left_sum:
        return "Right"
    else:
        return "Balance"
