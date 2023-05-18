import pytest

from src.applications.api.github_api_client import GitHubAPIClient
from src.config.config import Config


@pytest.fixture(scope='module')
def user_fixture():
    # create a user -> precondition
    user_name = "non_existing_user"
    user = dict(name=user_name)
    print(f"User {user_name} created")

    # execute test -> test step
    yield user

    # remove a user -> postconditions
    user = None

    print(f"User {user_name} removed")


@pytest.fixture(scope='module')  # with function scope it will be LOGIN/LOGOUT in every method instead of LOGIN 3 methods LOGOUT
def fixture_github_api_api_client():
    api = GitHubAPIClient()
    api.login(Config.get_property("USERNAME"), Config.get_property("PASSWORD"))

    yield api

    api.logout()
