import timeit



def func_count(fun):
    def inner():
        fun.function_count +=1
        print(fun.function_count)
        return fun()
    fun.function_count=0
    return inner





def main():
    def addNumbers():
        return 12345

    addNumbers = func_count(addNumbers)
    print(addNumbers())
    print(addNumbers())


if __name__ == "__main__":
    main()
