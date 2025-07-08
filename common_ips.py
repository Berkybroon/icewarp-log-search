from collections import Counter

# declare arrays
requests = []
ip_addresses = []

# import log file and fill requests array with all lines that start with a number (IP addresses)
with open('log') as file:
    for line in file:
        if line[0].isdigit():
            requests.append(line)

# method to extract the IP address from each line and save to array
def get_ip(str):
    ip_end = str.index(' ')
    ip_address = str[0:ip_end]
    ip_addresses.append(ip_address)

# run the above method on each object in the requests array
for request in requests:
    get_ip(request)

# count the occurences of each IP and save the top 50 to an output file
ip_counter = Counter(ip_addresses)
top_50_most_common = ip_counter.most_common(50)

for ip, count in top_50_most_common:
    print(f"{ip}: {count} occurrences")
