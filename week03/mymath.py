def my_abs(n):
    ''' 절대값 계산 '''
    if n < 0:
        return -1 * n
    return n

def my_power(base, exponent):
    ''' 거듭제곱 계산'''
    result = 1
    for i in range(exponent):
        result = result * base
    return result