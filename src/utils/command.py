from typing import List
import os

def make_add_user_command(firstname: str = "", lastname: str = "", username: str = "", password: str = ""):
    return "cmsAddUser -p {} \"{}\" \"{}\" {}".format(password, firstname, lastname, username)

def make_add_participation_command(contest_id: int, password: str = "", username: str = ""):
    return "cmsAddParticipation -c {} -p {} {}".format(contest_id, password, username)

def execute_command(commands: List[str]):
    print(commands)
    # for command in commands:
    #     os.system(command)
