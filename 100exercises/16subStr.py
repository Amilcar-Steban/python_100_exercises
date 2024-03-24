# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
value = ""

for i in range(n):
    value += f"{input()}\n"

print(re.sub(r"(?<=\s)&&(?=\s)|(?<=\s)\|\|(?=\s)", lambda match: "and" if "&&" in match.group(0) else "or", value))

