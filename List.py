# Printing list
buy=["Jet","Ship"]
print(buy)

# Modifing list
# 1
buy=["Jet","Ship"]
print(buy[0])

buy[0]="Island"
print(buy[0])

# 2
buy=["Jet","Ship"]
buy.append("Company")
print(buy)

# 3
buy=["Jet","Ship"]
buy.append("Company")

buy.extend(["Island","Factory"])
print(buy)

# 4
buy=["Jet","Ship"] 
buy.append("Company")
buy=buy+["Island","Factory"]

# 5
buy=["Jet","Ship","Island","Factory"] 
print(buy[1:3])

# 6
buy=["Jet","Ship","Island","Factory"] 
buy.pop(1)
print(buy)