#!/usr/bin/env python3
import urllib.request
import json
from argparse import Namespace, ArgumentParser


class GitHubRepoRelease:
    def __init__(self, repo):
        self.repo = repo
        url = f"https://api.github.com/repos/{repo}/releases/latest"
        self._resp_http = urllib.request.urlopen(url)
        self.release = json.load(self._resp_http)

    def download_urls(self, func=None, keywords=()):
        if keywords:
            func = lambda url: all(kwd in url for kwd in keywords)
        urls = [asset["browser_download_url"] for asset in self.release["assets"]]
        if func:
            urls = [url for url in urls if func(url)]
        return urls


def parse_args(args=None, namespace=None) -> Namespace:
    """Parse command-line arguments.
    """
    parser = ArgumentParser(
        description="Easy installation and configuration for Unix/Linux"
    )
    parser.add_argument(
        "repo",
        help="The GitHub repository of the format owner/project, e.g., dclong/xinstall."
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        default="",
        help="If specified, download the URL and save it to the specified file."
    )
    parser.add_argument(
        "-p",
        "--pip",
        dest="pip",
        action="store_true",
        help="Install the Python package using pip."
    )
    parser.add_argument(
        "-k",
        "--keywords",
        dest="keywords",
        nargs="*",
        default=(),
        help="Keywords in the URL for the purpose of filtering. Note that the first URL is returned so you must specify keywords to narrow down to one URL."
    )
    return parser.parse_args(args=args, namespace=namespace)


def main():
    args = parse_args()
    release = GitHubRepoRelease(args.repo)
    url = release.download_urls(keywords=args.keywords)[0]
    print(url)
    if args.output:
        urllib.request.urlretrieve(url, args.output)


if __name__ == '__main__':
    main()

