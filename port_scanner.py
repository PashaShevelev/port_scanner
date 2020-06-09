import asyncio
import sys


async def port_is_open(port, _ip='localhost'):
    try:
        reader, writer = await asyncio.open_connection(_ip, port)
        print(f'Port {port} is open')
        writer.close()
    except Exception:
        print(f'Port {port} is close')


def main():
    lo, hi = 0, 65_535
    left, right = tuple(map(int, sys.argv[1:]))
    if lo <= left and right <= hi:
        try:
            loop = asyncio.get_event_loop()
            tasks = [loop.create_task(port_is_open(border_port)) for border_port in range(left, right)]
            loop.run_until_complete(asyncio.wait(tasks))
        except Exception as ex:
            sys.exit(f"An error has occurred: {ex}")
    else:
        print(f'Range [{left}, {right}] is incorrect.')


if __name__ == '__main__':
    main()
