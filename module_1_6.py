#2
my_dict = {'name': 'Tema', 'age': 21}
print('Dict:', my_dict)
print('Existing value:', my_dict['name'])
print('Not existing value:', my_dict.get('student'))
my_dict.update({'data': '12-05-2312',
                'like_game': True})
print('Modified dictionary:', my_dict)
print('Deleted value:', my_dict.pop('like_game'))
#3
my_set = {1.24, 2, 2, 'time', 'time'}
print('Set:', my_set)
my_set.add(10)
my_set.add(True)
print('Modified set:', my_set)
my_set.discard(2)