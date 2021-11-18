
class Formater:
    @staticmethod
    def format_input_to_list(input_string) -> list:
        input_string = "".join(input_string.split())
        input_string = input_string.split(",")
        return input_string
