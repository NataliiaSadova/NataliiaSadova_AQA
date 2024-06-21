import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", 
            params ={"q": name}
            )
        body = r.json()

        return body
    
    def list_repositories_for_a_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}/repos")
        body = r.json()

        return body
    
    def list_users(self, id):
        r = requests.get('https://api.github.com/users', params ={"since": id })
        body = r.json()

        return body
    
    




