def extract_skills(text):
    keyword_skills = [
        "python", "java", "sql", "html", "css", "javascript",
        "c++", "c#", "tensorflow", "pandas", "numpy", "flask", "streamlit",
        "git", "docker", "linux", "power bi", "excel"
    ]
    text = text.lower()
    extracted = [skill for skill in keyword_skills if skill in text]
    return extracted
