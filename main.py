from fastapi import FastAPI

app = FastAPI()
app.title = "My API"

EDAD = "edad"
NOMBRE = "nombre"

movies = [
   {
        "id": 1,
        "name": "The Godfather",
        "imdb": 9.2,
        "year": 1972,
        "rating": 7.5
   },
    {
        "id": 2,
        "name": "aro",
        "imdb": 9.2,
        "year": 1972,
        "rating": 7.5
   }
]
@app.get("/", tags=["home"])
def home():
    return {EDAD: 25, NOMBRE: "Juan"}


@app.get("/movies/{id}", tags=["home"])  
def get_movie(id:int):
    for movie in movies:
        if movie["id"] == id:
            return movie
