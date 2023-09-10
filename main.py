from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    poem = 'poem'

@app.get('/hello')
def index():
    return {'message' : 'Hello World'}

@app.get('/blog/all')
def get_blog_type(type: BlogType):
    return {'message': 'all blogs list below'}

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog Type is {type}'}

@app.get('/blog/{id}type/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

