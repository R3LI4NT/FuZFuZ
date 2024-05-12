from banner.banner import *
import argparse
import requests
from tqdm import tqdm
from requests.exceptions import RequestException

def FuzFuz(parse):
    with open(parse.wordlist) as file:
        dictionary = file.read().splitlines()

    try: 
        progress = tqdm(total=len(dictionary), desc="\033[1;35mProgress\033[0m", unit="urls", dynamic_ncols=True)

        for line in dictionary:
            url = parse.url + line
            try:
                response = requests.get(url, timeout=5)  # Agregamos un tiempo de espera de 5 segundos
                if response.status_code == 200:
                    tqdm.write(f"{GREEN_NORMAL}Directory Found:{END} {url}")
                #elif response.status_code == 404:
                #    tqdm.write(f"{RED}[ERROR]{END} 404 Not Found: {url}")    
            except RequestException as e:
                tqdm.write(f"{RED}[ERROR]{END} al acceder a {url}: {e}")

            progress.update(1)

    except KeyboardInterrupt:
        print(f"{YELLOW}[!] Script interrupted by the user{END}")

    finally:
        progress.close()
       

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Web directory fuzzing script")
    parser.add_argument("-u", "--url", help="Base URL for fuzzing")
    parser.add_argument("-w", "--wordlist", help="Wordlist path")
    parse = parser.parse_args()

    FuzFuz(parse)
