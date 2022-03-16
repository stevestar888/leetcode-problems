"""
Interesting and kind of silly problem. You can return just the longUrl and shortUrl—and that passes with 100% memory but, surprisingly, not 100% speed—but that’s cheating. 

I made a dictionary that stores {tiny_url : full_url }, where tiny_url is the base_url + #, and I increment # every time we add a new url.
"""
class Codec:
#     def encode(self, longUrl):
#         """Encodes a URL to a shortened URL.
        
#         :type longUrl: str
#         :rtype: str
#         """
#         return longUrl
        

#     def decode(self, shortUrl):
#         """Decodes a shortened URL to its original URL.
        
#         :type shortUrl: str
#         :rtype: str
#         """
#         return shortUrl
        
    def __init__(self):
        self.count = 0
        self.store = {}
        
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        tiny_url = "https://tinyurl.com/{}".format(count)
        self.store[tiny_url] = longUrl
        self.count += 1
        return tiny_url     
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.store[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
