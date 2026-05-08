import os
import requests
import google.generativeai as genai
import argparse
import datetime
import sys

def get_trending_topics():
    """Determine trending topics for maximum engagement."""
    print("[INFO] Identifying high-value topics for today...")
    today = datetime.date.today().strftime("%B %d, %Y")
    topics = f"Crypto Airdrops 2025, Free AI Tools for Productivity, and Passive Income Apps for {today}."
    print(f"[INFO] Topics selected: {topics}")
    return topics

def generate_post(api_key, topics, dry_run=False):
    """Generate a high-value blog post using Gemini AI."""
    if dry_run:
        print("[DRY-RUN] Skipping Gemini API call.")
        return "Dry Run: The Ultimate Guide to Free Passive Income in 2025", "This is a dry run blog post content about " + topics

    if not api_key:
        print("[ERROR] GEMINI_API_KEY is missing! Please add it to GitHub Secrets.")
        return None, None

    print("[INFO] Connecting to Gemini AI...")
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        prompt = f"""
        Write a high-quality, 'ultimate guide' style blog post about: {topics}.
        The post must be optimized for Hive/Steemit to earn maximum upvotes (rewards).
        Structure:
        1. Catchy Title (Make it viral)
        2. Introduction (Why this matters now)
        3. Detailed sections with bullet points for readability.
        4. Pro-tips for beginners.
        5. Conclusion with an engaging question.
        6. Tags: #passiveincome #crypto #ai #money #technology

        Format in Markdown.
        Make it at least 600 words for better SEO ranking.
        Do NOT mention that you are an AI.
        """

        print("[INFO] Generating content (this may take a minute)...")
        response = model.generate_content(prompt)
        content = response.text
        lines = content.strip().split('\n')

        # Robust title extraction
        title = lines[0].replace('#', '').strip()
        if not title or len(title) < 5:
            title = "Maximizing Your Digital Income: 2025 Guide"

        print(f"[SUCCESS] Content generated successfully. Title: {title}")
        return title, content
    except Exception as e:
        print(f"[ERROR] Gemini AI Error: {e}")
        return None, None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Execute without calling APIs')
    args = parser.parse_args()

    gemini_key = os.environ.get("GEMINI_API_KEY")

    topics = get_trending_topics()
    title, content = generate_post(gemini_key, topics, args.dry_run)

    if title and content:
        try:
            with open("scripts/latest_post.md", "w") as f:
                f.write(f"TITLE: {title}\n")
                f.write(content)
            print("[INFO] Post saved to scripts/latest_post.md")
        except Exception as e:
            print(f"[ERROR] Failed to save post file: {e}")
            sys.exit(1)
    else:
        print("[ERROR] Post generation failed. Check the logs above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
