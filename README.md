# technical-sample
Sample code as per request. This repository shall be made private after a result has been received.

While not specified in the instructions provided, my description for this sample may be vague in areas to avoid referencing the source request and to maintain a level of confidentiality.

This git directory contains a Python code snippet for the "Integrity" core requirement.

Further details on how this code snippet operates can be located within the Python file.


# Reasoning for Core Requirement Selection
I chose to demonstrate the Integrity core requirement because to me, integrity in the provided context is vital. Even if all other components of the context were operational and running at high efficiency, the application would be useless if it is unable to confirm the integrity of files between client and server. 

As such, I explored this requirement in my demonstration, specifically via the use of generated hash digests.

Hashing involves data being passed through a mathematical 'hash' function, generating a condensed, fixed length, string output. If a file with a modified bit is passed in as input, the hash digest (output) of this modified file will vary sigificantly from the raw file hash digest.

As such, utilising hashing and comparing hash digests is an efficient and appropriate way to evaluate the integrity of data stored between two files. It is vastly more efficient than other options, such as evaluating a file's contents line-by-line. Moreover, hashes are not dependent on file type, meaning all file types (from simple .txt files to proprietary files and more) can be compared against each other with no limitation.

In the context of the code demonstration, I have used a SHA256 hash digest comparison. Other hashing methods can be used (such as the MD5 hashing algorithm), however I chose to use SHA256 as this method is widely used and secure.

As such, ultimately I chose to explore the Integrity core requirement via this code demonstration.