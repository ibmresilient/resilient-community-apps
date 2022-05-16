# -*- coding: utf-8 -*-

import os
import sys
from argparse import ArgumentParser

SCRIPT_NAME = os.path.basename(sys.argv[0])

PARSER_DESC = """
Script to print all names of images in ALLOW_IMAGE_NAMES.txt in the format required for SonarQube sources: 'fn_utilities/fn_utilities,fn_urlhaus/fn_urlhaus' to the terminal
"""

PARSER_USAGE = """
$ python {0} ".scripts/ALLOW_IMAGE_NAMES.txt"
$ python {0} ".scripts/ALLOW_IMAGE_NAMES.txt" --ignore-lines "rc-" "rc_data_feed_plugin_odbcfeed" --output .scripts/all_images.txt
""".format(SCRIPT_NAME)


def _get_args():
    """
    Setup and return the arguments used in this script
    """
    parser = ArgumentParser(description=PARSER_DESC)

    parser.usage = PARSER_USAGE

    parser.add_argument("ALLOW_IMAGE_NAMES",
                        help="Absolute path to ALLOW_IMAGE_NAMES.txt",
                        nargs="?",
                        metavar="ALLOW_IMAGE_NAMES.txt",
                        type=str)

    parser.add_argument("-o", "--output",
                        help="Path to file to print output to",
                        nargs="?",
                        type=str)

    parser.add_argument("-i", "--ignore-lines",
                        help="If lines of the file include any of these words, ignore them. E.g. 'rc-' 'rc_data_feed_plugin_odbcfeed'",
                        nargs="*",
                        type=str)

    return parser.parse_args()


def print_msg(msg):
    """
    Print a nicely formatted message surrounded by a divider

    :param msg: The message to print
    :type msg: str
    """
    div = "-----------------------"
    print("\n{0}\n{1}\n{0}\n".format(div, msg))


def main():
    """Main entry point"""

    all_allowed_images, sonar_sources = [], []

    args = _get_args()

    file_to_read = args.ALLOW_IMAGE_NAMES
    lines_to_ignore = args.ignore_lines

    if not os.path.isfile(file_to_read):
        raise IOError("File not found at '{0}'".format(file_to_read))

    with open(file_to_read, mode="r") as the_file:

        lines = the_file.readlines()

        for l in lines:

            l = l.strip()

            if not l or l.startswith("#"):
                continue

            ignore = False

            if lines_to_ignore:
                for ignore_line in lines_to_ignore:
                    if ignore_line in l:
                        ignore = True

            if not ignore:
                all_allowed_images.append(l)

    if not all_allowed_images:
        raise IOError("No image names found in '{0}'. Ensure there are some lines then are not commented out by a '#'".format(file_to_read))

    for image_name in all_allowed_images:
        sonar_sources.append("{0}/{0}".format(image_name))

    all_images_as_str = ",".join(sonar_sources)

    if args.output:
        path_output_file = args.output

        if not os.path.isdir(os.path.dirname(path_output_file)):
            print_msg("Provided output path '{0}' is not a valid directory or the directory does not exist. Not writing file".format(path_output_file))

        else:
            with open(path_output_file, mode="w") as the_file:
                the_file.write(all_images_as_str)

    print(all_images_as_str)

if __name__ == "__main__":
    main()
