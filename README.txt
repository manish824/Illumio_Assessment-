This program processes flow log data and adds tags to each log entry based on a lookup table. It also counts the occurrences of each tag and the combinations of destination ports and protocols.

## Input Files

The program requires three input files:

•⁠  ⁠Sample data is posted in the below files, update the data or replace the file with same name.

1.⁠ ⁠*Flow Logs File*: A file containing flow log entries with information like destination IP, source IP, destination port, protocol number, etc.(flow_logs.txt)
2.⁠ ⁠*Lookup Table File*: A CSV file that maps combinations of destination ports and protocols to specific tags. (lookup.csv)
3.⁠ ⁠*Protocol Numbers*: A CSV file that contains the assigned Internet Protocol Numbers.(protocol-numbers.csv) Source: [https://www.iana.org/assignments/protocol-numbers/protocol-numbers-1.csv](https://www.iana.org/assignments/protocol-numbers/protocol-numbers-1.csv)

## Output File

The program generates an output file that includes the count of each tag applied and the count of each port/protocol combination.

## Assumptions

The program makes the following assumptions:

1.⁠ ⁠The flow log file is in plain text and follows the AWS VPC Flow Log format (Version 2). 
2.⁠ ⁠The protocol numbers in the flow log correspond to the protocol names defined in the IANA protocol list. 
3.⁠ ⁠The destination port and protocol combination in the lookup table are matched case-insensitively with the flow log data.  Format: (dstport,protocol,tag)
4.⁠ ⁠For the count of matches for each port/protocol combination, only the destination port (dstport) is considered.

## Usage

To use the program, follow these steps:

1.⁠ ⁠Make sure you have Python 3.x/ Python installed on your machine.
2.⁠ ⁠Place the required files in the same directory as the program.
3.⁠ ⁠Open a terminal or command prompt and navigate to the directory where the program is located.
4.⁠ ⁠Run the script using the command: ⁠ python3 flow_parser.py ⁠ if python 3 installed, else 'python flow_parser.py' for python.