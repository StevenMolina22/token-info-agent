This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

## Additional Info

# Directory Structure
```
.gitignore
agent.py
coingecko.py
metadata.json
prompt_examples.txt
README.md
```

# Files

## File: prompt_examples.txt
````
Token Info Agent - Sample Queries and Expected Outputs

=== BASIC PRICE QUERIES ===

Query: "What's the price of Bitcoin?"
Expected: Bitcoin (BTC) Current Price: $43,250.00

Query: "How much is SOL?"
Expected: Solana (SOL) Current Price: $98.45

Query: "Show me the current price of Ethereum"
Expected: Ethereum (ETH) Current Price: $2,650.30

=== SYMBOL VARIATIONS ===

Query: "What's BTC trading at?"
Expected: Bitcoin (BTC) Current Price: $43,250.00

Query: "ETH price please"
Expected: Ethereum (ETH) Current Price: $2,650.30

Query: "How much is NEAR worth?"
Expected: Near Protocol (NEAR) Current Price: $3.45

=== CONVERSATIONAL QUERIES ===

Query: "Can you tell me the price of Cardano?"
Expected: Cardano (ADA) Current Price: $0.45

Query: "I want to know how much Stellar costs"
Expected: Stellar (XLM) Current Price: $0.85

=== ERROR SCENARIOS ===

Query: "What's the weather like?"
Expected: I'm here to help you with cryptocurrency token prices. Please ask about a token price, such as "What's the price of Bitcoin?"

Query: "How much is INVALIDTOKEN?"
Expected: Sorry, I couldn't find price data for that token. Please try a supported token like Bitcoin (BTC), Ethereum (ETH), or Solana (SOL).

Note: Prices are examples and will vary based on real-time market data from CoinGecko API.
````

## File: README.md
````markdown
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
````

## File: .gitignore
````
.agents/
**/__pycache__/
.threads/
````

## File: coingecko.py
````python
"""CoinGecko API helper module for fetching token prices."""
import logging
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import json

# Configure logging
logger = logging.getLogger(__name__)

def get_price(name: str) -> float | None:
    """
    Fetch the current USD price for a cryptocurrency token.
    
    Args:
        name: Token name (e.g., 'bitcoin', 'ethereum', 'solana', 'near')
        
    Returns:
        Current USD price as float, or None if error occurred
    """
    token_name = name.lower()
    
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_name}&vs_currencies=usd"
    
    try:
        # Make API request
        with urlopen(url) as response:
            data = json.loads(response.read().decode())
            
        # Extract price from response
        price = data[token_name]["usd"]
        return float(price)
        
    except HTTPError as e:
        logger.error(f"HTTP error fetching price for {token_name}: {e}")
        return None
    except URLError as e:
        logger.error(f"Network error fetching price for {token_name}: {e}")
        return None
    except KeyError as e:
        logger.error(f"Unexpected API response structure for {token_name}: {e}")
        return None
    except (ValueError, TypeError) as e:
        logger.error(f"Error parsing price data for {token_name}: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error fetching price for {token_name}: {e}")
        return None
````

## File: metadata.json
````json
{
  "name": "token-info-agent",
  "version": "0.0.19",
  "description": "The agent can fetch and return real-time token price data based queries",
  "category": "agent",
  "tags": [],
  "details": {
    "agent": {
      "defaults": {
        "model": "llama-v3p1-70b-instruct",
        "model_provider": "fireworks",
        "model_temperature": 1.0,
        "model_max_tokens": 16384
      },
      "framework": "minimal"
    }
  },
  "show_entry": true
}
````

## File: agent.py
````python
from nearai.agents.environment import Environment
from coingecko import get_price

def run(env: Environment):
    user_msg = env.get_last_message()["content"]

    SYSTEM_PROMPT = """
    # Token Info Agent System Prompt

    You are a Token Info Agent built as a Shade Agent on NEAR Protocol. Your primary function is to fetch and return real-time cryptocurrency token price data based on natural language user queries.

    ## Core Function

    **Primary Task**: Accept natural language prompts about token prices and return formatted price data from live APIs.

    ## Supported Query Types

    Handle these types of natural language requests:
    - "What's the price of SOL?"
    - "How much is 1 ETH in USD?"
    - "Show me the current Bitcoin price"
    - "What's NEAR trading at?"

    ## Required Capabilities

    ### Natural Language Processing
    - Parse user queries to extract token symbols/names
    - Handle variations in phrasing and token references
    - Support common token symbols (BTC, ETH, SOL, NEAR, etc.)

    ### Response Formatting
    Return price data in a clear, consistent format including:
    - Token name and symbol
    - Current USD price
    - Basic formatting for readability

    ## Response Format

    For price queries, respond with:
    ```
    [Token Name] ([SYMBOL])
    Current Price: $[price]
    ```

    Example:
    ```
    Solana (SOL)
    Current Price: $98.45
    ```

    ## Error Handling

    - If token not found: "Sorry, I couldn't find price data for that token."
    - If API error: "Unable to fetch price data right now. Please try again."
    - If unclear query: "Please specify which token you'd like price information for."

    ## Technical Constraints

    - Must function autonomously without manual intervention
    - Process queries and return results automatically
    - Maintain simple, reliable operation

    ## Operational Guidelines

    1. **Autonomy**: Operate independently
    2. **Reliability**: Provide consistent, accurate responses
    3. **Simplicity**: Keep interactions straightforward and user-friendly

    Your goal is to be a simple, reliable tool for getting real-time cryptocurrency price information through natural language queries.
    """

    msg_prompt = f"""
    Identify if the user is asking about the price of any token. Repond with "Yes" (Without any extra symbol or space) is the user is asking aobut the price. If not, repond with a message telling them that you are here to help them with price of tokens.
    User message: "{user_msg}"
    """
    response = env.completion([{"role": "user", "content": SYSTEM_PROMPT + msg_prompt}])
    if response.strip().lower() != "yes":
        env.add_reply(response)
        return

    token_name_prompt = f"""
    From the following user message, what is the cryptocurrency they are asking about?
    For example: "bitcoin", "ethereum", "solana", "cardano", "stellar", "tether", "near".
    Return exactly the token name and token symbol as a single string in the format: "<token_name> <token_symbol>".
    Use a single space between the name and symbol. Do not include any additional text, punctuation, or outputs.
    Example output:
        - "bitcoin BTC"
        - "ethereum ETH"
        - "solana SOL"
    User message: "{user_msg}"
    """
    response = env.completion([{"role": "user", "content": SYSTEM_PROMPT + token_name_prompt}])
    token_name, token_symbol = response.split()
    if token_name:
        price = get_price(token_name)
        if price is not None:
            reply = f"{token_name.capitalize()} ({token_symbol}) Current Price: {price:.2f}"
            env.add_reply(reply)
        else:
            env.add_reply(f"Sorry, I couldn't fetch the price for {token_name} right now.")
    else:
        env.add_reply("Sorry, I don't recognize that token.")

run(env)
````
