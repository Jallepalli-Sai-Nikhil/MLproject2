import datetime
import inspect

class CustomException(Exception):
    def __init__(self, message):
        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")
        formatted_time = now.strftime("%H:%M:%S")
        self.message = f"{formatted_date} {formatted_time}: {message}"
        super().__init__(self.message)

    @classmethod
    def error_details(cls):
        frame = inspect.currentframe().f_back
        script_name = inspect.getframeinfo(frame).filename
        line_number = frame.f_lineno
        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        return f"Error occurred in python script name [{script_name}] line number [{line_number}] error message date & time [{formatted_date}]"

# Example usage
try:
    raise CustomException("Something went wrong!")
except CustomException as e:
    print(e)
    print(CustomException.error_details())
    try:
        raise CustomException("Another error occurred!")
    except CustomException as e:
        print(e)
        print(CustomException.error_details())