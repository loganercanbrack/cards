# handler_functions.py
import platform
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

def launch_firefox_with_settings(proxy, user_agent):
    options = Options()

    if user_agent:
        options.set_preference("general.useragent.override", user_agent)

    if proxy:
        ip_port = proxy.split(':')
        if len(ip_port) == 2:
            ip, port = ip_port
            firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
            firefox_capabilities['marionette'] = True

            firefox_proxy = Proxy({
                'proxyType': ProxyType.MANUAL,
                'httpProxy': proxy,
                'ftpProxy': proxy,
                'sslProxy': proxy,
            })
            firefox_proxy.add_to_capabilities(firefox_capabilities)

            driver = webdriver.Firefox(capabilities=firefox_capabilities, options=options, executable_path=get_geckodriver_path())
        else:
            return "Invalid proxy format. Should be ip:port."
    else:
        driver = webdriver.Firefox(options=options, executable_path=get_geckodriver_path())

    try:
        driver.get("http://www.whatsmyua.info/")
        return "Browser launched successfully."
    except Exception as e:
        return f"Failed to launch browser: {e}"

def get_geckodriver_path():
    os_type = platform.system().lower()
    arch, _ = platform.architecture()

    base_path = "GeckoDriver/Firefox/v0.34.0/geckodriver-"

    if os_type == "windows":
        return base_path + ("win-aarch64" if "64" in arch else "win32")
    elif os_type == "darwin" and "arm":
        return base_path + ("macos-aarch64" if "64" in arch else "macos")
    elif os_type == "linux":
        return base_path + ("linux-aarch64" if "64" in arch else "linux32" if "32" in arch else "linux64")
    else:
        raise Exception("Unsupported OS")

def check_current_settings():
    # Placeholder function. Implement as needed.
    return "Current Proxy", "Current User Agent"
