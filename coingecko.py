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
