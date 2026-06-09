str = input("enter a string: ")
d = 0
for ch in str:
    if ch.isdigit():
        d = d + 1

print(f"number of digits is {d}, number of character is {len(str) - d}")