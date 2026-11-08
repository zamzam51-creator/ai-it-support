
import requests


def check_web(url):
    try:
        response = requests.get(url, timeout=5)

        status_code = response.status_code

        response_time = (
            response.elapsed.total_seconds() * 1000
        )

        return {
            "url": url,
            "status_code": status_code,
            "response_time_ms": round(response_time, 2),
            "ok": status_code < 400
        }

    except requests.RequestException as error:
        return {
            "url": url,
            "status_code": None,
            "response_time_ms": None,
            "ok": False,
            "error": str(error)
        }


result = check_web("https://example.com")
print(result)
