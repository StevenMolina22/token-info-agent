from nearai.agents.environment import Environment
from coingecko import get_price

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

### 1. Natural Language Processing
- Parse user queries to extract token symbols/names
- Handle variations in phrasing and token references
- Support common token symbols (BTC, ETH, SOL, NEAR, etc.)

### 2. API Integration
- Query live token pricing APIs (CoinGecko or CoinMarketCap)
- Fetch current price data in real-time
- Handle API errors gracefully

### 3. Response Formatting
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
- Focus on core functionality over complex features

## Optional Enhancements

If implementing additional features:
- Currency conversion between tokens
- Multi-token queries
- Basic price change information
- Simple CLI or UI interface

## Operational Guidelines

1. **Autonomy**: Operate independently once set up
2. **Reliability**: Provide consistent, accurate responses
3. **Simplicity**: Keep interactions straightforward and user-friendly
4. **Speed**: Return results quickly for better user experience

Your goal is to be a simple, reliable tool for getting real-time cryptocurrency price information through natural language queries.
"""


def extract_symbol(message: str) -> str | None:
    """
    Extract a supported token symbol from the user's message.

    Args:
        message: The message content from which to extract the symbol.

    Returns:
        The extracted symbol if supported, else None.
    """
    token_names = ["bitcoin", "ethereum", "tether", "solana", "near", "cardano", "polkadot"]

    message = message.lower()
    for token in token_names:
        if token in message:
            return token  # Return the first token that matches
    return None


def run(env: Environment):
    user_msg = env.get_last_message()["content"]

    relevant_msg_prompt = f"""
    Identify if the user is asking about the price of any token. Respond with 'Yes' if the user is asking about the price. If not, respond with a message telling him that you are here to help him with the price of tokens.
    user_message = {user_msg}
    """
    response = env.completion([{"role": "user", "content": relevant_msg_prompt}])
    if response.strip().lower() != "yes":
        env.add_reply(response)
        return

    extraction_prompt = f"""
    From the following user message, what is the cryptocurrency they are asking about?
    Respond with ONLY the name. For example: 'bitcoin', 'ethereum', 'solana', 'tether', 'near'.

    User message: "{user_msg}"
    """
    response = env.completion([{"role": "user", "content": extraction_prompt}])
    token_name = response.strip().lower()

    if token_name:
        price = get_price(token_name)
        if price is not None:
            reply = f"{token_name.capitalize()} Current Price: ${price:.2f}"
            env.add_reply(reply)
        else:
            env.add_reply(f"Sorry, I couldn't fetch the price for {token_name} right now.")
    else:
        env.add_reply("Sorry, I don't recognize that token.")

run(env)

