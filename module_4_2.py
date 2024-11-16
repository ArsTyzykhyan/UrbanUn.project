def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() #Программа работает,но ничего не показывает
inner_function() # Программа выдает ошибку:"NameError: name 'inner_function' is not defined"
test_function() # Программа работает,выдает print из функции inner_function()





