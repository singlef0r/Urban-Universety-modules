#2
immutable_var = ('a','f',2,3,1.234, False, ["21",332])
print('Immutable tuple:',immutable_var)
#3
# immutable_var[-1] = 100 - кортеж не поддерживает обращение по элементам.
#4
mutable_list = [1,2,3,'a','b','Student', 2.32]
mutable_list[1] = 200
mutable_list[-2] = "Urban ubiversity student"
print('Mutable list:',mutable_list)
