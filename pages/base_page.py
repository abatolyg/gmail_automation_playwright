# pages/base_page.py
import logging
from typing import Optional
from urllib.parse import parse_qs, urlparse
from playwright.sync_api import Page

from objects.login_result_object import LoginResultObject

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)    

