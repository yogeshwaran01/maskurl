"""
Description:
-----------
    This Script Mask the url behind another url

Usage:
-----
    python3 maskurl.py 
    
"""

import sys
import argparse
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
    return post(f"https://is.gd/create.php?format=json&url={big_url}").json()['shorturl']


def MaskUrl(target_url: str, mask_domain: str, keyword: str) -> str:
    """
    Function mask the url with given domain and keyword
    """
    url = Shortner(target_url)
    return f"{mask_domain}-{keyword}@{urlparse(url).netloc + urlparse(url).path}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mask the URL behind the another URL")

    parser.add_argument(
        "--target",
        type=str,
        help="Target URL to Mask (With http or https)",
        required=True,
    )
    parser.add_argument(
        "--mask",
        type=str,
        help="Mask URL (With http or https)",
        required=True,
    )
    parser.add_argument(
        "--keywords",
        type=str,
        help="Keywords (Use (-) instead of whitespace)",
        required=True,
    )

    print(f"\033[91m {banner}\033[00m")

    if len(sys.argv) == 1:
        print("\n")
        target = input("Enter the url (With http or https): ")
        mask = input("Enter the domain name to mask url (With http or https): ")
        keyword = input("Enter the keywords (use '-' instead of whitespace): ")
        print("\n")
    else:
        args = parser.parse_args()
        target = args.target
        mask = args.mask
        keyword = args.keywords

    print(f"\033[91m {MaskUrl(target, mask, keyword)}\033[00m")
