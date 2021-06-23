#!/usr/bin/python

def converter_function(number, unit_to_convert_to: str):
    '''
    Function that can convert fahrenheit to celcius vice versa.
    '''
    if unit_to_convert_to == 'F':
        number = (number * 9/5) + 32
    elif unit_to_convert_to == 'C':
        number = (number - 32) * (5/9)
    else:
        return ('Invalid unit')
    return int(number)
