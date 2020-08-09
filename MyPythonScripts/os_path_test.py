import os, shelve, pprint, the_cats

joined = os.path.join('User', 'bin', 'spam')
get_cwd = os.getcwd()

absolute = os.path.abspath('.')
is_abs = os.path.isabs(os.path.abspath('.'))
relative_path = os.path.relpath('C:\\Windows', 'C:\\MyPyhtonScripts')
dir_name = os.path.dirname(get_cwd)
base_name = os.path.basename(get_cwd)
tuple_name = os.path.split(get_cwd)
directories_list = get_cwd.split(os.path.sep)
size = os.path.getsize(get_cwd)
list_dir = os.listdir('C:\\Windows\\System32')
print(relative_path, get_cwd, absolute, is_abs, dir_name, base_name, tuple_name[0], tuple_name[1], directories_list,
      size)
total_size = 0
for filename in list_dir:
    total_size = total_size + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(total_size)
print(os.path.exists('C:\\Windows'),
os.path.isfile(os.path.join(get_cwd, 'pw.py')),
os.path.isdir(os.path.join(tuple_name[0], 'Anotações')),
os.path.isfile(os.path.join(tuple_name[0], 'Anotações', 'Biologia', 'BIO Frente 2.md')))
text = os.path.join(dir_name, 'documentos', 'hello.txt')
hello_file = open(text)
hello_content = hello_file.read()
sonet_file = open('..\documentos\sonet29.txt')
sonet_content = sonet_file.read()
print(hello_content, sonet_content)
hello_file.close()
hello_write = open(text, 'w')
new_hello = hello_write.write('Hello World!')
sonet_file.close()
sonet_file = open('..\documentos\sonet29.txt', 'a')
sonet_file.write('\nSoneto por Automatize Tarefas Maçantes com Python\nÉ DAVI')
shelf_file = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats
shelf_file.close()
shelf_file = shelve.open('mydata')
shelf_keys_list = list(shelf_file.keys())
shelf_values_list = list(shelf_file.values())
print(shelf_keys_list, shelf_values_list)
catz = open('..\documentos\ the_cats.py', 'w')
exibit = catz.write('Cats: ' + pprint.pformat(catz) + '\n')
print(pprint.pprint(shelf_values_list))
print(exibit)
catz.close()
print(the_cats.cats)
