from collections import Counter

s1 = 'BOBthebuilder'
s2 = 'fBoOkBIHnfndBthesibuishlider'

# Count characters in both strings
count1 = Counter(s1)
count2 = Counter(s2)

# Check if all characters of str1 are present in str2
possible = True
for ch in count1:
    if count1[ch] > count2[ch]:
        possible = False
        break

if possible:
    print("Possible")
else:
    print("Not Possible")