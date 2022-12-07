# Start of a packet is indicated by the most recent four characters that are different

with open("day6.txt", "r") as input_file:
    packet = input_file.read().strip()

# Create an empty set
# For each char, if the set of the next 4 chars == 4
# print the index of char + 4
for i in range(len(packet)):
    if len(set(packet[i:i+4])) == 4:
       print(i+4)
       break

# Start of message marker is indicated by the 14 distinct chars
for i in range(len(packet)):
    if len(set(packet[i:i+14])) == 14:
       print(i+14)
       break