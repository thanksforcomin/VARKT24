def result_accumulator(func):
    memory = []

    def wrapper(*args, method="accumulate"):
        nonlocal memory
        memory.append(func(*args))
        if method == "drop":
            temp = memory.copy()
            memory = []
            return temp

    return wrapper


@result_accumulator
def sum(a, b):
    return a + b


print(sum(5, 6, method="acc"))
print(sum(7, 8, method="drop"))
