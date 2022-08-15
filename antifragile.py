from lib2to3.pgen2 import token
from todoist_api_python.api import TodoistAPI
import json

class AntiFragile:
    TEST_ACCESS_TOKEN = "test_access_token"
    CLIENT_ID = "client_id"
    CLIENT_SECRET = "client_secret"

    # create an init function for the class
    def __init__(self, token_file):
        """Initialize the AntiFragile class

        Args:
            token: token to authenticate the user
        """
        token_map = self.read_tokens(token_file)
        self.access_token = token_map[AntiFragile.TEST_ACCESS_TOKEN]
        self.client_id = token_map[AntiFragile.CLIENT_ID]
        self.client_secret = token_map[AntiFragile.CLIENT_SECRET]
        self.api = TodoistAPI(self.access_token)

    def read_tokens(self, token_file):
        """Read the tokens from the token file"""
        with open(token_file) as f:
            tokens = json.load(f)
        return tokens

    def add_task(self):
        pass

    def get_all_tasks(self):
        try:
            projects = self.api.get_projects()
            for project in projects:
                print(project)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    token_file = ".tokens"
    af = AntiFragile(token_file)
    af.get_all_tasks()
