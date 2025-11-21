from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from src.data import winners

api = FastAPI(title="Oscar Leading Actress API", version="1.0.0")

# Serve actress images
api.mount("/images", StaticFiles(directory="actress_pictures"), name="images")

# Default endpoint - returns HTML with photos
@api.get("/winner/{actress}", response_class=HTMLResponse)
def get_winner_html(actress: str):
    name = actress.strip()
    for key in winners.keys():
        if key.lower() == name.lower():
            wins = winners[key]
            html = f"""
            <html>
                <head>
                    <title>{key} - Oscar Wins</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            max-width: 800px;
                            margin: 50px auto;
                            padding: 20px;
                            background-color: #f5f5f5;
                        }}
                        h1 {{
                            color: #333;
                        }}
                        .win {{
                            background: white;
                            padding: 20px;
                            margin: 20px 0;
                            border-radius: 8px;
                            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                        }}
                        img {{
                            max-width: 400px;
                            height: auto;
                            border-radius: 8px;
                            margin-top: 10px;
                        }}
                        .movie {{
                            font-size: 24px;
                            font-weight: bold;
                            color: #d4af37;
                        }}
                        .year {{
                            font-size: 18px;
                            color: #666;
                        }}
                    </style>
                </head>
                <body>
                    <h1>{key}</h1>
            """
            for win in wins:
                movie = win["movie"]
                year = win["year"]
                if len(wins) > 1:
                    image_file = f"{key} {movie}.png"
                else:
                    image_file = f"{key}.png"
                html += f"""
                    <div class="win">
                        <div class="movie">{movie}</div>
                        <div class="year">Year: {year}</div>
                        <img src="/images/{image_file}" alt="{key} with Oscar for {movie}">
                    </div>
                """
            html += """
                </body>
            </html>
            """
            return html
    raise HTTPException(status_code=404, detail="Actress not found (2010–2025)")

# Health check
@api.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.app:api", host="0.0.0.0", port=8080, reload=True)