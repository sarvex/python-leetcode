# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """


class Solution:
    def crawl(self, startUrl: str, htmlParser: "HtmlParser") -> list[str]:
        """Crawl all URLs under the same hostname starting from startUrl.

        Intuition:
            This is a standard graph traversal problem where each URL is a
            node and links are edges. We restrict traversal to the same host.

        Approach:
            Use DFS starting from startUrl. Extract the hostname from each URL
            and only follow links that share the same hostname. Track visited
            URLs in a set.

        Complexity:
            Time: O(n) where n is the number of URLs
            Space: O(n)
        """

        def extract_host(url: str) -> str:
            return url[7:].split("/")[0]

        def dfs(url: str) -> None:
            if url in visited:
                return
            visited.add(url)
            for next_url in htmlParser.getUrls(url):
                if extract_host(url) == extract_host(next_url):
                    dfs(next_url)

        visited: set[str] = set()
        dfs(startUrl)
        return list(visited)
