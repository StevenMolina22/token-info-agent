"""CoinGecko API helper module for fetching token prices."""

import logging
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import json

# Configure logging
logger = logging.getLogger(__name__)

# Symbol to CoinGecko ID mapping for supported tokens
SYMBOL_TO_ID: dict[str, str] = {
    "BTC": "bitcoin",
    "ETH": "ethereum", 
    "SOL": "solana",
    "NEAR": "near"
}

# Symbol to token name mapping for display purposes
SYMBOL_TO_NAME: dict[str, str] = {
    "BTC": "Bitcoin",
    "ETH": "Ethereum", 
    "SOL": "Solana",
    "NEAR": "NEAR Protocol"
}

def get_price(symbol: str) -> float | None:
    """
    Fetch the current USD price for a cryptocurrency token.
    
    Args:
        symbol: Token symbol (e.g., 'BTC', 'ETH', 'SOL', 'NEAR')
        
    Returns:
        Current USD price as float, or None if error occurred
    """
    # Convert symbol to uppercase for consistency
    symbol = symbol.upper()
    
    # Check if symbol is supported
    if symbol not in SYMBOL_TO_ID:
        logger.warning(f"Unsupported token symbol: {symbol}")
        return None
    
    # Get CoinGecko ID for the symbol
    coingecko_id = SYMBOL_TO_ID[symbol]
    
    # Construct API URL
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coingecko_id}&vs_currencies=usd"
    
    try:
        # Make API request
        with urlopen(url) as response:
            data = json.loads(response.read().decode())
            
        # Extract price from response
        price = data[coingecko_id]["usd"]
        return float(price)
        
    except HTTPError as e:
        logger.error(f"HTTP error fetching price for {symbol}: {e}")
        return None
    except URLError as e:
        logger.error(f"Network error fetching price for {symbol}: {e}")
        return None
    except KeyError as e:
        logger.error(f"Unexpected API response structure for {symbol}: {e}")
        return None
    except (ValueError, TypeError) as e:
        logger.error(f"Error parsing price data for {symbol}: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error fetching price for {symbol}: {e}")
        return None
