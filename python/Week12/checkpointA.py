import pandas

census_data = pandas.read_csv("emlemmon.github.io\python\Week12\census.csv")
print(census_data)

census_data.columns = ["age", "gov", "num", "schooling", "grade", "ageee", "grg", "kjjj", 
                        "mmvm", "check", "fine", "old", "older", "place", "money"]
mean = census_data.age.mean()

print(mean)