class Codec:
    def __init__(self):
        self.map = {}
        self.count = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl1 = 'http://tinyurl.com/'
        self.count += 1
        shortUrl = shortUrl1 + str(self.count)
        self.map[shortUrl] = longUrl
        return shortUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))