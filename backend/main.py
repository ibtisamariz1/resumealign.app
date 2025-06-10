from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

app = FastAPI()

# CORS middleware for frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Ping route
@app.get("/ping")
def ping():
    return {"message": "pong"}

# ✅ Matching logic route
@app.post("/match")
async def match_files(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(...)
) -> Dict:
    # Step 1: Read uploaded files as bytes
    resume_bytes = await resume.read()
    jd_bytes = await job_description.read()

    # Step 2: Convert to dummy text (in real life use PDF parser)
    resume_text = resume_bytes.decode("utf-8", errors="ignore")
    jd_text = jd_bytes.decode("utf-8", errors="ignore")

    # Step 3: Fake GPT scoring logic (mock response for now)
    score = 78  # hardcoded mock score
    feedback = (
        "✅ Good alignment with required skills.\n"
        "❗ Resume could include more measurable impact and tools used in recent roles."
    )

    return {
        "score": score,
        "feedback": feedback
    }
