# EXCEPTION FILE SETUP

# importing libraries
import os
import sys


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_details: sys):
        self.error_message = CustomException.get_detailed_error_message(error_message=error_message,
                                                                        error_details=error_details)

    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_details: sys) -> str:

        # exec_tb = execution try block
        # execution starts from try block.
        _, _, exec_tb = error_details.exc_info()

        # exec_tb = execution try block
        # tb_frame = try block frame by frame
        # f_lineno = line by line
        # execution starts from try block frame by frame and line by line
        exception_block_line_number = exec_tb.tb_frame.f_lineno

        # exec_tb = execution try block
        # tb_lineno = try block line by line
        try_block_line_number = exec_tb.tb_lineno

        # exec_tb = execution try block
        # tb_frame = try block frame by frame
        # f_code = code by code
        # co_filename = file by file
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"""
        Error Occurred in execution of :
        [{file_name}] at 
        try block line number : [{try_block_line_number}]
        and exception block line number : [{exception_block_line_number}"]
        error message: [{error_message}]
        """

        return error_message

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return CustomException.__name__.str()
