from fastapi import FastAPI

app = FastAPI()


@app.get("/groups")
async def groups():
    groups_list = [
        {
            "id": 1,
            "online": False,
            "nombre": "Casa",
            "color": "1",
            "miembros": ["Adrian", "Brais", "Bea", "Camilo"],
        },
        {
            "id": 2,
            "online": True,
            "nombre": "Trabajo",
            "color": "3",
            "miembros": ["Mario#1231", "Brais#1223", "Miguel#4123"],
        },
    ]
    return groups_list
