"""
Description:
-----------
    This Script Mask the url with given and Keyword

Usage:
-----
    python3 maskurl.py 
    
"""

from urllib.parse import urlparse

from requests import post


banner = r"""
 __  __      _      ____    _  __  _   _   ____    _     
|  \/  |    / \    / ___|  | |/ / | | | | |  _ \  | |    
| |\/| |   / _ \   \___ \  | ' /  | | | | | |_) | | |    
| |  | |  / ___ \   ___) | | . \  | |_| | |  _ <  | |___ 
|_|  |_| /_/   \_\ |____/  |_|\_\  \___/  |_| \_\ |_____|
                                                       
"""


def Shortner(big_url: str) -> str:
    """
    Function short the big urls to short
    """
    return post(f"https://da.gd/s/?url={big_url}").text


def MaskUrl(target_url: str, mask_domain: str, keyword: str) -> str:
    """
    Function mask the url with given domain and keyword
    """
    url = Shortner(target_url)
    return f"{mask_domain}-{keyword}@{urlparse(url).netloc + urlparse(url).path}"


if __name__ == "__main__":
    print(f"\033[91m {banner}\033[00m")
    print("\n")
    target = input("Enter the url (With http or https): ")
    domain = input("Enter the domain name to mask url (With http or https): ")
    keyword = input("Enter the keywords (use '-' instead of whitespace): ")
    print("\n")
    print(f"\033[91m {MaskUrl(target, domain, keyword)}\033[00m")
