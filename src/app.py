from fastapi import FastAPI, HTTPException
from src.data import winners

api = FastAPI(title="Oscar Leading Actress API", version="1.0.0")

@api.get("/winner/{actress}")
def get_winner(actress: str):
    name = actress.strip()
    
    for key in winners.keys():
        if key.lower() == name.lower():
            wins = winners[key]
            return {"actress": key, "wins": wins}
    
    raise HTTPException(status_code=404, detail="Actress not found (2010–2025)")

@api.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.app:api", host="0.0.0.0", port=8080, reload=True)