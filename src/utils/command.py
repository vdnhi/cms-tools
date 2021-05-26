from typing import List
import os

def make_add_user_command(firstname: str = "", lastname: str = "", username: str = "", password: str = ""):
    return "cmsAddUser -p {} \"{}\" \"{}\" {}".format(password, firstname, lastname, username)

def execute_command(commands: List[str]):
    for command in commands:
        os.system(command)
