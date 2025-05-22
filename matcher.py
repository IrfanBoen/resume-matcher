import pandas as pd

def match_jobs(user_skills):
    df = pd.read_csv("job_database.csv")
    matched_jobs = []

    for _, row in df.iterrows():
        job_title = row["Job Title"]
        required_skills = [skill.strip() for skill in row["Skills"].split(",")]
        overlap = set(user_skills).intersection(set(required_skills))
        if overlap:
            matched_jobs.append(f"{job_title} (matched: {', '.join(overlap)})")

    return matched_jobs
