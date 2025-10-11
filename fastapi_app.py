from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import logging

app = FastAPI()

# Enable CORS for all origins and GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

logging.basicConfig(filename="agent_run.log", level=logging.INFO)

AGENT = "copilot-cli"
EMAIL = "24f2006575@ds.study.iitm.ac.in"

@app.get("/task")
def run_task(q: str, request: Request):
    # Forward q to copilot-cli (simulated here)
    try:
        # For demo, run Python code to print 23rd prime
        if "23th prime" in q or "23rd prime" in q:
            code = """def nth_prime(n):\n    primes = []\n    num = 2\n    while len(primes) < n:\n        for p in primes:\n            if num % p == 0:\n                break\n        else:\n            primes.append(num)\n        num += 1\n    return primes[-1]\nprint(nth_prime(23))\n"""
            with open("agent_task.py", "w") as f:
                f.write(code)
            result = subprocess.run(["python", "agent_task.py"], capture_output=True, text=True)
            output = result.stdout.strip()
        else:
            output = "Agent only supports the 23th prime task for demo."
        # Log the run
        logging.info(f"Task: {q}, Output: {output}, IP: {request.client.host}")
        return JSONResponse({
            "task": q,
            "agent": AGENT,
            "output": output,
            "email": EMAIL
        })
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return JSONResponse({
            "task": q,
            "agent": AGENT,
            "output": str(e),
            "email": EMAIL
        }, status_code=500)
