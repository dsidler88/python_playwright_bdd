import json
import time
from playwright.sync_api import APIResponse
from api_objects.base_api import BaseApi


class MockApiObject(BaseApi):

    def visit_github_project(self,page):
        """
        Visit the github project page
        """
        page.goto("http://www.google.com")
        time.sleep(15)
        pass
        # response: APIResponse = self.request_get("https://jsonplaceholder.typicode.com/posts/1")
        # assert response.ok, "Response is not ok"

