from typing import Optional,Iterable,List
def fib(n:int,memo:Optional[dict]=dict()) -> int:
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]
print(fib(50))

def grid_traveller(row:int,col:int,memo:Optional[dict]={}) -> int:
    key = str(row) + "," + str(col)
    if key in memo:
        return memo[key]
    if col == 1 and row == 1: 
        return 1
    if col == 0 or row == 0:
        return 0
    memo[key] = grid_traveller(row -1 ,col,memo) + grid_traveller(row,col - 1,memo)
    return memo[key]
print(grid_traveller(180,180))

def can_sum(target:int,values:Iterable[int],memo:Optional[dict]={}) -> bool:
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for value in values:
        remainder = target - value
        if can_sum(remainder,values,memo):
            memo[target] = True
            return True
    memo[target] = False
    return False

print(can_sum(7,[2,4]))
print(can_sum(7,[2,3,4]))
""" memioziation reciepe
    make it work and make it efficient
    """

def sum_of_adjacent(array:List[int]) -> int:
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    max_sums = array[:]
    max_sums[1] = max(array[0],array[1])
    for i in range(2,len(array)):
        max_sums[i] = max(max_sums[i-1],max_sums[i-2]+array[i])
    return max_sums[-1]


def min_coins(n:int,coins:List[int]):
    num_of_coins = [float('inf') for i in range(n+1)]
    num_of_coins[0] = 0
    for i in coins:
        for j in range(n+1):
            if i <= j:
                num_of_coins[j] = min(num_of_coins[j],num_of_coins[j-i]+1)
    return num_of_coins[n] if num_of_coins[n] != float('inf') else 0


print(sum_of_adjacent([75,105,120,75,90,135]))
print(min_coins(7,[1,5,10]))
