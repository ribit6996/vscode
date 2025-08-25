f = int(input("число:"))
d = int(input("второе:"))

s = input("выберете один из способов вычисления(*, /, **):")
if s == "*":
    print(f * d)

elif s == "**":
    print(f ** d)

elif s == '/':
    print(f / d)

else:
    print('Вы ввели полную хуйню')