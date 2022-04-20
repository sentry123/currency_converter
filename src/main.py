"""
Driver Class for currency_conversion
"""


from get_data import get_data


if __name__ == '__main__':

    identifier_input = str(input("Enter the identifier: "))
    target_currency_input = str(input("Enter the target_currency: "))

    if target_currency_input is None or target_currency_input == '':
        print(get_data(identifier_input))
    else:
        print(get_data(identifier_input, target_currency_input))
