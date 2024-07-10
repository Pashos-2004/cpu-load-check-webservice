from fastapi import BackgroundTasks, FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def read_root():
    return {"<p>Привет)</p>"}

uvicorn.run(
        app,
        host='localhost',
        port=8080
    )

