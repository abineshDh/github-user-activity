# GitHub User Activity CLI Tool

This is a simple command-line tool to fetch and display the recent public activity of any GitHub user using the GitHub API.

## Features

- Fetches the **latest 10 events** from a user's GitHub activity
- Displays event type, repository, creation time, and commit messages (for push events)
- Handles missing data and errors gracefully

## Usage

### Run the script:

```bash
python github-user-activity.py <github-username>
```

Replace <github-username> with the GitHub username whose recent activity you want to check. The script will fetch and display the latest events in the terminal.

### Example:
```bash
python github-user-activity.py arun_gosling
```
## Output Format
The script will display the following details for each event:

- **Event Type**: Type of activity (e.g., PushEvent, PullRequestEvent, etc.)
- **Repository**: The name of the repository where the activity occurred
- **Creation Time**: When the event was created, formatted as a nicely readable date/time
- **Commit Message** (for push events): The message for the latest commit (if applicable)


