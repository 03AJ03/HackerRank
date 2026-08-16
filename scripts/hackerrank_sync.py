import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE_URL = "https://www.hackerrank.com"
USERNAME = "akshat_jain0310"
SESSION = os.environ["HACKERRANK_SESSION"]
MIXPANEL = os.environ.get("HACKERRANK_MIXPANEL_TOKEN", "")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/151.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Referer": f"{BASE_URL}/profile/{USERNAME}",
}

COOKIES = {
    "_hrank_session": SESSION,
}
if MIXPANEL:
    COOKIES["hackerrank_mixpanel_token"] = MIXPANEL


def get_json(url, params=None):
    response = requests.get(
        url,
        params=params,
        headers=HEADERS,
        cookies=COOKIES,
        timeout=30,
    )
    if response.status_code in (401, 403):
        raise RuntimeError(
            "HackerRank authentication failed. Refresh HACKERRANK_SESSION "
            "and HACKERRANK_MIXPANEL_TOKEN."
        )
    response.raise_for_status()
    return response.json()


def get_all_accepted_submissions():
    accepted = []
    offset = 0
    limit = 100

    while True:
        data = get_json(
            f"{BASE_URL}/rest/contests/master/submissions/",
            {"offset": offset, "limit": limit},
        )

        models = data.get("models") or data.get("data") or []
        if not models:
            break

        for submission in models:
            if str(submission.get("status", "")).lower() == "accepted":
                accepted.append(submission)

        if len(models) < limit:
            break

        offset += limit

    return accepted


def get_submission_details(challenge_slug, submission_id):
    url = (
        f"{BASE_URL}/rest/contests/master/challenges/"
        f"{challenge_slug}/submissions/{submission_id}"
    )
    data = get_json(url)
    return data.get("model", data)


def clean_name(value):
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_") or "solution"


def language_info(language):
    lang = (language or "").lower()
    mapping = {
        "python": ("Python", ".py"),
        "python3": ("Python", ".py"),
        "pypy3": ("Python", ".py"),
        "sql": ("SQL", ".sql"),
        "mysql": ("SQL", ".sql"),
        "oracle": ("SQL", ".sql"),
        "db2": ("SQL", ".sql"),
        "java": ("Java", ".java"),
        "java8": ("Java", ".java"),
        "java15": ("Java", ".java"),
        "java17": ("Java", ".java"),
        "cpp": ("C++", ".cpp"),
        "c++": ("C++", ".cpp"),
        "c": ("C", ".c"),
        "csharp": ("C#", ".cs"),
        "c#": ("C#", ".cs"),
        "javascript": ("JavaScript", ".js"),
        "typescript": ("TypeScript", ".ts"),
        "go": ("Go", ".go"),
        "ruby": ("Ruby", ".rb"),
        "php": ("PHP", ".php"),
        "kotlin": ("Kotlin", ".kt"),
        "swift": ("Swift", ".swift"),
        "rust": ("Rust", ".rs"),
    }
    return mapping.get(lang, (language or "Other", ".txt"))


def parse_timestamp(value):
    if value is None:
        return datetime.now(timezone.utc)

    if isinstance(value, (int, float)) or str(value).isdigit():
        return datetime.fromtimestamp(float(value), tz=timezone.utc)

    value = str(value)
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"

    try:
        dt = datetime.fromisoformat(value)
    except ValueError:
        return datetime.now(timezone.utc)

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def git_date(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def commit_with_date(message, timestamp):
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = "03AJ03"
    env["GIT_AUTHOR_EMAIL"] = "203957546+03AJ03@users.noreply.github.com"
    env["GIT_COMMITTER_NAME"] = "03AJ03"
    env["GIT_COMMITTER_EMAIL"] = "203957546+03AJ03@users.noreply.github.com"
    env["GIT_AUTHOR_DATE"] = git_date(timestamp)
    env["GIT_COMMITTER_DATE"] = git_date(timestamp)

    subprocess.run(["git", "commit", "-m", message], check=True, env=env)


def sync_submission(submission):
    challenge = submission.get("challenge") or {}
    slug = challenge.get("slug") or submission.get("challenge_slug")
    title = challenge.get("name") or submission.get("challenge_name") or slug or "solution"

    if not slug:
        print(f"Skipping submission {submission.get('id')}: no challenge slug")
        return False

    submission_id = submission.get("id")
    details = get_submission_details(slug, submission_id)

    code = details.get("code")
    language = details.get("language") or details.get("lang") or submission.get("language")

    if not code:
        print(f"Skipping {title}: code not available")
        return False

    category, extension = language_info(language)
    folder = Path("HackerRank") / category / clean_name(title)
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / f"solution{extension}"

    timestamp = parse_timestamp(
        details.get("created_at")
        or details.get("createdAt")
        or details.get("timestamp")
        or submission.get("created_at")
        or submission.get("timestamp")
    )

    marker = f"HackerRank submission: {submission_id}"
    existing_log = subprocess.run(
        ["git", "log", "--all", "--format=%s", "--grep", marker],
        check=True,
        capture_output=True,
        text=True,
    ).stdout

    if marker in existing_log:
        return False

    changed = False
    if not file_path.exists() or file_path.read_text(encoding="utf-8").strip() != code.strip():
        file_path.write_text(code.rstrip() + "\n", encoding="utf-8")
        subprocess.run(["git", "add", str(file_path)], check=True)
        changed = True

    if changed:
        commit_with_date(f"{marker} - {title}", timestamp)
    else:
        subprocess.run(["git", "commit", "--allow-empty", "-m", f"{marker} - {title}"], check=True)
        # Correct the empty commit date after creating it.
        subprocess.run(["git", "reset", "--soft", "HEAD~1"], check=True)
        subprocess.run(["git", "commit", "--allow-empty", "-m", f"{marker} - {title}"], check=True)

    print(f"SYNCED: {title} [{language}] - {timestamp.date()}")
    return True


def main():
    print(f"Checking HackerRank for {USERNAME}...")
    submissions = get_all_accepted_submissions()
    print(f"Found {len(submissions)} accepted submissions.")

    # Process oldest first so the Git history follows HackerRank chronology.
    submissions.sort(key=lambda x: parse_timestamp(x.get("created_at") or x.get("timestamp")))

    synced = 0
    for submission in submissions:
        try:
            if sync_submission(submission):
                synced += 1
        except Exception as exc:
            title = (submission.get("challenge") or {}).get("name", "unknown")
            print(f"FAILED: {title}: {exc}")

    # Push all commits created during this run.
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print(f"Sync complete. Synced {synced} submission(s).")


if __name__ == "__main__":
    main()
