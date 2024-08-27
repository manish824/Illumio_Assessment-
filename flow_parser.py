import csv
from collections import defaultdict

prtl_map = {}

with open('protocol-numbers.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        prtl_number = row[0].strip()
        prtl_name = row[1].strip().lower()
        prtl_map[prtl_number] = prtl_name

def load_lookup_table(lookup_file):
    lookup_table = defaultdict(lambda: "Untagged")
    with open(lookup_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dstport = row['dstport'].strip()
            protocol = row['protocol'].strip().lower()
            tag = row['tag'].strip()
            lookup_table[(dstport, protocol)] = tag
    return lookup_table

def parse_flow_logs(flow_file, lookup_table):
    tag_counts = defaultdict(int)
    port_prtl_counts = defaultdict(int)

    with open(flow_file, 'r') as file:
        for line in file:
            flds = line.strip().split()
            dstport = flds[6]
            prtl_number = flds[7].strip()  
            prtl = prtl_map.get(prtl_number, 'unknown').lower()

            tag = lookup_table.get((dstport, prtl), "Untagged")

            tag_counts[tag] += 1
            port_prtl_counts[(dstport, prtl)] += 1

    return tag_counts, port_prtl_counts

def write_output(tag_counts, port_prtl_counts, output_file):
    with open(output_file, 'w') as file:
        file.write("Tag Counts:\nTag,Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")

        file.write("\nPort/Protocol Combination Counts:\nPort,Protocol,Count\n")
        for (port, prtl), count in port_prtl_counts.items():
            file.write(f"{port},{prtl},{count}\n")

def main():
    lookup_file = 'lookup.csv'
    flow_file = 'flow_logs.txt'
    output_file = 'output_file.txt'

    lookup_table = load_lookup_table(lookup_file)

    tag_counts, port_prtl_counts = parse_flow_logs(flow_file, lookup_table)

    write_output(tag_counts, port_prtl_counts, output_file)

    print(f"Output written to the file : {output_file}")

if __name__ == "__main__":
    main()
