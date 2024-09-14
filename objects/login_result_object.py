class LoginResultObject:
    def __init__(self, url: str, is_inbox_visible: bool, is_compose_button_visible: bool):
        self.url = url
        self.is_inbox_visible = is_inbox_visible
        self.is_compose_button_visible = is_compose_button_visible

    def is_equal(self, other):
        if not isinstance(other, LoginResultObject):
            return False
        return (
            self.url == other.url and
            self.is_inbox_visible == other.is_inbox_visible and
            self.is_compose_button_visible == other.is_compose_button_visible
        )       

    def to_json(self):
        return {
            'url': self.url,
            'is_inbox_visible': self.serviceis_inbox_visible,
            'is_compose_button_visible': self.is_compose_button_visible
        }
    
    @classmethod
    def from_json(cls, data: dict):
        return cls(url=data['url'], is_inbox_visible=data['is_inbox_visible'], is_compose_button_visible=data['is_compose_button_visible'])
    


    

    