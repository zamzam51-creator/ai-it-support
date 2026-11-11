import json
import shutil
import socket
import sys

import requests


def check_disk(path="C:\\"):
    """Return disk space info for path, in GB."""
    try:
        total, used, free = shutil.disk_usage(path)
    except OSError:
        return {"check": "disk", "ok": False, "detail": f"Could not read disk {path}"}
    gb = 1024 ** 3
    return {
        "check": "disk",
        "total_gb": round(total / gb, 1),
        "used_gb": round(used / gb, 1),
        "free_gb": round(free / gb, 1),
        "used_percent": round(used / total * 100, 1),
        "free_percent": round(free / total * 100, 1),
        "ok": used / total < 0.9,
    }


def check_dns(host):
    """Look up the IP address for host."""
    try:
        ip = socket.gethostbyname(host)
        return {"check": "dns", "ok": True, "detail": ip}
    except socket.gaierror:
        return {"check": "dns", "ok": False, "detail": f"Could not resolve {host}"}


def check_port(host, port=443):
    """Check whether a TCP port is open on host."""
    try:
        with socket.create_connection((host, port), timeout=3):
            return {"check": "port", "ok": True, "detail": f"{host}:{port} is open"}
    except OSError:
        return {"check": "port", "ok": False, "detail": f"{host}:{port} is closed or unreachable"}


def check_website(url):
    """Check that url responds, and report status code and response time."""
    try:
        response = requests.get(url, timeout=5)
        ms = round(response.elapsed.total_seconds() * 1000)
        return {
            "check": "website",
            "ok": response.status_code < 400,
            "detail": f"{response.status_code} in {ms} ms",
        }
    except requests.RequestException:
        return {"check": "website", "ok": False, "detail": f"Could not reach {url}"}


def run_all_checks(host):
    """Run every check against host and return a list of results."""
    return [
        check_disk(),
        check_dns(host),
        check_port(host),
        check_website(f"https://{host}"),
    ]


def save_report(results, filename="report.json"):
    """Save results to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = "example.com"

    results = run_all_checks(host)
    print(json.dumps(results, indent=2))
    save_report(results)

    passed = 0
    for result in results:
        if result["ok"]:
            passed += 1
    print(f"{passed} of {len(results)} checks passed")
    print("Report saved to report.json")
