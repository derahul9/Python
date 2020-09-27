import pandas

dtxt = pandas.read_csv("Employees.txt")
#print(dtxt)

dtxt2 = pandas.read_csv("Employees2.txt", delimiter = "|")
#print(dtxt2)

dcsv = pandas.read_csv("Employees.csv", header = None, names = ["A", "B", "C", "D", "E", "F", "G", "H"])
#print(dcsv)
#print (dcsv.shape)

dxlsx = pandas.read_excel("Employees.xlsx", sheet_name= 0)      #Need additional module - pip3 install xlrd
#print (dxlsx)

djson = pandas.read_json("Employees.json")
#print (djson)
#print (djson.loc[:, "Department"])
#print(djson.loc[[2,4,7]])
#print(djson.loc[3:5,"Phone":"Skills"])
#print (djson.iloc[[4,6,8]])
#print (djson.iloc[2, 2:5])
#print (djson.sample())
#print (djson.sample(n = 4))
#print (djson.sample(frac = 0.8))
#print(djson[(djson.loc[:,"Salary"] < 50000) | (djson.loc[:,"Salary"] > 56000)])
#print(djson[(djson.loc[:,"Salary"] > 50000) & (djson.loc[:,"Department"] == "Sales")]
#print(djson[(djson.loc[:,"Salary"] > 50000) ~ (djson.loc[:,"Department"] == "Sales")]

#Adding to table
djson["Badge ID"] = ["0010", "0011", "0012", "0013", "0014", "0015", "0016", "0017", "0018", "0019"]
#print (djson)

# Updating multiple rows based on a condition
djson.loc[djson["Department"] == "IT", "Salary"] = "90000"

# ...or, being more granular and using multiple conditions:
djson.loc[(djson["Department"] == "IT") & (djson["Skills"] == "Networking"), "Salary"] = "100000"

# Updating multiple fields on the same row
djson.loc[djson["ID"] == 9, ["Salary", "Phone"]] = ["80000", "555666777"]

print (djson)




