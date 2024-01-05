# proxy_checker.py
import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector, ProxyType

async def check_proxy(proxy):
    """
    Check the functionality of a single proxy by attempting to connect to a website.

    Importing the Method:
    ---------------------
    - Ensure you have the 'aiohttp' and 'aiohttp_socks' libraries installed in your Python environment:
      `pip install aiohttp aiohttp_socks`
    - Place this 'proxy_checker.py' script in the 'Modules' folder within your project directory.
    - Import this function into your main application script using: `from Modules.proxy_checker import check_proxy`.

    Args:
        proxy (str): The proxy address in the format 'ip:port'.

    Returns:
        bool: True if the proxy was able to connect successfully, False otherwise.

    Usage Example:
    --------------
    # Import the method from the Modules folder
    from Modules.proxy_checker import check_proxy

    # Check a single proxy
    result = asyncio.run(check_proxy("127.0.0.1:8080"))
    print(f"Proxy is {'working' if result else 'not working'}.")

    Notes:
    ------
    - This function tests the proxy by trying to connect to http://www.google.com. The target URL can be changed as needed.
    - SOCKS5 proxies are assumed by default. Modify the 'proxy_type' argument for different proxy types.
    """
    ip, port = proxy.split(':')
    print(f"Trying proxy {proxy}...")
    connector = ProxyConnector(
        proxy_type=ProxyType.SOCKS5,
        host=ip,
        port=int(port),
        rdns=True
    )
    try:
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get('http://www.google.com', timeout=10) as response:
                if response.status == 200:
                    print(f"Proxy {proxy} is working.")
                    return True
                else:
                    print(f"Proxy {proxy} failed with status code {response.status}.")
                    return False
    except asyncio.TimeoutError:
        print(f"Proxy {proxy} timed out.")
        return False
    except Exception as e:
        print(f"Proxy {proxy} failed. Error: {e}")
        return False

async def check_proxies(proxies):
    """
    Check the functionality of multiple proxies concurrently.

    Importing the Method:
    ---------------------
    - Ensure you have the 'aiohttp' and 'aiohttp_socks' libraries installed in your Python environment:
      `pip install aiohttp aiohttp_socks`
    - Place this 'proxy_checker.py' script in the 'Modules' folder within your project directory.
    - Import this function into your main application script using: `from Modules.proxy_checker import check_proxies`.

    Args:
        proxies (list): A list of proxy addresses in the format ['ip:port', 'ip:port', ...].

    Returns:
        list: A list of boolean values corresponding to each proxy's status (True if working, False otherwise).

    Usage Example:
    --------------
    # Import the method from the Modules folder
    from Modules.proxy_checker import check_proxies

    # Check multiple proxies
    proxies = ["127.0.0.1:8080", "192.168.1.1:8080"]
    results = asyncio.run(check_proxies(proxies))
    for proxy, result in zip(proxies, results):
        print(f"{proxy} is {'working' if result else 'not working'}.")

    Notes:
    ------
    - This function tests each proxy by trying to connect to http://www.google.com concurrently.
    - SOCKS5 proxies are assumed by default. Modify the 'proxy_type' argument for different proxy types.
    """
    tasks = [check_proxy(proxy) for proxy in proxies]
    results = await asyncio.gather(*tasks)
    return results

# This part is just for direct module testing
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        proxies = sys.argv[1].split(',')  # Pass proxies as comma-separated values
        asyncio.run(check_proxies(proxies))
    else:
        print("Please provide proxies as a comma-separated list.")
