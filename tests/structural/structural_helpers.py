import inspect

def try_to_import():
    try:
        from assignment import POTUSgen
        print("hi")
    except:
        # raise Exception("Variable not set, or file file corrupt")
        return False
    return True

def get_all_functions(module):
    functions = [i for i,_ in inspect.getmembers(module, inspect.isfunction)]
    return functions

def check_for_function(name, module):
    return True if name in get_all_functions(module) else False
