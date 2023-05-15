import requests


def test_repo():
    # 'curl -L -H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/emojis')
    r = requests.get(
        url="https://api.github.com/emojis",
        headers={
            "Accept": "application/vnd.github+json",
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
