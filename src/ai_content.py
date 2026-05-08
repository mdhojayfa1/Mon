import os
import json
import google.generativeai as genai
import argparse
import datetime
import sys

def load_config():
    """Load affiliate links from config."""
    config_path = "config/settings.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    return {"referral_links": {}, "keywords": {}}

def get_trending_topics():
    """Determine trending topics."""
    today = datetime.date.today().strftime("%B %d, %Y")
    return f"Best Passive Income Apps and Crypto Airdrops for {today}."

def generate_post(api_key, topics, config, dry_run=False):
    """Generate post and inject affiliate links."""
    if dry_run:
        return "Dry Run Title", "Dry run content about " + topics

    if not api_key:
        print("[ERROR] GEMINI_API_KEY missing.")
        return None, None

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Pass config info to AI for injection
    links_info = json.dumps(config.get("referral_links", {}))

    prompt = f"""
    Write a 800-word viral blog post about: {topics}.
    Format: Markdown.

    IMPORTANT: We have the following partner links. Intelligently insert 2-3 of them into the text where they naturally fit:
    {links_info}

    Structure:
    1. Viral Title
    2. Hook Introduction
    3. Step-by-step Guide
    4. Why this is the best for 2025
    5. Call to action
    6. Tags: #money #crypto #ai #lifestyle #passiveincome
    """

    try:
        response = model.generate_content(prompt)
        content = response.text
        lines = content.strip().split('\n')
        title = lines[0].replace('#', '').strip()
        return title, content
    except Exception as e:
        print(f"[ERROR] Gemini Error: {e}")
        return None, None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Execute without calling APIs')
    args = parser.parse_args()

    config = load_config()
    gemini_key = os.environ.get("GEMINI_API_KEY")

    topics = get_trending_topics()
    title, content = generate_post(gemini_key, topics, config, args.dry_run)

    if title and content:
        with open("src/latest_post.md", "w") as f:
            f.write(f"TITLE: {title}\n")
            f.write(content)
        print(f"[SUCCESS] Post generated: {title}")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
