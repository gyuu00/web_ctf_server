import socket
import subprocess
import threading
import os
import shutil
from datetime import datetime

PORT_BASE = 10000

def build_and_run(username):
    container_name = f"webctf_{username}"
    port = PORT_BASE + int(username[-2:], 36) % 1000  # 포트 충돌 방지

    build_dir = f"/tmp/build_{username}_{datetime.now().timestamp()}"
    shutil.copytree("Command_Cloud", build_dir)

    # Docker build
    subprocess.run(["docker", "build", "-t", container_name, build_dir], check=True)

    # Docker run
    subprocess.run([
        "docker", "run", "-d",
        "--name", container_name,
        "-p", f"{port}:5000",
        "--memory", "256m",
        "--cpus", "0.5",
        container_name
    ], check=True)

    return port

def handle_client(conn, addr):
    conn.sendall(b"[CTF Server] Username: ")
    username = conn.recv(1024).decode().strip()

    try:
        port = build_and_run(username)
        public_ip = subprocess.getoutput("curl -s ifconfig.me")
        url = f"http://{public_ip}:{port}"
        conn.sendall(f"\n[+] 컨테이너 생성 완료!\n[+] 웹 접속: {url}\n".encode())
    except Exception as e:
        conn.sendall(f"[!] 오류 발생: {e}\n".encode())
    finally:
        conn.close()

def main():
    print("[*] 대기 중 (port 9999)...")
    s = socket.socket()
    s.bind(("0.0.0.0", 9999))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
