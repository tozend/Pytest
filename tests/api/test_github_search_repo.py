from src.applications.api.github_api_client import GitHubAPIClient

#Test definiotns for specific requests

def test_search_repo_positive(fixture_github_api_api_client):
    """
    This test search for existing repo on GitHub
    """
    # Prepare the existing repo name
    repo_name = 'python'

    # Search for the repo from step #1
    repos_list = fixture_github_api_api_client.search_repo(repo_name)

    # Validate the repo really exists
    assert len(repos_list) != 0

def test_search_repo_negativ(fixture_github_api_api_client):
    """
    This test search for non-existing repo on GitHub
    """
    # Prepare the existing repo name
    repo_name = 'python18237c8m789uc98fuc98wuf98cu427093289ikwoekr'

    # Search for the repo from step #1
    repos_list = fixture_github_api_api_client.search_repo(repo_name)

    # Validate the repo really exists
    assert len(repos_list) == 0
    #assert repo_name not in repos_list