import time
import functools
import inspect

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get caller's frame information
        current_frame = inspect.currentframe()
        caller_frame = current_frame.f_back if current_frame else None
        if caller_frame is None:
            raise Exception("No caller frame.")
        
        context = inspect.getframeinfo(caller_frame).code_context
        call_line = context[0] if context else ''
        
        # Extract variable names from the function call
        # Find text between parentheses and split by comma
        start_idx = call_line.find(func.__name__) + len(func.__name__)
        call_args = call_line[start_idx:].split('(', 1)[1].rsplit(')', 1)[0]
        arg_names = [arg.strip() for arg in call_args.split(',') if arg.strip()]
        
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        
        args_str = ", ".join(arg_names)
        print(f"Function '{func.__name__}({args_str})' took {execution_time:.4f} seconds to execute, answer = {result}")
        return result
    return wrapper