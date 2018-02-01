contents = open("logs.txt")
count = {}
new_contents = []
results = []

for line in contents:
    line = line.split()
    new_contents.append(line[0])

for ip_address in new_contents:
    count[ip_address] = count.get(ip_address, 0) + 1

while len(results) < 3:
    highest = max(count, key=count.get)
    results.append((highest, count.get(highest)))
    count[highest] = 0

for result in results:
    print str(result[0]) + " accessed " + str(result[1]) + " times."