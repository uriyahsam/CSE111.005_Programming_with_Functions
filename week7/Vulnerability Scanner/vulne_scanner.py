import requests
import socket
import ssl
from bs4 import BeautifulSoup

def check_headers(url):
    """Checks the security headers of a given website."""
    response = requests.get(url)
    headers = response.headers
    security_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]
    return {header: headers.get(header, "Missing") for header in security_headers}

def port_scan(domain, ports=[80, 443, 22, 21, 25]):
    """Scans common ports to detect open ones."""
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((domain, port)) == 0:
                open_ports.append(port)
    return open_ports

def ssl_check(domain):
    """Evaluates SSL/TLS security settings."""
    context = ssl.create_default_context()
    try:
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                return ssock.getpeercert()
    except Exception as e:
        return str(e)

def get_server_info(url):
    """Retrieves and analyzes the server details."""
    response = requests.get(url)
    server = response.headers.get("Server", "Unknown")
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "No Title"
    return {"server": server, "title": title}

def run_scan(url):
    """Performs a full security scan on a website."""
    domain = url.split("//")[-1].split("/")[0]
    results = {
        "headers": check_headers(url),
        "open_ports": port_scan(domain),
        "ssl_info": ssl_check(domain),
        "server_info": get_server_info(url)
    }
    return results

if __name__ == "__main__":
    target_url = input("Enter the website URL: ")
    scan_results = run_scan(target_url)
    print(scan_results)
