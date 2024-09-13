# models/login_result_object.py
class LoginResultObject:
    def __init__(self, url: str, service_param: str):
        self.url = url
        self.service_param = service_param

    def to_json(self):
        return {
            'url': self.url,
            'service_param': self.service_param
        }
    
    @classmethod
    def from_json(cls, data: dict):
        return cls(url=data['url'], service_param=data['service_param'])
    

    def is_equal(self, other):
        if not isinstance(other, LoginResultObject):
            return False
        return self.url == other.url and self.service_param == other.service_param