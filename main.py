from Bot import Bot
import asyncio

problem = """Two water taps together can fill a tank in 9, 3, 8 hours. The tap of larger diameter takes 10 hours less  than the smaller one to fill the tank separately.Find the time in which each tap can separately fill the tank
"""
solution = """
Let the time taken by the smaller pipe to fill the tank be x hr.
Time taken by the larger pipe = (x - 10) hr
Part of tank filled by smaller pipe in 1 hour = 1/x
Part of tank filled by larger pipe in 1 hour = 1/(x - 10)

According to the problem, both pipes together can fill the tank in 9 3/8 hours, which is 75/8 hours. So, the part of the tank they can fill in 1 hour is 8/75.

Therefore, we can set up the equation:
1/x + 1/(x - 10) = 8/75
=> (x-10 + x)/ [x(x - 10)] = 8/75
=> (2x - 10) / [x(x - 10)] = 8/75
=> 75(2x - 10) = 8x(x - 10)
=> 150x - 750 = 8x^2 - 80x
=> 8x^2 - 230x + 750 = 0
=> 8x^2 - 200x -30x + 750 = 0
=> 8x(x-25) - 30(x-25) = 0
=> (x-25)(8x-30) = 0
=> x = 25, 30/8


Time taken by the smaller pipe cannot be 30/8 = 3.75 hours. As in this case, the time taken by the larger pipe will be negative, which is logically not possible.
Therefore, time taken individually by the smaller pipe and the larger pipe will be 25 and 25 - 10 =15 hours respectively.
"""


bot = Bot()
asyncio.run(bot.chat(problem, solution))