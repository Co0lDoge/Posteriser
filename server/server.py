from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from transformers import pipeline
from rembg_default import BackgroundRemover
from PIL import Image
import uvicorn
import io

app = FastAPI()

# Load the transformer model once at startup
TEXT_MODEL_PATH = "model/sage-fredt5-large"
U2NET_PATH = "model/u2net/"
DEEPLAB_MODEL_PATH = 'model/model'

background_pipeline = BackgroundRemover(U2NET_PATH)
text_pipeline = pipeline("text2text-generation", model=TEXT_MODEL_PATH)

@app.get("/correct")
async def correct(text: str):
    try:
        # Process the input text with the model
        result = text_pipeline(text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/rembg")
async def remove_background(image: UploadFile = File(...)):
    # Read the uploaded image into a PIL object
    image_data = await image.read()
    img = Image.open(io.BytesIO(image_data))

    # Process the image (e.g., remove background)
    img_noback = BackgroundRemover(U2NET_PATH).remove_background(img)

    # Convert the image to a byte stream
    img_byte_arr = io.BytesIO()
    img_noback.save(img_byte_arr, format="PNG")
    img_byte_arr.seek(0)

    return StreamingResponse(img_byte_arr, media_type="image/png")

if __name__ == "__main__":
    # Run the app on all available interfaces on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)