
Title: Make a Token Info Agent | NEARN

URL Source: http://nearn.io/thebafnetwork/2/


This bounty is part of our effort to highlight what's possible with Shade Agents, autonomous, chain-abstracted AI agents built on NEAR using Chain Signatures. These agents can read, reason, and act across ecosystems without centralized control.

Your task is to build a functional Token Info Agent that can fetch and return real-time token price data based on user queries. Just as important, and staying true to our commitment to open-source documentation, you'll create a clear, beginner-friendly tutorial that anyone can follow.

## Quick Start

**Installation:** `uv pip install -r requirements.txt` (only `requests`)

**Usage example:** 'What's the price of SOL?'

### What You’ll Build

Your Token Info Shade Agent should be able to:

*   Accept natural language prompts such as:

“What’s the price of SOL?”

“How much is 1 ETH in USD?”

*   Query a live token pricing API (such as CoinGecko or CoinMarketCap)

*   Return formatted price data to the user

(Optional) Add features like:

*   Currency conversion between tokens or fiat

*   Prompt parsing for multi-token support

*   A CLI or basic UI interface to display results

*   LLM integration for flexible language processing

### Submission Requirements

Your GitHub PR should include a `/token-info-agent/` folder containing:

*   `README.md` — A full tutorial: setup, logic, usage, and examples

*   `main.py`, `index.js`, or `lib.rs` — Your agent’s core logic in Python, JavaScript, or Rust

*   `prompt_examples.txt` — At least 3 sample user queries and expected outputs

*   `demo.mp4` or Loom/YouTube link — A short video (2–5 min) walking through the agent’s functionality

(Optional) Basic UI wrapper or CLI interface

### Technical Requirements

*   Must be built in JavaScript, Python, or Rust

*   Agent must function autonomously (no manual steps after setup)

*   Code must be open source and submitted via GitHub PR

*   Tutorial must be clear, complete, and reproducible

### Judging Criteria

**Clarity & Reproducibility**

Is your tutorial easy to follow and replicate?

**Agent Autonomy**

Does your agent process prompts and return price data without manual input?

**Code Quality & Logic**

Is your logic well-structured and accurate across test cases?

### Resources

Everything you need to learn about Shade Agents and how they work:

*   [Intro to Shade Agents – NEAR Docs](https://docs.near.org/ai/shade-agents/introduction)

*   [NEAR Blog: The First Truly Autonomous AI Agents](https://www.near.org/blog/shade-agents-the-first-truly-autonomous-ai-agents)

*   [Shade Agents Walkthrough Video with Proximity Labs](https://www.youtube.com/watch?v=04NEXdLz9EE)

*   [CoinGecko API Documentation](https://www.coingecko.com/en/api/documentation)

