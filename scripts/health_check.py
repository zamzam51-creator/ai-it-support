import shutil 

def check_disk(path="c:\\"):
    """return disk space info for path, in GB."""
    total, used, free = shutil.disk_usage(path)
    gb = 1024 ** 3
    return {
        "check":"disk",
        "total_gb": round(total /gb,1),
        "used_gb": round(used / gb, 1),
        "free_gb": round(free / gb, 1),
    }

print(check_disk())