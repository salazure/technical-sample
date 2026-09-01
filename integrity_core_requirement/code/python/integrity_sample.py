'''

----- OVERVIEW -----
The following section of code has been developed as per the "Integrity" core requirements of the technical scenario assessment.

Prior to testing this code, please review the README.md and ensure the /client_data/ and /server_data/ directories exist and possess data.

If you wish to confirm this code is operational across different directories, change the "client_side" and "server_side" tags in the "config.json" file (within the code directory).


----- ASSUMPTIONS -----
This code segment is to resemble only a section of a larger program and architectural environment.

This segment takes on the role of a 'receiver', whereby it verifies the files it possesses match the files on the client machine.

It assumes these files have already been transferred, with the files existing in two locations: client_data and server_data.

This code also assumes config.json will not move location.

After confirming integrity (or noting down disrepancies), this code will return its results.


FURTHER DETAILS FOR THE JUSTIFICATION OF WHY THIS CORE REQUIREMENT WAS CHOSEN CAN BE FOUND IN THE README.MD WITHIN THIS GIT DIRECTORY

'''

import json
from pathlib import Path
import hashlib

# const holding configuration file name
CONFIG_FILENAME = "config.json"

# global directory paths
client_data_path = ""
server_data_path = ""

# global dictionaries to compare files
# format: {"file1.txt": "[hash digest]"}
client_files = {}
server_files = {}


# initialise loads the directory paths from the config.json file
def initialise():
    global client_data_path, server_data_path

    # get directory where config file exists
    directory = Path(__file__).resolve().parent.parent

    try:
        # open JSON file and set global paths
        with open(directory / CONFIG_FILENAME, "r") as file:
            raw_data = json.load(file)
            client_data_path = directory.parent / raw_data["client_directory"]
            server_data_path = directory.parent / raw_data["server_directory"]
    except FileNotFoundError:
        # if file not found, print error
        print("Could not open file. Please check config.json values match desired directory.")
    else:
        print("Client and server directories located successfully.")


# loads a list of files from a specified directory and generates rows of a dictionary
# this function has been made generic (to handle both client and server) to reduce code duplication
def load_data_from_directory(directory_path, specified_dictionary):
    # load directory to specified path (either client or server files)
    directory = Path(directory_path)

    # print loaded path
    print(f"\n\nLoaded directory path: {directory}")

    # loop files in directory
    for item in directory.iterdir():
        hash_digest = generate_hash_digest(item)
        specified_dictionary[item.name] = hash_digest

        # print output as it is generated
        print(f"\nFilename: {item.name}")
        print(f"Hash digest: {hash_digest}")


# generates and returns a hash digest for a specified file
def generate_hash_digest(filename):
    # the reference below was used to understand how python handles the generation of hashes
    # reference: https://stackoverflow.com/questions/22058048/hashing-a-file-in-python

    # uses hashlib to generate a hash digest via hashing method sha256 (and via opening the file as read binary (rb))
    # for this technical scenario, no minimum security level has been defined, so sha256 has been used as the hashing method
    with open(filename, 'rb', buffering=0) as file:
        return hashlib.file_digest(file, 'sha256').hexdigest()


# draws data from client and server files before comparing to evaluate if integrity is maintained or not
def verify_integrity():
    global client_files, server_files

    # define storage for results
    results = {}

    # loop server_files rows
    for server_filename, server_hash in server_files.items():
        # check if server file is in client_files dictionary
        if server_filename in client_files:
            # if yes, confirm that hash matches
                # as a side note, this comparison is relatively efficient as it evaluates two hash digests against eachother (rather than the whole file data)
            if server_hash == client_files[server_filename]:
                # if the hash digest matches, we can assume both files are the same
                # this assumption is safe to make as a generated hash will vary greatly between two files even if only a single bit was changed/deleted/added
                results[server_filename] = [True, "VALID"]
            else:
                # if hash does not match, this indicates the files have changed or have been modified
                results[server_filename] = [False, "FILE DATA DOES NOT MATCH"]
        else:
            # if file cannot be found, note this result
            results[server_filename] = [False, "NOT ON CLIENT"]

    # loop client_files (to validate all files have been covered and there is no file left behind)
    for client_filename in client_files.keys():
        # check if file exists in server files looped previously
        if client_filename not in results:
            # if no, log this result
            results[client_filename] = [False, "NOT ON SERVER"]

    return results


# this function prints the results collected from "verify_integrity" in a nicer format
def print_output(results):
    # initial header
    print("\n\n-- OUTPUT GENERATED --\n")

    # loop dictionary values by their key and value held within
    for key, value in results.items():
        # print results
        print(f"Filename: {key}")
        print(f"File matches across directories: {value[0]}")
        print(f"Status: {value[1]}\n")


# main function
if __name__ == "__main__":
    # load configuration
    initialise()

    # load data from client and server
    load_data_from_directory(client_data_path, client_files)
    load_data_from_directory(server_data_path, server_files)

    # check integrity of data across both directories
    # generates a short dictionary of filenames against their integrity status
    results = verify_integrity()

    # handle output print
    print_output(results)


    print("Sample demonstration complete. Thank you for testing this sample code.")