from array import array

s = "MCMXCIV"

dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
total = 0

for i in range(len(s)):
    if (i + 1) < len(s) and (dict[s[i]] < dict[s[i+1]]):
        total -= dict[s[i]]
    else:
       total += dict[s[i]]
print(total)
