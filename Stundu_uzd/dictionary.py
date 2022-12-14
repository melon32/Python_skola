# create an empty dictionary
my_dict = {}

while True:
    key = input('Ievadi vardu: ')
    if key in my_dict:
        print('Vards jau eksiste: ')
        continue

    value = input('Ievadi savu miljako edienu: ')
    
    my_dict[key] = value
    choice = input('Vai velies turpinat? (y/n)')
    if choice == 'n':
        print(my_dict)
        break
    elif choice == 'y':
        continue
    elif choice != 'n':
        print('Analfabets?')
        break
    


    
    
    
