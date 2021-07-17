# This file is for functions to be used in either EDA or data visualization.

def find_min(object):
    '''
    Meant to be used in the dataframe.apply method
    in order to seperate the reference interval series into a minimum_expected series

    Parameters
    ----------
    object: numpy.int64
        The object the apply method is passing to the function
    
    
    Returns
    ----------
    _min: float
        The minimum value in the range
    
    '''
    lst = str(object).split()
    _min = float(lst[0])
    
    return _min

def find_max(object):
    '''
    Meant to be used in the dataframe.apply method
    in order to seperate the reference interval series into a maximum_expected series

    Parameters
    ----------
    object: numpy.int64
        The object the apply method is passing to the function
    
    
    Returns
    ----------
    _min: float
        The minimum value in the range
    
    '''
    lst = str(object).split()
    _max = float(lst[-1])
    
    return _max


if __name__ == '__main__':
    pass