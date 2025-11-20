
# Executive Summary

**Problem:** People often want a quick way to check Oscar winners for Best Leading Actress without digging through long lists or websites.

**Solution:** This project is a simple FastAPI app that lets you type in an actress’s name (2010–2025) and instantly see the movie and year she won. It also has a health check endpoint to confirm the app is running.

# System Overview

**Course Concept(s):** This project uses FastAPI, a Python web framework, to build a simple API. FastAPI is a concept from the course module on APIs and data pipelines.

**Architecture Diagram:**  
The system is very simple:
- User sends a request (like asking for an actress name).
- FastAPI receives the request in `app.py`.
- The app looks up data from `data.py`.
- The app sends back a JSON response.

(See diagram in /assets once added.)

**Data/Models/Services:**  
- Data source: `data.py` file with Oscar winners (2010–2025).  
- Format: Python dictionary.  
- License: Public information, no restrictions.

# How to Run (Local)

This app is designed to run inside a container (Docker), but here are the basic steps to run it locally:

1. Make sure you have Python installed.
2. Create and activate a virtual environment:

python -m venv venv 

venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Run the app with Uvicorn:

uvicorn src.app:api --reload --host 0.0.0.0 --port 8080

5. Test the health endpoint:
curl.exe http://localhost:8080/health

Expected output:

{"status":"ok"}

# Design Decisions

**Why FastAPI?**  
FastAPI was chosen because it is simple to use, fast, and makes building APIs easy for beginners.

**Alternatives Considered:**  
Flask was another option, but FastAPI has built-in support for automatic documentation and type checking, which made it easier.

**Tradeoffs:**  
- FastAPI is great for small projects, but for very large systems you might need more setup.  
- Keeping the data in a Python file (`data.py`) is simple, but not scalable compared to a database.

**Security/Privacy:**  
- No secrets are stored in the code.  
- Example environment variables are in `.env.example`.  
- Input is stripped to avoid errors with extra spaces.

**Ops (Operations):**  
- Health check endpoint (`/health`) confirms the app is running.  
- Known limitation: only covers Oscar winners from 2010–2025.

# Results & Evaluation

**Sample Outputs:**
- Health check:
{"status":"ok"}

- Example winner lookup:
GET /winner/Natalie Portman 
Response: {"actress":"Natalie Portman","movie":"Black Swan","year":2010}

**Screenshots:**  
Screenshots of these outputs can be placed in the `/assets` folder and linked here.

**Performance Notes:**  
- The app responds instantly for small data lookups.  
- Resource usage is minimal since the dataset is small.

**Validation/Tests:**  
- A simple test confirms `/health` returns status 200 and `{"status":"ok"}`.  
- Data lookup works for valid names and returns 404 for names not in the dataset.

## Ethics, Security, and Operations

- **Privacy:**  
  This app only shows public Oscar winner data. It does not collect or store any personal information about users.

- **Safe Inputs:**  
  If you type in an actress name that isn’t in the list, the app gives a clear “Not Found” message instead of breaking.

- **Environment Settings:**  
  Any settings (like port numbers or future secrets) are kept in a `.env` file. Nothing private is written directly into the code.

- **Lightweight App:**  
  The app is small and fast. It doesn’t use much memory or CPU, so it can run easily on most computers or cloud services.

- **Health Check:**  
  There is a `/health` endpoint that lets you quickly check if the app is running.

- **Ethical Use:**  
  The data comes from public Oscar records. It’s used here only for learning and demo purposes, not for profit.



# What’s Next

- Add more Oscar categories (Best Actor, Best Director, etc.).
- Connect to a real database instead of a Python dictionary.
- Improve error messages and input handling.
- Add more unit tests in the `tests/` folder.
- Deploy the app to the cloud for extra credit.

# Links

**GitHub Repo:** <INSERT-YOUR-REPO-URL-HERE>

**Public Cloud App (optional):** Not deployed yet.


