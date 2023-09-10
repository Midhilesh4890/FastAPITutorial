from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    poem = 'poem'

@app.get(path = '/hello')
def index():
    return {'message' : 'Hello World'}

@app.get(path = '/blog/all', 
         tags = ['blog'],
         summary = 'this api call retrieves all blogs',
         description= 'this api call retrieves all blogs listed in the website in the order',
         response_description = 'List of available blogs')

@app.get('/blog/{id}', status_code = status.HTTP_200_OK)
def get_blog_id(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog id {id} is not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message' : f'blog id is {id}'}

@app.get(path = '/blog/type/{type}', tags = ['blog'])
def get_blog_type(type: BlogType):
    return {'message': f'Blog Type is {type}'}

@app.get(path = '/blog/{id}type/{comment_id}', tags=['blog', 'comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
        **Retrieves the information of the user who writes a comment or a blog**
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

