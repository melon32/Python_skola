my_dictionary = {}

my_dictionary1 = {
    'abols1' : 'green',
    'abols2' : 'red',
    'abols4' : 'blue',
}

my_dictionary1['abols3'] = 'blue'

for key, value in my_dictionary1.items():
    if value == 'blue':
        print(f'{key} : {value}')