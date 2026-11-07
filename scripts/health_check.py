import shutil 
import socket

def check_disk(path="c:\\"):
    """Return disk space info for path, in GB."""
    total, used, free = shutil.disk_usage(path)
    gb = 1024 ** 3
    return {
        "check":"disk",
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
        
print(check_disk())
print(check_dns("example.com"))
print(check_dns("this-domain-does-not-exist-12345.com"))
print(check_port("example.com"))
print(check_port("example.com", 81))