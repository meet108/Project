Male = input("Enter a name: ")
Female = input("Enter a name: ")
combine_string = Male + Female
lower_Case_string = combine_string.lower()

t = lower_Case_string.count('t')
r = lower_Case_string.count('r')
u = lower_Case_string.count('u')
e = lower_Case_string.count('e')
true = t + r + u + e

l = lower_Case_string.count('l')
o = lower_Case_string.count('o')
v = lower_Case_string.count('v')
e = lower_Case_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score} is beyond")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score} is intermediate")
else:
    print(f"Your score is {love_score}")