import gzip
import json
import os
import re

INPUT_FILE = "akshat_jain0310_data.json.gz"
OUTPUT_DIR = "HackerRank"

EXTENSIONS = {
    "mysql": ".sql",
    "db2": ".sql",
    "python3": ".py",
    "pypy3": ".py",
    "java": ".java",
    "cpp": ".cpp",
    "c": ".c",
    "javascript": ".js"
}

LANGUAGE_FOLDER = {
    "mysql": "SQL",
    "db2": "SQL",
    "python3": "Python",
    "pypy3": "Python",
    "java": "Java",
    "cpp": "CPP",
    "c": "C",
    "javascript": "JavaScript"
}


def clean(name):
    name = re.sub(r'[<>:"/\\\\|?*]', "", name)
    name = name.replace(" ", "_")
    return name


with gzip.open(INPUT_FILE, "rt", encoding="utf-8") as f:
    data = json.load(f)

count = 0

for submission in data["submissions"]:

    language = submission["language"].lower()

    folder = LANGUAGE_FOLDER.get(language, "Other")

    extension = EXTENSIONS.get(language, ".txt")

    challenge = clean(submission["challenge"])

    path = os.path.join(
        OUTPUT_DIR,
        folder,
        challenge
    )

    os.makedirs(path, exist_ok=True)

    filename = os.path.join(path, "solution" + extension)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(submission["code"])

    count += 1

print(f"Exported {count} submissions successfully!")