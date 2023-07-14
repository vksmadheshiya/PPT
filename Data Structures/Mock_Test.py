# Write a function that takes a list of numbers as input and returns a new list containing 
# only the even numbers from the input list. Use list comprehension to solve this problem.

def list_comprehension_func(list_input:list=[]) -> list :
    return [item for item in list_input if item%2==0]


print(list_comprehension_func([2,3,4,6,8,9,4,3,8,2]))


# 18. Implement a decorator function called ‘timer’ that measures the execution time of a function.
# The ‘timer’ decorator should print the time taken by the decorated function to execute. 
# Use the ‘time’ module in Python to calculate the execution time.

from time import perf_counter
import time
def timer(func):
    def wrapper_func(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        finish_time = perf_counter()
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
    return wrapper_func

@timer
def my_function():
    # Function code goes here
    time.sleep(2)

my_function()


# @timer
# def make_list1():
#     '''Concatenation'''
#     my_list = []
#     for item in range(10000):
#         my_list = my_list + [item]

# make_list1()


# 19. Write a function called ‘calculate_mean’ 
# that takes a list of numbers as input and returns the mean (average) of the numbers. 
# The function should calculate the mean using the sum of the numbers divided by the total count.

def calculate_mean(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean

data = [10, 15, 20, 25, 30]
mean_value = calculate_mean(data)
print("Mean:", mean_value)


# 20. Write a function called ‘perform_hypothesis_test’ that takes two lists of numbers as input, 
# representing two samples. The function should perform a two-sample t-test and return the p-value. 
# Use the ‘scipy.stats’ module in Python to calculate the t-test and p-value.
# Hypothesis Testing Formula
# Z = ( x̅ – μ0 ) / (σ /√n)

# Here, x̅ is the sample mean,
# μ0 is the population mean,
# σ is the standard deviation,
# n is the sample size.


from scipy import stats
def perform_hypothesis_test(rvs1, rvs2):
    t_stat, p_val = stats.ttest_ind(rvs1,rvs2)
sample1 = [5, 10, 15, 20, 25]
sample2 = [10, 20, 30, 40, 50]
p_value = perform_hypothesis_test(sample1, sample2)
print("P-value:", p_value)
