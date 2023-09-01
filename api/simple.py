from fastapi import FastAPI

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': True}

@app.get("/predict")
def predict(num_ppl, wait_ppl):
    return {'wait_ppl':int(num_ppl)*int(wait_ppl)}