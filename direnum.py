import requests
import argparse
import sys

def check_directory(base_url, directory, verbose):
    dir_enum = f"http://{base_url}/{directory}.html"
    r = requests.get(dir_enum)
    
    if r.status_code == 404:
        pass
    else:
        if verbose:
            print("Valid directory:", dir_enum)
        else:
            print("Valid directory:", directory)

def main():
    parser = argparse.ArgumentParser(description="Check directories for validity.")
    parser.add_argument("base_url", help="Base URL to check directories against")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbosity")
    args = parser.parse_args()

    sub_list = open("<YOUR_LIST.TXT>").read()
    directories = sub_list.splitlines()

    for dir in directories:
        check_directory(args.base_url, dir, args.verbose)

if __name__ == "__main__":
    main()
