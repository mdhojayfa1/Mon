import os
import argparse
import sys
from beem import Hive
from beem.exceptions import AccountDoesNotExistsException

def post_to_hive(username, posting_key, title, body, dry_run=False):
    """Post content to the Hive blockchain."""
    if dry_run:
        print("[DRY-RUN] Skipping Hive blockchain broadcast.")
        print(f"[DRY-RUN] Title: {title}")
        return True

    if not username:
        print("[ERROR] HIVE_USERNAME is missing! Please add it to GitHub Secrets.")
        return False
    if not posting_key:
        print("[ERROR] HIVE_POSTING_KEY is missing! Please add it to GitHub Secrets.")
        return False

    print(f"[INFO] Attempting to post to Hive as @{username}...")
    try:
        # Initialize Hive with the posting key
        h = Hive(keys=[posting_key])

        # Tags
        tags = ["technology", "ai", "web3", "hive", "programming", "passiveincome"]

        print("[INFO] Broadcasting to blockchain...")
        h.post(title=title, body=body, author=username, tags=tags, self_vote=True)
        print(f"[SUCCESS] Post published! View it at https://peakd.com/@{username}")
        return True
    except AccountDoesNotExistsException:
        print(f"[ERROR] The Hive account '@{username}' does not exist. Check your spelling.")
        return False
    except Exception as e:
        if "WIF" in str(e):
            print("[ERROR] Invalid Posting Key! Make sure you copied the 'Private Posting Key'.")
        else:
            print(f"[ERROR] Hive Blockchain Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Execute without calling APIs')
    args = parser.parse_args()

    hive_username = os.environ.get("HIVE_USERNAME")
    hive_posting_key = os.environ.get("HIVE_POSTING_KEY")

    if not os.path.exists("scripts/latest_post.md"):
        print("[ERROR] No post found. Run ai_content.py first.")
        sys.exit(1)

    print("[INFO] Loading latest post...")
    try:
        with open("scripts/latest_post.md", "r") as f:
            lines = f.readlines()
            title = lines[0].replace("TITLE: ", "").strip()
            body = "".join(lines[1:])
    except Exception as e:
        print(f"[ERROR] Could not read post file: {e}")
        sys.exit(1)

    if title and body:
        success = post_to_hive(hive_username, hive_posting_key, title, body, args.dry_run)
        if not success:
            sys.exit(1)
    else:
        print("[ERROR] Post file is empty or corrupted.")
        sys.exit(1)

if __name__ == "__main__":
    main()
