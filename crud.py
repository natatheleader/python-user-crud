from dataclasses import dataclass

@dataclass
class User:
    username: str
    password: str
    active: bool

class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, username, password):
        if username in self.users:
            return None
        user = User(username, password, True)
        self.users[username] = user
        return user

    def read_user(self, username):
        if username not in self.users:
            return None
        return self.users[username]

    def update_user(self, username, password, active):
        if username not in self.users:
            return None
        user = self.users[username]
        user.password = password
        user.active = active
        self.users[username] = user
        return user

    def delete_user(self, username):
        if username not in self.users:
            return False
        del self.users[username]
        return True