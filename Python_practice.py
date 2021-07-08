counties = ["Arapahoe", "Denver", "Jefferson"]
print(counties)
counties.append("El Paso")
print(counties)
print(counties.index("Denver"))
print(len(counties))
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])
    for county in counties:
        print(counties[i])
    counties_dict = {"Arapahoe" : 422829, "Denver" : 463353, "Jefferson" : 432438 }
    for key, value in counties_dict.items():
        print(f"{key} county has {value} registered voters.")





       


