import os
import requests
import google.generativeai as genai
import argparse
import datetime

def get_trending_topics():
    """Determine trending topics for maximum engagement."""
    # We focus on crypto airdrops, free money opportunities, and AI tools
    # as these are highly rewarded on Hive/Steemit.
    today = datetime.date.today().strftime("%B %d, %Y")
    topics = f"Crypto Airdrops 2025, Free AI Tools for Productivity, and Passive Income Apps for {today}."
    return topics

def generate_post(api_key, topics, dry_run=False):
    """Generate a high-value blog post using Gemini AI."""
    if dry_run:
        print("Dry run: Skipping Gemini API call.")
        return "Dry Run: The Ultimate Guide to Free Passive Income in 2025", "This is a dry run blog post content about " + topics

    if not api_key:
        print("Error: Gemini API key not provided.")
        return None, None

    # Using the standard generativeai package (ignoring deprecation warning for now as it's the current installed version)
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

    try:
        response = model.generate_content(prompt)
        content = response.text
        lines = content.strip().split('\n')
        # Robust title extraction
        title = lines[0].replace('#', '').strip()
        if not title or len(title) < 5:
            title = "Maximizing Your Digital Income: 2025 Guide"
        return title, content
    except Exception as e:
        print(f"Error generating post: {e}")
        return None, None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='Execute without calling APIs')
    args = parser.parse_args()

    gemini_key = os.environ.get("GEMINI_API_KEY")

    print("Identifying high-value topics...")
    topics = get_trending_topics()

    print("Generating long-form content...")
    title, content = generate_post(gemini_key, topics, args.dry_run)

    if title and content:
        with open("scripts/latest_post.md", "w") as f:
            f.write(f"TITLE: {title}\n")
            f.write(content)
        print(f"Successfully generated post: {title}")
    else:
        print("Failed to generate post.")

if __name__ == "__main__":
    main()
