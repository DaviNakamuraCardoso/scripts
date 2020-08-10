import re, os, shutil

datas_americanas = re.compile(r'''^(.*?)
((0|1)?\d)-                                  # mês                               
((0|1|2|3)?\d)-                                     # dia                              
((19|20)\d\d)                                     # ano
(.*?)$
''', re.VERBOSE)


os.chdir('..\\datas')

for american_file_name in os.listdir():
    mo = datas_americanas.search(american_file_name)
    if mo == None:
        continue

    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    euro_filename = before_part + day_part + '-' + month_part + '-' + year_part
    abs_working_dir = os.path.abspath('.')
    american_file_name = os.path.join(abs_working_dir, american_file_name)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    print('Renomeando %s para %s' % (american_file_name, euro_filename))
    shutil.move(american_file_name, euro_filename)