def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
    except Exception as e:
        print(f"An error occurred: {e}")

function_with_closed_file("my_file.txt")
#Alternative solution using try...finally
def function_with_closed_file_try_finally(filename):
    f = None
    try:
        f = open(filename, 'r')
        # ... some code that processes the file ...
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if f:
            f.close() 

function_with_closed_file_try_finally("my_file.txt")