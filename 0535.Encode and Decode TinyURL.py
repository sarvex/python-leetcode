from collections import defaultdict


class Codec:
    """URL shortener using incremental ID mapping.

    Intuition:
        Assign each URL a unique integer ID and use it as the short URL key.
        Store the mapping for decoding.

    Approach:
        On encode, increment a counter and store the mapping from ID to URL.
        On decode, extract the ID from the short URL and look up the original.

    Complexity:
        Time: O(1) for both encode and decode
        Space: O(n) where n is number of encoded URLs
    """

    def __init__(self) -> None:
        self.url_map: dict[str, str] = defaultdict()
        self.counter = 0
        self.domain = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        self.counter += 1
        self.url_map[str(self.counter)] = longUrl
        return f"{self.domain}{self.counter}"

    def decode(self, shortUrl: str) -> str:
        url_id = shortUrl.split("/")[-1]
        return self.url_map[url_id]
