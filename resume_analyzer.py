import json
from datetime import datetime

def load_json(file):
    try:
        with open(file,"r")as f:
            return json.load(f)
        
    except FileNotFoundError:
        print(f"File not found {file}")
        return{}
    

def analyze_resume(resume,job):
    resume_skills = set(resume.get("skills",[]))
    required_skills = set(job.get("required_skills",[]))

    matched = list(resume_skills & required_skills)
    missing = list(required_skills - resume_skills)

    return matched , missing


def save_report(name,email,job_title,matched,missing):
    now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    report = {
        "name": name,
        "email": email,
        "job_title" : job_title,
        "matched_skills" : matched,
        "missing_skills" : missing,
        "suggetions " : missing,
        "analysed_at" : now
    }

    with open("report.json", "w") as f:
        json.dump(report,f,indent=4)

    print(f"report saved to report.jsons")

def main():
    resume = load_json("resume.json")
    job = load_json("job.json")

    if not resume or not job:
        return
    
    print(f"Analyzing resume for {resume["name"]} - applying for {job["title"]}")
    matched, missing = analyze_resume(resume,job)

    print(f"Matching skills: ",matched)
    print("Missing skills : ", missing)


    if missing:
        print("\n Recomnded to learn: ")
        for skill in missing:
            print(f"Learn {skill}")

    else:
        print("PRfect match")
        save_report(resume["name"],resume["email"],job["title"],matched,missing)
if __name__ == "__main__":
    main()