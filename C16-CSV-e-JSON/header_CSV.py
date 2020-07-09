import csv

example_csv = open('example.csv')
example_dictionary_reader = csv.DictReader(example_csv) # The dictReader gets the data as a dictionary array,
# with which row as a dictionary, and header as it's keys.
print(list(example_dictionary_reader))
for row in example_dictionary_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
# If you try to use a DictReader in a csv that doesn't have a header, it will use the first line as a header. In this
# case, '4/5/2015 13:34', 'Apples' and '73'. To avoid this, you can pass a second argument to DictReader, like this:
example_file = open('example1.tsv')
example_dict_reader = csv.DictReader(example_file, ['Time', 'Name', 'Amount'])
print(list(example_dict_reader))
for row in example_dict_reader:
    print(row['Time'], row['Name'], row['Amount'])
example_file.close()
output_file = open('output2.csv', 'w', newline='')
# If you want your csv to contain a header, call writeheader
output_dict_writer = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
output_dict_writer.writeheader()
output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '444-4444'})
output_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-5555'})
output_dict_writer.writerow({'Phone': '333-3333', 'Name': 'Carol', 'Pet': 'Dog'})
output_file.close()


