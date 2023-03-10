import json
import pytest
import requests
import allure
from endpoints.get_posts import GetPosts


@allure.feature('GET endpoint')
@allure.story('Get all')
@allure.title('Check that all 100 posts returned')
@allure.issue(
    (
        'https://kontur.fibery.io/Tasks/Task/Geocint-Upload-all-'
        'indicators-via-layer-uploading-endpoint-on-dev-target-13537'
    ),
    name='Bug'
)
def test_get_all_posts(my_text):
    with allure.step('Printing content of the my_text variable'):
        print(my_text)
    with allure.step('Requesting get endpoint for all posts'):
        all_posts = GetPosts()
    with allure.step('Checking that response code is 200'):
        assert all_posts.is_response_200()
    assert all_posts.posts_count_is_correct(100)


@allure.feature('GET endpoint')
@allure.story('Get one')
@pytest.mark.regression
def test_get_one_post():
    get_post = GetPosts(11)
    assert get_post.result_json['id'] == 11


@allure.feature('POST endpoint')
@allure.story('Add a post')
def test_add_post():
    my_headers = {
        'Content-Type': 'application/json',
        # 'Authorization': 'skjdhfksjdfhwieuyiwejhsf',
    }
    my_body = json.dumps(
        {
            "userId": 3,
            "id": 15,
            "title": "Code or Die",
            "body": (
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                "Pellentesque vitae placerat dolor, porta semper nulla"
            )
        }
    )
    response = requests.request(
        'POST',
        'https://jsonplaceholder.typicode.com/posts',
        headers=my_headers,
        data=my_body
    ).json()
    assert response['title'] == 'Code or Die'


@allure.feature('DELETE endpoint')
@allure.story('Delete a post')
def test_delete_post():
    requests.request('DELETE', 'https://jsonplaceholder.typicode.com/posts/40')
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts/40')
    assert response.status_code == 404
