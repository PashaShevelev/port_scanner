import socket
from concurrent import futures
from get_args import pars_arg
from functools import partial


def port_is_open(port, ip, state):
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    con_tcp, con_udp = sock_tcp.connect_ex((ip, port)), sock_udp.connect_ex((ip, port))

    try:
        if not con_tcp and state[0]:
            print(f"TCP {port} {get_protocol(socket.getservbyport(port))}")
        if not con_udp and state[1]:
            print(f"UDP {port} {get_protocol(socket.getservbyport(port))}")
    except OSError:
        if not con_tcp and state[0]:
            print(f"TCP {port}")
        if not con_udp and state[1]:
            print(f"UDP {port}")
    finally:
        sock_tcp.close()
        sock_udp.close()


def port_scanner(left, right, ip, *state):
    for port in range(left, right):
        port_is_open(port, ip, state)


def main():
    args = pars_arg()
    ip = args[0]
    state_tcp, state_udp = args[1:3]
    left, right = args[3]
    border_workers = args[4]
    lo, hi = 0, 65_355
    if lo <= left and right <= hi:
        if left - right > 100:
            with futures.ThreadPoolExecutor(max_workers=border_workers) as executor:
                spawn = partial(executor.submit, port_scanner)
                fs = [spawn(bord_l, bord_l + 100, ip, state_tcp, state_udp) for bord_l in range(left, right + 1, 100)]
                for i in futures.as_completed(fs):
                    i.result()
        else:
            port_scanner(left, right + 1, ip, state)
    else:
        print(f'Range [{left}, {right}] is incorrect.')


if __name__ == '__main__':
    main()
