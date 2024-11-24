from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cấu hình URL kết nối MySQL
DATABASE_URL = "mysql+mysqlconnector://khahhann:10102003@localhost:3306/backend_data"

# Tạo engine SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Khởi tạo cơ sở dữ liệu
Base = declarative_base()

# Dependency để lấy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
