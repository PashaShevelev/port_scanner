import argparse


def pars_arg():
    pars = argparse.ArgumentParser()
    pars.add_argument('-t', action="store_true")
    pars.add_argument('-u', action="store_true")
    pars.add_argument('-p', '--ports', nargs=2, type=int)
    args = pars.parse_args()
    return args.t, args.u, args.ports
