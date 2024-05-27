from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import sqlite3
import uvicorn

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает все домены
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает все методы
    allow_headers=["*"],  # Разрешает все заголовки
)

class Item(BaseModel):
    name: str
    description: str

def init_db():
    conn = sqlite3.connect('blog-back.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Вызовите функцию инициализации базы данных при старте
init_db()

# Создайте endpoint для добавления элемента
@app.post("/items/")
async def create_item(item: Item):
    conn = sqlite3.connect('blog-back.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name, description) VALUES (?, ?)',
                   (item.name, item.description))
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return {"id": item_id, "name": item.name, "description": item.description}

@app.get("/items/", response_model=list[Item])
async def read_items():
    conn = sqlite3.connect('blog-back.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    items = [Item(id=row["id"], name=row["name"], description=row["description"]) for row in rows]
    conn.close()
    return items

app.mount('/static', StaticFiles(directory='dist'), name='static')

posts = [
    {
        'id':1, 
        'title':'About django',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam fugiat, adipisci quo et ipsa eius nam vero nemo distinctio aspernatur animi odit provident asperiores sapiente fugit laudantium expedita molestiae dolores.',
        'comments': [
        {'id':1, 'content':'Comment One', 'author':"John Doe"},
        {'id':2, 'content':'Comment 2', 'author':"John Doe"},
        {'id':3, 'content':'Comment 3', 'author':"John Doe"},
        ]
    },
    {
        'id':2, 
        'title':'Vue.js or React.js',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quibusdam fugiat, adipisci quo et ipsa eius nam vero nemo distinctio aspernatur animi odit provident asperiores sapiente fugit laudantium expedita molestiae dolores.',
        'comments': [
        {'id':4, 'content':'Comment One', 'author':"John Doe"},
        {'id':5, 'content':'Comment 2', 'author':"John Doe"},
        {'id':6, 'content':'Comment 5', 'author':"John Doe"},
        ]
    },
]

@app.get('/')
def get_index():
    return FileResponse('dist/index.html')

@app.get('/api/posts')
def get_posts():
    return posts

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8088, reload=True)

#     Практика 4:
# Необходимо воспроизвести пример из урока и доработать его:
# - на фронтенде добавить хэдер и футер, чтобы сайт был больше похож на блог
# - на бэкэнде добавить получение данных из базы. Чтобы не усложнять код в качестве базы данных рекомендую использовать SQLite.