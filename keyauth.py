import requests
import hashlib

class KeyAuth:
    def __init__(self, name, ownerid, secret, version):
        self.name = name
        self.ownerid = ownerid
        self.secret = secret
        self.version = version
        self.base_url = "https://keyauth.com/api/1.0/"
        self.session_id = None

    def get_checksum(self):
        # Assuming this is a way to verify the integrity of the script
        with open(__file__, 'rb') as f:
            checksum = hashlib.sha256(f.read()).hexdigest()
        return checksum

    def login(self, key):
        url = f"{self.base_url}/login"
        data = {
            "ownerid": self.ownerid,
            "name": self.name,
            "secret": self.secret,
            "version": self.version,
            "key": key,
            "hash": self.get_checksum()
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            self.session_id = response.json().get('sessionid')
            return response.json()
        else:
            return response.json()

if __name__ == "__main__":
    keyauthapp = KeyAuth(
        name="BediumAC",  # Application Name
        ownerid="CqvuLJWKYV",  # Owner ID
        secret="deb1b1f53345d79a059abbd4082dce7d3f86ca1de84172aaf4cf3009128d1663",  # Application Secret
        version="1.0"  # Application Version
    )

    key = input("Enter your key: ")
    result = keyauthapp.login(key)

    if result['success']:
        print("Login successful!")
    else:
        print("Login failed:", result['message'])
