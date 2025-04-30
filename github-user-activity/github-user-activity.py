import sys
import json
import urllib.request
from datetime import datetime


class GitHubActivityFetcher:
    def __init__(self, username):
        self._api_url = f"https://api.github.com/users/{username}/events"
        self.username = username
        self.parsed_data = None

    def fetch_data(self):
        try:
            response = urllib.request.urlopen(self._api_url)
            data = response.read().decode("utf-8")
            self.parsed_data = json.loads(data)
            print(f"Fetched {len(self.parsed_data)} events.")
        except Exception as e:
            print("Failed to fetch the data:", e)

    def display_events(self):
        if not self.parsed_data:
            print("No data to display.")
            return
        recent_events = self.parsed_data[:10]
        for event in recent_events:
            event_id = event.get("id")
            event_type = event.get("type")
            repo_name = event.get("repo", {}).get("name")
            account_user = event.get("actor", {}).get("login", {})
            created_at_raw = event.get("created_at")
            created_time = datetime.strptime(created_at_raw, "%Y-%m-%dT%H:%M:%SZ")
            formatted_time = created_time.strftime("%B %d, %Y - %I:%M %p")
            print(f"Username    : {account_user}")
            print(f"Event Type  : {event_type}")
            print(f"Event ID    : {event_id}")
            print(f"Repository  : {repo_name}")
            print(f"Created at  : {formatted_time}")
            print("Commit messages:")
            if event_type == 'PushEvent':
                commits = event.get('payload', {}).get('commits', [])
                if commits:
                    for commit in commits:
                        print(" -", commit.get("message"))
                else:
                    print(" - No commits found")
            print("-" * 40)

    def runner(self):
        self.fetch_data()
        self.display_events()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python github-user-activity.py <github-username>")
        sys.exit()

    username = sys.argv[1]
    fetcher = GitHubActivityFetcher(username)
    fetcher.runner()
