from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def fortune():
    print('foo!')

