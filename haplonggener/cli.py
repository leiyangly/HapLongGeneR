import argparse
import sys
from textwrap import dedent

from .discover import run_discover_mode
from .annotate import run_annotate_mode
from .utils import check_dependencies
from . import __version__


def main():
    description = dedent(
        f"""haplonggener

        Usage:   haplonggener <command> <arguments>
        Version: {__version__}

        Command: discover   Find retrocopied genes
                 annotate   Annotate retrocopied genes
        """
    )

    parser = argparse.ArgumentParser(
        prog="haplonggener",
        usage=argparse.SUPPRESS,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=description,
        add_help=False,
    )

    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS,
                        help="Show this help message and exit.")
    parser.add_argument("-v", "--version", action="version",
                        version=f"%(prog)s {__version__}",
                        help="Show program's version number and exit.")
    parser.add_argument("-g", "--log", dest="log_file", metavar="FILE",
                        help="Write console output to FILE")

    subparsers = parser.add_subparsers(dest="command")

    parser_discover = subparsers.add_parser(
        "discover", add_help=False, usage=argparse.SUPPRESS,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Usage:   haplonggener discover [options]",
        help="Discover retrocopied genes",
    )
    parser_discover._positionals.title = ""
    parser_discover._optionals.title = "Options"
    parser_discover.add_argument("-i", "--in", dest="input", required=True,
                                 help="Input haploid assembly FASTA")
    parser_discover.add_argument("-o", "--out", dest="output", required=True,
                                 help="Output prefix")
    parser_discover.add_argument("-h", "--help", action="help",
                                 default=argparse.SUPPRESS,
                                 help="Show this help message and exit.")

    parser_annotate = subparsers.add_parser(
        "annotate", add_help=False, usage=argparse.SUPPRESS,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Usage:   haplonggener annotate [options]",
        help="Annotate retrocopied genes",
    )
    parser_annotate._positionals.title = ""
    parser_annotate._optionals.title = "Options"
    parser_annotate.add_argument("-i", "--in", dest="input", required=True,
                                 help="Input file with discovered retrocopies")
    parser_annotate.add_argument("-o", "--out", dest="output", required=True,
                                 help="Output annotation file")
    parser_annotate.add_argument("-h", "--help", action="help",
                                 default=argparse.SUPPRESS,
                                 help="Show this help message and exit.")

    parser._action_groups = [g for g in parser._action_groups if g.title != "positional arguments"]

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if len(sys.argv) == 2:
        if sys.argv[1] == "discover":
            parser_discover.print_help(sys.stderr)
            sys.exit(1)
        elif sys.argv[1] == "annotate":
            parser_annotate.print_help(sys.stderr)
            sys.exit(1)

    args = parser.parse_args()

    log_handle = None
    if getattr(args, "log_file", None):
        log_handle = open(args.log_file, "w")
        sys.stdout = _Tee(sys.stdout, log_handle)

    check_dependencies()

    if args.command == "discover":
        run_discover_mode(args.input, args.output)
    elif args.command == "annotate":
        run_annotate_mode(args.input, args.output)

    if log_handle:
        log_handle.close()


class _Tee:
    """Simple stdout splitter."""

    def __init__(self, *streams):
        self.streams = streams

    def write(self, data):
        for s in self.streams:
            s.write(data)

    def flush(self):
        for s in self.streams:
            s.flush()


if __name__ == "__main__":
    main()
