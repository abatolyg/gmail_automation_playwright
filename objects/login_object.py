# models/login_object.py
class LoginObject:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @classmethod
    def from_json(cls, data: dict):
        return cls(username=data['username'], password=data['password'])