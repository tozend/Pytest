import requests

from src.config.config import Config

class GitHubAPIClient:
    def login(self, username, password):
        print(f'- - - LOGIN {username}/{password} - - -')

    def logout(self):
        print('- - - LOGOUT - - -')

    def get_emojis(self):
        """
        Get list of available emojis in github system
        """
        r = requests.get(
            #url="https://api.github.com/emojis",
            url=f"https://{Config.get_property('API_BASE_URL')}/emojis",  # after implementing config file
            headers={
                "Accept": "applications/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            })
        print('Get Emojis Response Status Code: ', r.status_code)

        r.raise_for_status()
        body = r.json()
        list_of_emojis = body.keys()

        return list_of_emojis
