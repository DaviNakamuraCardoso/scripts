import csv

output_file = open('output.csv', 'w', newline='')
output_writer = csv.writer(output_file)
output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_writer.writerow(['Hell, World!', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1, 2, 3.141592, 4])
output_file.close()

csv_file = open('example1.tsv', 'w', newline='') # We save it as a tsv because the delimiter is a tab
csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
csv_writer.writerow(['apples', 'oranges', 'grapes'])
csv_writer.writerow(['eggs', 'bacon', 'ham'])
csv_writer.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csv_file.close()


