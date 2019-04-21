## -*- coding: utf-8 -*-
#"""
#Created on Wed Apr  3 11:20:31 2019
#
#@author: 11601
#"""

def solve(n, nums, solveStr='x'):
    ''' Play 24 with nums 1,3,4,6 like so: >>> solve(24, [1,3,4,6]) (6/(1-(3/4))) '''
    n = float(n)
    solved = False

    if len(nums) == 1: 
        return (solveStr.replace('x', str(int(n))) if n == float(nums[0]) else False)

    for num in [float(x) for x in nums]:
        possibles = [   ( n-num , '+', False),
                        ( num-n , '-', True),
                        ( n+num , '-', False),
                        ( n*num , '/', False),
                        ( (n/num if num != 0 else 100000) , '*', True),
                        ( (num/n if n != 0 else 100000) , '/', True)]

        wo = [x for x in nums]
        wo.remove(num)

        for possible in possibles:
            if possible[2]:
                solved = solved or solve(possible[0], wo, solveStr.replace('x', '(' + str(int(num)) + possible[1] + 'x)'))
            else:
                solved = solved or solve(possible[0], wo, solveStr.replace('x', '(x' + possible[1] + str(int(num)) + ')'))

    return solved