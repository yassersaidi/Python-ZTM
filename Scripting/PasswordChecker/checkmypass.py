import requests
import hashlib
import sys


CHECK_API = 'https://api.pwnedpasswords.com/range/'

def request_api_data(query_char):
    res = requests.get(CHECK_API+query_char)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching data: {res.status_code}')
    return res

def check_password(hashes, hash_to_check)->int:
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash,count in hashes:
        if hash == hash_to_check:
            return int(count)
    return 0
def pwned_api_check(password)->bool:
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    print("Checking..")
    response = request_api_data(first5_char)
    print("\n------RESULTS------\n")
    count = check_password(response,tail)
    if count>0:
        print(f"{password} was found {count} times... you should change your password!")
        return True
    else:
        print(f"{password} was NOT found.. you can keep it!")
        return False

def main():
    password = input("Enter a password you wanna check: ")
    pwned_api_check(password)
    print("\n------END------\n")

if __name__ == '__main__':
    sys.exit(main())
