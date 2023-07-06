#def outer_function():
#    print("inside inner")
#    def inner_function():
#        print("Hello wolrd")
#    inner_function()
#outer_function()


def outer_function(name):
    def inner_function():
        print("Hello",name)
    inner_function()
outer_function("Aditya")