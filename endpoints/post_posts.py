from endpoints.endpoint_handler import EndpointHandler


class PostPosts(EndpointHandler):
    url = 'https://jsonplaceholder.typicode.com/posts'
    method = 'POST'
