import csv

example_file = open('example.csv')
example_reader = csv.reader(example_file)
example_data = list(example_reader)
print(example_data)    # Os dados csv são devolvidos em forma de uma matriz
print(example_data[0][0], example_data[0][1], example_data[0][2])
for i in range(1, len(example_data)):
    print('At', example_data[i][0], 'we sold', example_data[i][2], example_data[i][1])
# IMPORTANTE: Só é possível fazer um loop pelo csv uma vez. Para acessá-lo novamente, abra o arquivo mais uma vez
example_file = open('example.csv')
example_reader = csv.reader(example_file)
for row in example_reader:
    print('Row #' + str(example_reader.line_num) + ' ' + str(row))
example_file.close()
