
def decorator(fn):
    def wrap(*args):
        fn(*args)
        print("Среднее арифметическое чисел ", *args, " = ", sum(args)/len(args))

    return wrap


@decorator
def func_sum(*args):
    print("Сумма чисел ", *args, " = ", sum(args))


func_sum(2, 3, 3, 4)

