from fastapi import FastAPI, HTTPException
from transformers import pipeline
import uvicorn

app = FastAPI()

# Load the transformer model once at startup
model_path = "./model/sage-fredt5-large"
model = pipeline("text2text-generation", model=model_path)

@app.get("/correct/{text}")
async def correct(text: str):
    try:
        # Process the input text with the model
        result = model(text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Run the app on all available interfaces on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)