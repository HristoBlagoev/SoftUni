import requests

def fetch_user_repositories(username):
    url = f'http://api.github.com/users/{username}/repos'
    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print('Error!')
        return None


def display_repositories_info(repositories):
    if repositories:
        print("\nUser's Repositories:")
        for repo in repositories:
            print('\nRepositories name:', repo['name'])
            print('Description:', repo['description'])

def main():
    username = input('Enter GitHub Username: ')
    repositories = fetch_user_repositories(username)
    if repositories:
        display_repository_info(repositories)

