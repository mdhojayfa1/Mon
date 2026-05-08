import os
import argparse
from beem import Hive
from beem.exceptions import AccountDoesNotExistsException

def post_to_hive(username, posting_key, title, body, dry_run=False):
    """Post content to the Hive blockchain."""
    if dry_run:
        print("Dry run: Skipping Hive blockchain broadcast.")
        print(f"Title: {title}")
        return True

    if not username or not posting_key:
        print("Error: Hive username or posting key not provided.")
        return False

    try:
        # Initialize Hive with the posting key
        h = Hive(keys=[posting_key])

        # Tags are usually the last part of the body in our generator,
        # but Hive likes them explicitly in metadata too.
        # We'll just use a default list and let the body tags do the work.
        tags = ["technology", "ai", "web3", "hive", "programming"]

        h.post(title=title, body=body, author=username, tags=tags, self_vote=True)
        print(f"Successfully posted to Hive: {title}")
        return True
    except AccountDoesNotExistsException:
        print(f"Error: Account {username} does not exist.")
        return False
    except Exception as e:
        print(f"Error posting to Hive: {e}")
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Execute without calling APIs')
    args = parser.parse_args()

    hive_username = os.environ.get("HIVE_USERNAME")
    hive_posting_key = os.environ.get("HIVE_POSTING_KEY")

    if not os.path.exists("scripts/latest_post.md"):
        print("No post found to upload. Run ai_content.py first.")
        return

    with open("scripts/latest_post.md", "r") as f:
        lines = f.readlines()
        title = lines[0].replace("TITLE: ", "").strip()
        body = "".join(lines[1:])

    if title and body:
        post_to_hive(hive_username, hive_posting_key, title, body, args.dry_run)
    else:
        print("Invalid post format.")

if __name__ == "__main__":
    main()
