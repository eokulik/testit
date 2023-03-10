from endpoints.endpoint_handler import EndpointHandler
from requests import request


class GetPosts(EndpointHandler):
    url = 'https://jsonplaceholder.typicode.com/posts'
    method = 'GET'

    def __init__(self, post_id=None):
        self.post_id = post_id
        self.result = self.get_endpoint()
        self.result_json = self.result.json()
        self.status_code = self.result.status_code

    def get_endpoint(self):
        if self.post_id:
            result = request(method=self.method, url=self.url + '/' + str(self.post_id))
        else:
            result = request(method=self.method, url=self.url)
        return result

    def posts_count_is_correct(self, expected_number):
        return len(self.result_json) == expected_number
