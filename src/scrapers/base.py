import requests


class BaseScraper:

    def fetch(self, url):

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/138.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        print("Status Code:", response.status_code)
        print("Final URL :", response.url)

        response.raise_for_status()

        return response.text