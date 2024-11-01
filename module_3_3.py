def  print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list_ = [1, True, "Арс"]
values_dict_ = {'a':45, 'b':True,'c': "Арс"}
print(*values_list_)
print(values_dict_)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

