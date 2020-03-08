import socket, socks, requests


def main():
    socks.set_default_proxy(socks.SOCKS5, "lqcode.com", 1080)
    socket.socket = socks.socksocket
    print(requests.get('http://127.0.0.1:1080').text)


if __name__ == '__main__':
    main()