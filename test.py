import os
print("This file is test")

directory = '.'
for i in range(1, 8):
    if not os.path.exists(f'module_{i}'):
        os.mkdir(f'module_{i}')

