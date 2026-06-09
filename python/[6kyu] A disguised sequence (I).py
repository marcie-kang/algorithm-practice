"""
You can take two points of view to do this kata:

- the first one purely algorithmic from the definition of un.
- the second one - not at all mandatory, but as a complement - is to get a bit your head around and find which sequence is hidden behind un.
"""

def fcn (n):
    if n == 0: return 1
    if n == 1: return 2

    u_current = 1
    u_next = 2

    for num in range(2, n + 1):
        u_after = (6 * u_current * u_next) // (5 * u_current - u_next)
        u_current = u_next
        u_next = u_after

    return u_next
