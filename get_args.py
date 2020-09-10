import argparse


def pars_arg():
    pars = argparse.ArgumentParser()
    pars.add_argument('-ip', default='localhost')
    pars.add_argument('-t', action="store_true")
    pars.add_argument('-u', action="store_true")
    pars.add_argument('-w', default=4, help='max count workers')
    pars.add_argument('-p', '--ports', nargs=2, type=int)
    
    args = pars.parse_args()
    return args.ip, args.t, args.u, args.ports, args.w
