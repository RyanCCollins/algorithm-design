import timeit
from loop import factorial as loopFactorial
from recursive import factorial as recursiveFactorial

value = 100
loop = 'loop'
recursive = 'recursive'

start_time = timeit.default_timer()
loopFactorial(value)
loopTime = (timeit.default_timer() - start_time) * 1000

start_time = timeit.default_timer()
recursiveFactorial(value)
recursiveTime = (timeit.default_timer() - start_time) * 1000

winner = loop if loopTime < recursiveTime else recursive
print(f'The winning strategy was: {winner}')
print(f'The {loop} took: {loopTime}s')
print(f'The {recursive} took: {recursiveTime}s')