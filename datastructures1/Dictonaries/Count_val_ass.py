def val_count(data):
    print("The value of key success count in data: ",sum(key['success']for key in data))
data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}]
val_count(data)