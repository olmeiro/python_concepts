# HOF: High Order function

def increment(x):
    return x + 1

def high_order_function(x, func):
    return x + func(x)

result = high_order_function(2, increment)
print(result) # 2 + (2 + 1) = 5

# usando lambda

increment_lambda = lambda x : x + 1
high_order_function_lambda = lambda x, func: x + func(x)

result_lambda = high_order_function_lambda(2, increment_lambda)

# Ahora tenemos una lambda generica segun sea el caso:
result_lambda_v2 = high_order_function_lambda(2, lambda x: x + 2)
result_lambda_v3 = high_order_function_lambda(2, lambda x: x - 2)

