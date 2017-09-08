from functools import wraps


def your_decorator(func):
    '''Decorator to ...'''
    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        print("Do you like it ?")
        func(*args, **kwargs)

        return print("Ok, move to the next chalange")
    return wrapper


@your_decorator
def some_function():
    print("No, I've tired from decorator tutorials")


if __name__ == '__main__':
    some_function()
