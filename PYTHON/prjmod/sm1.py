def fun1():
    """_summary_
    """
    print("FUN1")
    
def fun2():
    print("FUN2")
    
def fun3():
    print("FUN3")
    
def fun4(x, kwarg=3):
    """_summary_

    :param x: _description_
    :type x: _type_
    :param kwarg: _description_, defaults to 3
    :type kwarg: int, optional
    :return: _description_
    :rtype: _type_
    """
    if (x < 2):
        raise(TypeError)   
    
    return kwarg

