# models/login_result_object.py
class LoginResultObject:
    def __init__(self, base_url: str, service_param: str):
        self.base_url = base_url
        self.service_param = service_param

    def to_json(self):
        return {
            'base_url': self.base_url,
            'service_param': self.service_param
        }