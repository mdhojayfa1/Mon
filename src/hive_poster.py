import os
import argparse
import sys
from beem import Hive, Steem
from beem.exceptions import AccountDoesNotExistsException

def post_to_blockchain(chain_type, username, posting_key, title, body, dry_run=False):
    """Post content to Hive or Steemit blockchain."""
    chain_name = "Hive" if chain_type == "hive" else "Steemit"

    if dry_run:
        print(f"[DRY-RUN] Skipping {chain_name} broadcast.")
        return True

    if not username or not posting_key:
        print(f"[SKIP] {chain_name} credentials not set.")
        return True

    print(f"[INFO] Attempting to post to {chain_name} as @{username}...")
    try:
        if chain_type == "hive":
            client = Hive(keys=[posting_key])
        else:
            # Note: Steem might require different nodes, but beem handles basic ones
            client = Steem(keys=[posting_key])

        tags = ["technology", "ai", "web3", "passiveincome", "money"]

        client.post(title=title, body=body, author=username, tags=tags, self_vote=True)
        print(f"[SUCCESS] {chain_name} post published!")
        return True
    except Exception as e:
        print(f"[ERROR] {chain_name} Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Execute without calling APIs')
    args = parser.parse_args()

    # Credentials for Hive
    hive_user = os.environ.get("HIVE_USERNAME")
    hive_key = os.environ.get("HIVE_POSTING_KEY")

    # Credentials for Steemit
    steem_user = os.environ.get("STEEM_USERNAME")
    steem_key = os.environ.get("STEEM_POSTING_KEY")

    if not os.path.exists("src/latest_post.md"):
        print("[ERROR] No post found. Run ai_content.py first.")
        sys.exit(1)

    with open("src/latest_post.md", "r") as f:
        lines = f.readlines()
        title = lines[0].replace("TITLE: ", "").strip()
        body = "".join(lines[1:])

    print(f"[INFO] Broadcasting '{title}' to blockchains...")

    # Post to both
    post_to_blockchain("hive", hive_user, hive_key, title, body, args.dry_run)
    post_to_blockchain("steem", steem_user, steem_key, title, body, args.dry_run)

if __name__ == "__main__":
    main()
