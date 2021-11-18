from pydantic import BaseModel, Field
from typing import Optional


class BaseInput(BaseModel):
    state: Optional[str] = Field(None, example="Insira um estado ou estados separados por vírgulas como no exemplo: DORMINDO, ACORDADO")
    transitions: Optional[str] = Field(None, example="Insira uma transição ou transições separadas por vírgulas como no exemplo: 08:00, 12:00")


if __name__ == "__main__":
    # function to strip the input by comma
    def strip_input(input_data):
        input_data = "".join(input_data.split())
        input_data = input_data.split(",")
        return input_data

    print(strip_input("08:00"))
