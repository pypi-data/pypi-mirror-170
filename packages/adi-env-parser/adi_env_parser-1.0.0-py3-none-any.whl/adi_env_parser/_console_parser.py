import argparse
import json
import sys
from . import EnvironmentParser


def main():
    arg_parser = argparse.ArgumentParser(
        prog="adi-env-parser",
        description="Parses environment variables with defined prefix and "
                    "creates JSON output from the parsed structure.",
        usage="adi-env-parser -p <prefix> -j <base_json_file>"
        )

    arg_parser.add_argument(
        "--prefix", "-p", type=str, nargs='?', required=False, default=None,
        help="Environment variable prefix. Default: PYENV"
        )
    arg_parser.add_argument(
        "--json", "-j", type=str, nargs='?', required=False, default=None,
        help="JSON formatted file to read as base configuration"
        )
    arg_parser.add_argument(
        "--indent", "-i", type=int, nargs='?', required=False, default=4,
        help="Number of spaces to use for indentation of output JSON string"
        )

    args = arg_parser.parse_args()

    parser_config = {}
    parser_config.update({"prefix": args.prefix}) if args.prefix else None
    parser_config.update({"config_file": args.json}) if args.json else None

    try:
        parser = EnvironmentParser(**parser_config)
        print(json.dumps(parser.configuration, indent=args.indent))
    except FileNotFoundError:
        print(f"File {args.json} not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Unable to parse JSON file {args.json}")
        sys.exit(1)
