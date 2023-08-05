# internal
from laz.internal.meta import version


HELP = f'''Laz version {version}

Usage:
  laz [-h] [-v] <command> [<arg1>] ... [<argN>]

Global Options:
  -h (--help)        Display help message
  -v (--verbose)     Increase verbosity of log messages

Available Commands:
  <path>             Configuration/Target path to run arguments against
  help               Display help message
  init               Initialize a directory with an example laz.yml
  show               Show the effective configuration of a given target
  tree               Display tree structure of laz.yml files in current project
  version            Display current Laz package version

Online Documentation: https://joshwycuff.github.io/py-laz/
'''


def help():
    print(HELP)
