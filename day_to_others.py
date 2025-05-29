d = int(input("Enter the number of days: "))

y = d//365


print("Years: ",y)


d = d%365

m = d//30

print("Months: ",m)

d = d%30

print("Days1000: ",d)
