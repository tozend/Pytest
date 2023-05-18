import requests

from src.config.config import Config

class GitHubAPIClient:
    def login(self, username='username', password='password'):
        print(f'- - - LOGIN {username}/{password} - - -')

    def logout(self):
        print('- - - LOGOUT - - -')

    def search_repo(self, repo_name):
        """
        Searching repository by a repo_name param
        Return list of repositories
        """
        r = requests.get(
            url=f"{Config.get_property('API_BASE_URL')}/search/repositories",  # after implementing config file
            headers={
                "Accept": "applications/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            params={
                'q': str(repo_name)
            },
        )
        print('Get Search Repo  Response Status Code: ', r.status_code)

        # Throw an error if response is not 2xx or 3xx
        r.raise_for_status()
        body = r.json()['items']
        return body

        # body = r.json()
        # body_repo_names = [x.name for x in body['items']]
        #
        # return body_repo_names

    def get_emojis(self):
        """
        Get list of available emojis in github system
        """
        r = requests.get(
            #url="https://api.github.com/emojis",
            url=f"{Config.get_property('API_BASE_URL')}/emojis",  # after implementing config file
            headers={
                "Accept": "applications/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            })
        print('Get Emojis Response Status Code: ', r.status_code)

        r.raise_for_status()
        body = r.json()
        list_of_emojis = body.keys()

        return list_of_emojis
