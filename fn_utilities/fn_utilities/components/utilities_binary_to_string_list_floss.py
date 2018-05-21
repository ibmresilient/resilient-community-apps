import sys
import tempfile
from floss import main

def get_strings(temp_file_binary):
    # get_strings extracts encoded string from file and returns a list of strings found in the
    # file.  Floss is called to extract the strings.  For more information on Floss:
    # https://github.com/fireeye/flare-floss/blob/master/doc/usage.md
    with tempfile.NamedTemporaryFile(bufsize=0) as temp_file_strings:
        try:
            # Floss writes output to stdout so redirect stdout to temporary file
            save_stdout = sys.stdout
            output_stream = open(temp_file_strings.name.encode("ascii"), 'w')
            sys.stdout = temp_file_strings

            # Call Floss to extract strings from the file.
            # Use commandline arguments: -q for quiet mode so that only the strings
            # are returned, no headers;  -s option directs floss to analyze binary
            # files containing shellcode. See floss documentation for other options
            # you can pass to floss.
            # https://github.com/fireeye/flare-floss/blob/master/doc/usage.md
            result_floss = main.main(['main', '-q', '-s', temp_file_binary.name.encode("ascii")])
            output_stream.close()

            if result_floss != 0:
                raise Exception("Error running floss.")

            try:
                # Read the output from floss and make a list of the decoded strings
                floss_output = open(temp_file_strings.name.encode("ascii"), "r")
                list_string = floss_output.read().splitlines()
            except Exception as err:
                raise err
            finally:
                # Close the file.
                floss_output.close()

        except Exception as err:
            raise err
        finally:
            # Restore stdout and close the file. The temporary file will be deleted on close.
            sys.output = save_stdout
            temp_file_strings.close()

    return list_string

def extract_strings_from_binary(data):
    # extract_strings_from_binary writes binary data to a file and calls get_strings to extract
    # the encoded strings
    with tempfile.NamedTemporaryFile('w', bufsize=0) as temp_file_binary:
        try:
            # Write binary data to a temporary file.
            temp_file_binary.write(data)

            list_string = get_strings(temp_file_binary)
        except Exception as err:
            raise err

        finally:
            # Close the temporary binary file. Closing the temp file will delete it.
            temp_file_binary.close()
    return list_string