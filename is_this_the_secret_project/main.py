from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
       <html>
        <body>
            <title>Conduit</title>
            <div>
                <h1>you con du it!!!!!!!!!!!!!!!!</h1>
                </div>
                <div>
            <img src="https://relayfm.s3.amazonaws.com/uploads/broadcast/image_3x/62/conduit_artwork.png"/>
            </div>
        </body>
    </html> 
    """
