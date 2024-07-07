from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from models import Song

app = FastAPI()

# Canciones iniciales
songs_db: List[Song] = [
    Song(id=1, title="Ella Baila Sola", score=1, country="MEX", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=2, title="Flowers", score=2, country="USA", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=3, title="La Bebe (Remix)", score=3, country="PRI", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=4, title="Un x100to", score=4, country="COL", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=5, title="TQG", score=5, country="COL", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=6, title="Cruel Summer", score=6, country="USA", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=7, title="Classy 101", score=7, country="PRI", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=8, title="Shakira: Bzrp Music Sessions, Vol. 53", score=8, country="ARG", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=9, title="Cupid", score=9, country="KOR", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=10, title="Yandel 150", score=10, country="PRI", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=11, title="Kill Bill", score=11, country="USA", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=12, title="As It Was", score=12, country="UK", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=13, title="Tengo un plan", score=13, country="HN", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=14, title="Creepin'", score=14, country="CAN", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=15, title="La Bachata", score=15, country="PRI", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=16, title="Beso", score=16, country="ESP", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=17, title="Anti-Hero", score=17, country="USA", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=18, title="Calm Down", score=18, country="NGA", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=19, title="Quevedo: Bzrp Music Sessions, Vol. 52", score=19, country="ARG", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
    Song(id=20, title="Rich Flex", score=20, country="CAN", date_added=datetime.utcnow(), date_modified=datetime.utcnow()),
]

# Función para encontrar una canción por el ID
def find_song(song_id: int) -> Optional[Song]:
    for song in songs_db:
        if song.id == song_id:
            return song
    return None

# Función para obtener el próximo ID disponible
def get_next_id() -> int:
    if not songs_db:
        return 1
    return max(song.id for song in songs_db) + 1

# Endpoint para obtener el ranking de canciones, con opción de filtrar por país y limitar el número de resultados
@app.get("/ranking", response_model=List[Song])
def get_ranking(country: Optional[str] = None, limit: int = Query(10, gt=0)):
    """
    Obtener el ranking de canciones.
    - Si `country` es None, devuelve el ranking mundial.
    - Si `country` tiene un valor, filtra las canciones por ese país y devuelve el ranking por país.
    """
    # Filtrar canciones por el país si se ingresa, si no, devuelve todas las canciones
    filtered_songs = [song for song in songs_db if country is None or song.country == country]
    
    # Ordenar canciones por puntaje (score)
    sorted_songs = sorted(filtered_songs, key=lambda x: x.score)
    
    # Devolver el número limitado de canciones especificadas por `limit`
    return sorted_songs[:limit]

# Endpoint para agregar una nueva canción
@app.post("/song", response_model=Song)
def add_song(song: Song):
    song.id = get_next_id()
    song.date_added = datetime.utcnow()
    song.date_modified = datetime.utcnow()
    songs_db.append(song)
    return song

# Endpoint para obtener la información completa de una canción por ID
@app.get("/song/{id}", response_model=Song)
def get_song(id: int):
    song = find_song(id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

# Endpoint para actualizar una canción existente
@app.put("/song/{id}", response_model=Song)
def update_song(id: int, updated_song: Song):
    song = find_song(id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    song.title = updated_song.title
    song.score = updated_song.score
    song.country = updated_song.country
    song.date_modified = datetime.utcnow()
    return song

# Endpoint para eliminar una canción por ID
@app.delete("/song/{id}")
def delete_song(id: int):
    global songs_db
    songs_db = [song for song in songs_db if song.id != id]
    return {"message": "Song deleted successfully"}

# Endpoint para hacer un 'touch' a una canción, incrementando su posición en el ranking
@app.get("/song/touch/{id}", response_model=Song)
def touch_song(id: int):
    song = find_song(id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    if song.score > 1:
        song.score -= 1
    song.date_modified = datetime.utcnow()
    return song