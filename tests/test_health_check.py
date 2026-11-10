from scripts.health_check import check_disk, check_dns, check_port, check_website


def test_check_disk_reports_usage():
    result = check_disk()
    assert result["check"] == "disk"
    assert 0 <= result["used_percent"] <= 100


def test_check_dns_good_domain():
    result = check_dns("example.com")
    assert result["ok"] is True


def test_check_dns_bad_domain():
    result = check_dns("this-domain-does-not-exist-12345.com")
    assert result["ok"] is False
    assert "Could not resolve" in result["detail"]


def test_check_port_open():
    result = check_port("example.com", 443)
    assert result["ok"] is True


def test_check_website_ok():
    result = check_website("https://example.com")
    assert result["ok"] is True
    assert result["detail"].startswith("200")