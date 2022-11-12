'''
The variables of same name but different name space are shadowed by each name space. 
'''
#!bin/bash/python3

var_shadow = "global"

def outer_function():
    var_shadow = "outer"

    def inner_function():
        var_shadow = "inner"
        print("inner_function scope: %s" % var_shadow)

    inner_function()
    print("outer_function scope: %s" % var_shadow)


if __name__ == "__main__":
    outer_function()
    print("global scope: %s" % var_shadow)
