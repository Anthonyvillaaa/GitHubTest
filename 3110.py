def is_decimal_integer(input_string):
	if (not input_string.startswith('0')) and input_string.startswith(('0123456789')) and all(char in '0123456789_' for char in input_string[1:]):
		return True
	elif input_string.startswith(('+', '-')) and input_string[1]!='0' and all(char in '0123456789_' for char in input_string[2:]):
		return True
	else:
		return False
	
def is_octal_integer(input_string):
	if input_string.startswith(('0o', '0O')) and all(char in '01234567_' for char in input_string[2:]):
		return True
	else:
		return False

def is_hexadecimal_integer(input_string):
    if input_string.startswith(('0x', '0X')) and all(char in '0123456789abcdefABCDEF_' for char in input_string[2:]):
        return True
    else:
        return False

# def is_float(input_string):
#     try:
#         float_val = float(input_string)
#         return True
#     except ValueError:
#         return False

def check_literal_type(input_string):
    if is_decimal_integer(input_string):
        print("Valid decimal integer")
    elif is_octal_integer(input_string):
        print("Valid octal integer")
    elif is_hexadecimal_integer(input_string):
        print("Valid hexadecimal integer")
#     elif is_float(input_string):
#         print("Valid floating point literal")
    else:
        print("Not a valid.")

input_string = input("Enter a string: ")
check_literal_type(input_string)
