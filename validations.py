import constants
import re

class Validation:
    def checkUserInput(option):

        # check user input value match our options
        check_input = bool(re.fullmatch(constants.USER_INPUT_CHECK_USING_REGEX, option))
        return check_input
