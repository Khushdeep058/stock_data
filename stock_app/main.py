from fastapi import FastAPI
from routes.routes import router
import uvicorn
app = FastAPI(title="Stock Data API")

app.include_router(router)

if __name__ == "__main__":
   
    uvicorn.run(app, host="127.0.0.1", port=5011, reload=True)
