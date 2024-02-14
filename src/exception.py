import sys


# whenever error gets raise we want to write our own custom message.
def error_message_details(error, error_detail: sys):
    """To write custom error message

    Args:
        error (_type_): error raised
        error_detail (sys): error info from sys.
    """

    # interested in third info in error details
    # on which line exception has occured -> on which line
    _, _, exc_tb = error_detail.exc_info()

    # error in file name
    file_name = exc_tb.tb_frame.f_code.co_filename

    # line number
    line_num = exc_tb.tb_lineno

    error_message = "Error occured in python script name [{0}] line number [{1} error message[{2}]]".format(
        file_name, line_num, str(error)
    )

    return error_message


# whnever we raise this custom exception we will call error message details
# and error deatils will be tracked by sys.
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )

    # whenever we try to print it.. we get error message.
    def __str__(self):
        return self.error_message
