import pandas

#Dataframe is 2 dimensional data structure with labelled access (rows and columns)
#The data source could be list or text or CSV file

d = pandas.DataFrame([['Andy', 46, 'Engineer'], ['Jane', 33, 'Nurse'], ['Robert', 21, 'Student'], ['Maria', 30, 'Student']])
#print (d)     #Columns and Rows are called Index

d1 = pandas.DataFrame([['Andy', 46, 'Engineer'], ['Jane', 33, 'Nurse'], ['Robert', 21, 'Student'], ['Maria', 30, 'Student']], columns = ['Name', 'Age', 'Occupation'], index = ['ID1', 'ID2', 'ID3', 'ID4'])
print (d1)
print (d1.Name)
print (d1.Age.min())

