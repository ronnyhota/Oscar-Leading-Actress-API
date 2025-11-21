from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from src.data import winners

api = FastAPI(title="Oscar Leading Actress API", version="1.0.0")

api.mount("/images", StaticFiles(directory="actress_pictures"), name="images")

@api.get("/winner/{actress}")
def get_winner(actress: str):
    name = actress.strip()
    
    for key in winners.keys():
        if key.lower() == name.lower():
            wins = winners[key]
            
            for win in wins:
                movie = win["movie"]
                
                if len(wins) > 1:
                    
                    image_file = f"{key} {movie}.png"
                else:
                    
                    image_file = f"{key}.png"
                
                win["image"] = f"/images/{image_file}"
            
            return {"actress": key, "wins": wins}
    
    raise HTTPException(status_code=404, detail="Actress not found (2010–2025)")

@api.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.app:api", host="0.0.0.0", port=8080, reload=True)