"""
    Operation Functions
"""
from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import schemas
from Fish import Fish
from database import engine, SessionLocal, Base

# Create the database
Base.metadata.create_all(engine)

app = FastAPI()


# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get('/fish/{fish_id}', response_model=schemas.Fish)
async def get_fish_by_id(fish_id: str, session: Session = Depends(get_session)):
    fish = session.get(Fish, fish_id)

    # Error handling
    if not fish:
        raise HTTPException(status_code=404, detail=f"Fish with id {fish_id} not found")
    return schemas.Fish.from_orm(fish)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8081)
