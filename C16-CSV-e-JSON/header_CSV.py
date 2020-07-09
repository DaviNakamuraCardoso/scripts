import csv

example_csv = open('example.csv')
example_dictonary_reader = csv.DictReader(example_csv) # The dictReader gets the data as a dictionary, with the headers
# as keys an columns as values
for row in example_dictonary_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
