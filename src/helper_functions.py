# This file is for functions to be used in either EDA or data visualization.

def seperate_range(series):
    '''
    Meant to be used in the dataframe.apply method
    in order to seperate the reference interval series into a minimum_expected series
    and a maximum_expected series

    Parameters
    ----------
    series: pandas.series
        The row the apply method is currently passing to this function
    
    
    Returns
    ----------
    _min: float
        The minimum value in the range
    
    _max: float
        The maximum value in the range
    '''
    lst = series['REFERENCE_INTERVAL'].split()
    _min = float(lst[0])
    _max = float(lst[-1])

    return _min, _max


if __name__ == '__main__':
    pass