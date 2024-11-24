from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cấu hình CORS
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Danh sách các nguồn được phép
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Phương thức HTTP được phép
    allow_headers=["*"],  # Tất cả các tiêu đề
    max_age=3600,  # Thời gian cache cho các yêu cầu CORS
)

@app.get("/")
async def root():
    return {"message": "Hello World"}
