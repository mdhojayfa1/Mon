# 🤖 Automated AI Passive Income System

Welcome to your new automated income stream! This repository uses cutting-edge AI and Blockchain technology to generate money for you while you sleep. It is designed to be **"set and forget,"** **100% free,** and **completely safe** for your GitHub account.

---

## 🧐 What is this?
This system is an **Automated Content Creator**.
1. **The Brain (AI):** Every day, the system scans for trending high-value topics (like new AI tools, crypto airdrops, and finance tips).
2. **The Writer (Gemini):** It uses Google's powerful Gemini AI to write professional, engaging, and long-form blog posts.
3. **The Payout (Hive):** It automatically publishes these posts to the **Hive Blockchain**.
4. **The Money:** On the Hive blockchain, users get rewarded with cryptocurrency (HBD and HIVE) when others see or upvote their content. These rewards are then paid out directly to your digital wallet.

---

## 🛠️ Step-by-Step Setup Guide

Follow these steps exactly to activate your income stream.

### Step 1: Get your AI Brain (Google Gemini API)
*This is free and takes 1 minute.*
1. Go to **[Google AI Studio](https://aistudio.google.com/app/apikey)**.
2. Sign in with your Google account.
3. Click on **"Create API key"**.
4. Copy the long code (your API Key).
5. **Save this key.** You will need it in Step 3.

### Step 2: Get your Payout Account (Hive Blockchain)
*This is your digital wallet where the money goes.*
1. Go to **[InLeo.io](https://inleo.io/signup)** or **[Ecency.com](https://ecency.com/signup)**.
2. Create a free account (you can use your Google or Email).
3. Once logged in, go to your **Wallet** or **Profile Settings**.
4. Look for **"Keys and Permissions"**.
5. Find your **"Private Posting Key"** (It usually starts with the number `5`).
    - *Warning: Never share your "Active" or "Owner" keys. You only need the **Posting Key** for this.*
6. **Copy your Username and Private Posting Key.**

### Step 3: Connect Everything to GitHub
*This activates the automation.*
1. Go to the top of **this GitHub page**.
2. Click on the **Settings** tab (next to "Actions").
3. On the left sidebar, click **Secrets and variables** > **Actions**.
4. Click the green button: **New repository secret**.
5. Add the following **3 secrets** one by one:

| Secret Name | Secret Value |
| :--- | :--- |
| `GEMINI_API_KEY` | Paste the key from **Step 1** |
| `HIVE_USERNAME` | Your Hive username (e.g., `user123`) |
| `HIVE_POSTING_KEY` | Paste the Private Posting Key from **Step 2** |

---

## 🚀 How it Works (The Workflow)
Once the secrets are added, everything happens automatically:
- **Daily Posting:** Every day at 10:00 AM UTC, the AI will generate a new post and publish it.
- **Auto-Maintenance:** Every Sunday, the repo refreshes itself to stay "active" and keep GitHub's automation happy.
- **No Limits:** This uses very little of your free GitHub minutes, so it will run forever for free.

## 📈 How to See Your Earnings
You don't need to check GitHub. Just log in to your Hive account on **[PeakD.com](https://peakd.com)** or **[Ecency.com](https://ecency.com)**.
- You will see your new posts appearing daily.
- You will see "Rewards" appearing on your posts after 7 days.
- You can withdraw these rewards to any crypto exchange (like Binance or Coinbase) and turn them into your local currency ($).

---

## ❓ FAQ & Troubleshooting
- **Is it really free?** Yes. Google Gemini has a free tier, Hive posting is free, and GitHub Actions are free.
- **Can I get banned?** No. This method follows all rules. We avoid "bandwidth sharing" or "mining" which are the common reasons for bans.
- **What if it doesn't post?** Go to the **"Actions"** tab on GitHub. Click on `AI Reward Poster`. If there is a red error, it will tell you if your API key or Username is wrong.

**You are all set! Now go back to sleep, and let the AI work for you.** 💸
