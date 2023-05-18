import pytest
import requests

from src.applications.api.github_api_client import GitHubAPIClient

# 1 approach
def test_repo():
    # 'curl -L -H "Accept: applications/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/emojis')
    r = requests.get(
        url="https://api.github.com/emojis",
        headers={
            "Accept": "applications/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
    })

    print(r)
    #print(*r)
    #print(r.__dict__)
    print("Response status code: ", r.status_code)
    # print(requests.codes.ok)
    print("Response Headers: ", r.headers)
    print("Response Cache Header: ", r.headers['Cache-Control'])
    #print("Response Body: ", r.text['zzz'])
    print("Response Body: ", r.json()['zzz'])

    r.raise_for_status()

    assert 'v8' in r.json()['zzz']

# 2 approach

# To create oneliner:
@pytest.fixture(scope='module')
def list_of_emojis(fixture_github_api_api_client):
    yield fixture_github_api_api_client.get_emojis()


# With Conftest fixture
def test_emoji_could_be_retrieved(fixture_github_api_api_client):
    emojis = fixture_github_api_api_client.get_emojis()

    assert len(emojis) != 0


# With oneliner fixture above:
def test_emoji_could_be_retrieved2(list_of_emojis):
    assert len(list_of_emojis) != 0


# Old way:
def test_emoji_exists():
    api = GitHubAPIClient()
    api.login()
    emojis = api.get_emojis()

    assert 'zzz' in emojis
    api.logout()


def test_emoji_doesnt_exists():
    api = GitHubAPIClient()
    emojis = api.get_emojis()

    assert 'zzz123' not in emojis
