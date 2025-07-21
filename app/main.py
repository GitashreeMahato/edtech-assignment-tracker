from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session  # <-- also needed
from sqlalchemy import text
from app.database import SessionLocal


app = FastAPI()

#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally : 
        db.close()

@app.get("/")
def root():
    return {"message": "API running..."}

@app.get("/db-check")
def check_database_connection(db: Session = Depends(get_db)):
    print("Entered /db-check route")
    try:
        db.execute(text("SELECT 1"))
        print("✅ Database connection successful")
        return {"status": "db is working"}
    except Exception as e:
        print("❌ Database connection failed:", e)
        return {"status": "db is not working", "error": str(e)}
