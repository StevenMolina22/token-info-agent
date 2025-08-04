# Token Info Agent - A NEAR Shade Agent

A functional autonomous AI agent built on NEAR Protocol using Shade Agents that fetches and returns real-time cryptocurrency token price data based on natural language queries.

## 🚀 Quick Start

```bash
# NearAI setup
pip install nearai  # OR: python3 -m pip install nearai
nearai login # OR nearai login --remote

# Run the agent
nearai registry download arepaehuevo.near/token-info-agent/0.0.19
cd ~/.nearai/registry/arepaehuevo.near/token-info-agent/0.0.19
nearai agent interactive . --local # OR: nearai agent interactive $(pwd) --local

# publish changes
nearai registry upload .

# Example usage
"What's the price of SOL?"
# Output: Solana (SOL) Current Price: $98.45
```

## 📋 Overview

This Token Info Agent is part of the NEAR Shade Agents ecosystem - autonomous, chain-abstracted AI agents that can read, reason, and act across ecosystems without centralized control. The agent accepts natural language prompts about cryptocurrency prices and returns formatted, real-time price data from the CoinGecko API.

### What This Agent Does

- **Natural Language Processing**: Understands various ways users ask about token prices
- **Real-time Data**: Fetches current prices from CoinGecko API
- **Autonomous Operation**: Processes queries and returns results without manual intervention
- **Error Handling**: Gracefully handles API errors and invalid tokens

## 🏗️ Architecture

The project consists of three main components:

### 1. `agent.py` - Main Agent Logic
The core agent that:
- Processes user messages using NEAR AI environment
- Uses LLM to parse natural language queries
- Identifies token names and symbols
- Formats responses consistently

### 2. `coingecko.py` - API Integration
A helper module that:
- Handles CoinGecko API requests
- Implements robust error handling
- Returns price data or None on failure

### 3. `metadata.json` - Agent Configuration
Defines agent metadata including:
- Model configuration (Llama v3.1 70B)
- Framework settings
- Version and description

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Internet connection for API calls

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd token-info-agent
   ```

2. **Test the components**
   ```python
   # Test the CoinGecko API helper
   from coingecko import get_price
   print(get_price('bitcoin'))  # Should return current BTC price
   ```

## 🎯 Usage Examples

The agent supports various natural language queries:

### Basic Price Queries
```
User: "What's the price of Bitcoin?"
Agent: Bitcoin (BTC) Current Price: $113,500.00

User: "How much is SOL?"
Agent: Solana (SOL) Current Price: $161.44

User: "Show me the current price of Ethereum"
Agent: Ethereum (ETH) Current Price: $3,145.30
```

### Symbol Variations
```
User: "What's BTC trading at?"
Agent: Bitcoin (BTC) Current Price: $113,500.00

User: "ETH price please"
Agent: Ethereum (ETH) Current Price: $3,145.30

User: "How much is NEAR worth?"
Agent: Near (NEAR) Current Price: $3.45
```

### Conversational Queries
```
User: "Can you tell me the price of Cardano?"
Agent: Cardano (ADA) Current Price: $0.70

User: "I want to know how much Stellar costs"
Agent: Stellar (XLM) Current Price: $0.85
```

### Error Handling Strategy

The agent implements comprehensive error handling:

1. **API Errors**: Network issues, HTTP errors, malformed responses
2. **Token Recognition**: Invalid or unsupported tokens
3. **Data Parsing**: Malformed price data
4. **User Input**: Non-price related queries

## 🚨 Error Scenarios

### Invalid Tokens
```
User: "How much is INVALIDTOKEN?"
Agent: Sorry, I couldn't find price data for that token. Please try a supported token like Bitcoin (BTC), Ethereum (ETH), or Solana (SOL).
```

### Non-Price Queries
```
User: "What's the weather like?"
Agent: I'm here to help you with cryptocurrency token prices. Please ask about a token price, such as "What's the price of Bitcoin?"
```

### API Failures
```
User: "What's the price of Bitcoin?"
Agent: Sorry, I couldn't fetch the price for bitcoin right now.
```

## 🧪 Testing

### Manual Testing
Use the examples in `prompt_examples.txt` to test various scenarios

### Supported Tokens
The agent supports any token available on CoinGecko's API, including:
- Bitcoin (BTC)
- Ethereum (ETH)
- Solana (SOL)
- Near Protocol (NEAR)
- Cardano (ADA)
- Stellar (XLM)
- And hundreds more...

## 🔮 Future Enhancements

Potential improvements for the agent:

### Core Features
- **Multi-token queries**: "Compare BTC and ETH prices"
- **Historical data**: "What was Bitcoin's price yesterday?"
- **Price alerts**: "Notify me when SOL hits $100"
- **Currency conversion**: "How much is 1 BTC in EUR?"

## 📚 Resources

### Shade Agents Documentation
- [Intro to Shade Agents – NEAR Docs](https://docs.near.org/ai/shade-agents/introduction)
- [NEAR Blog: The First Truly Autonomous AI Agents](https://www.near.org/blog/shade-agents-the-first-truly-autonomous-ai-agents)

### API Documentation
- [CoinGecko API Documentation](https://www.coingecko.com/en/api/documentation)
- [CoinGecko Simple Price Endpoint](https://www.coingecko.com/en/api/documentation#operations-simple-get_simple_price)

---

*Built with ❤️ for the NEAR Protocol ecosystem as part of the Shade Agents bounty program.*
