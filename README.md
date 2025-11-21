# Oscar Leading Actress API

A simple web app that tells you which actress won the Oscar for Best Leading Actress in any year from 2010 to 2025.

## What Does This Do?

**The Problem:** You want to quickly find out who won the Best Actress Oscar in a specific year without searching through long lists online.

**The Solution:** This app lets you type in an actress's name and instantly get back which movie she won for and what year. It's fast and easy to use!

## How It Works

The app is built with **FastAPI**, which is a tool that helps create simple web services in Python. Here's what happens:

1. You ask for an actress's name (like "Emma Stone")
2. The app looks it up in a list
3. The app sends you back the movie title and year
4. Done!

**What I Used:**
- **FastAPI** - A Python tool for building web services (this is the course concept I'm using)
- **Python dictionary** - A simple list that stores all the Oscar winner information
- **Docker** - A way to package the app so it runs the same way on any computer

## What Data Does It Have?

The app knows about Oscar winners from 2010 to 2025. The information comes from public Oscar records and is stored in a simple Python file called `data.py`.

## How to Run This App

### Option 1: Run with Docker (Recommended - Works on any computer)

**Step 1: Build the app**
```bash
docker build -t oscar-actress-api:latest .
```

**Step 2: Run the app**
```bash
docker run --rm -p 8080:8080 oscar-actress-api:latest
```

**Step 3: Test it!**

Open your web browser and try these links:
- Health check: http://localhost:8080/health
- Look up Emma Stone: http://localhost:8080/winner/Emma%20Stone
- Interactive docs: http://localhost:8080/docs

Or use this command in a terminal:
```bash
curl http://localhost:8080/health
```

You should see: `{"status":"ok"}`

**To stop the app:** Press `Ctrl+C` in the terminal where it's running.

---

### Option 2: Run with the run.sh script (Mac/Linux/Git Bash only)

```bash
bash run.sh
```

**Note:** If you're using Windows PowerShell, use Option 1 instead.

---

### Option 3: Run without Docker (if you want to test locally)

1. Install Python
2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install what the app needs:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   uvicorn src.app:api --reload --host 0.0.0.0 --port 8080
   ```

## Example Outputs

**When you check if the app is running:**
```
GET http://localhost:8080/health
Response: {"status":"ok"}
```

**When you look up an actress:**
```
GET http://localhost:8080/winner/Natalie%20Portman
Response: {"actress":"Natalie Portman","movie":"Black Swan","year":2011}
```

**When you look up someone who didn't win:**
```
GET http://localhost:8080/winner/Random%20Person
Response: 404 Error - "Actress not found (2010–2025)"
```

## Why I Made These Choices

**Why FastAPI instead of other tools?**
- It's simple to learn and use
- It automatically creates documentation for your app (go to `/docs` to see it!)
- It's fast and modern

**Why not use a real database?**
- For this small project, a simple Python dictionary works fine
- If I had thousands of records, I'd use a database like MongoDB or PostgreSQL

**What about bigger projects?**
- This setup works great for small apps
- For bigger apps with lots of users, I'd need to add more features like caching and load balancing

## Safety & Privacy

**Is this safe to use?**
- Yes! The app only shows public Oscar winner information
- It doesn't collect any personal data from users
- If you type a name that's not in the list, it just says "not found" - it doesn't break

**Security features:**
- No passwords or secrets are saved in the code
- Settings are kept in a `.env` file (there's an example file called `.env.example`)
- User input is cleaned up to avoid errors

**Resource usage:**
- This app is very lightweight - it doesn't use much memory or CPU
- It can run easily on most computers or cloud servers

**How to check if it's working:**
- There's a special `/health` endpoint you can check anytime

## Tests

I created some basic tests to make sure everything works:
- Test that the health check returns "ok"
- Test that looking up a real actress works
- Test that looking up a fake name returns an error

The tests are located in the `tests/` folder. Since the Docker container runs successfully and the API works as shown above, the core functionality is validated.

To run the tests, its important to use a virtual environment. Additionally, note that the "python -m" tells Python to run the pytest while keeping track of where your project files are located. Without it, Python can't find the "src" folder and the tests will fail even though the code is right:
```
venv\Scripts\activate
python -m pytest tests/
```

To get out of the virtual environment you just created, simply type:
```
deactivate
```


## What I'd Add Next

If I had more time, here's what I'd improve:
- Add more Oscar categories (Best Actor, Best Director, Best Picture)
- Use a real database instead of a Python file
- Make better error messages
- Add more tests
- Deploy it to the cloud so anyone can use it online

## Links

**GitHub Repository:** https://github.com/ronnyhota/Oscar-Leading-Actress-API

**Live Demo:** Not deployed yet (maybe for extra credit!)

## License

This project is open source - see the LICENSE.txt file for details.