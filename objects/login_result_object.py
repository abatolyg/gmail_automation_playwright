class LoginResultObject:
    def __init__(self,error_code, url: str, is_inbox_visible: bool, is_compose_button_visible: bool):
        self.error_code = error_code
        self.url = url
        self.is_inbox_visible = is_inbox_visible
        self.is_compose_button_visible = is_compose_button_visible

    def is_equal(self, other):
        if not isinstance(other, LoginResultObject):
            return False
        return (
            self.error_code == other.error_code and
            self.url == other.url and
            self.is_inbox_visible == other.is_inbox_visible and
            self.is_compose_button_visible == other.is_compose_button_visible
        )       

    def to_json(self):
        return {
            'error_code': self.error_code,
            'url': self.url,
            'is_inbox_visible': self.serviceis_inbox_visible,
            'is_compose_button_visible': self.is_compose_button_visible
        }
    
    @staticmethod
    def from_json(data: dict):
        try:
            expected_results = data['expected_results']
            return LoginResultObject(
                error_code=expected_results.get('error_code', 'unknown'),
                url=expected_results.get('url', ''),
                is_inbox_visible=expected_results.get('is_inbox_visible', False),
                is_compose_button_visible=expected_results.get('is_compose_button_visible', False)
            )
        except KeyError as e:
            raise ValueError(f"Missing key in JSON data: {e}")
    
    
    
    


    

    