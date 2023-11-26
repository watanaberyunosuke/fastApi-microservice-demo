import uvicorn
from fastapi import FastAPI, Response
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Gateway"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/fish/{fish_id}")
async def say_fish(fish_id: int):
    try:
        response = requests.get("http://localhost:8081/fish/" + str(fish_id))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500

    if response.headers['Content-Type'] == 'application/json':
        return {"content": response.json(), "status-code":response.status_code}
    else:
        return Response(response.content)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
