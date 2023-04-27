import pytest


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


def test_signup(user_fixture):
    assert user_fixture.get('name') == 'non_existing_user'


def test_signup_negative(user_fixture):
    assert user_fixture.get('name') == 'non_existing_user'


def test_signup_positive(user_fixture):
    assert user_fixture.get('name') == 'non_existing_user'

# def test_signup():
#     user_name = "non_existing_user"
#     user = dict(name=user_name)
#
#     print(f"User {user_name} created")
#
#     assert user.get('name') == user_name
#
#     user = None
#
#     print(f"User {user_name} removed")
