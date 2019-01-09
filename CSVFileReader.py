import csv
import os


def choosefile():
    file = input("Please enter file name or directory\n")
    if os.path.isfile(file):
        return file
    else:
        print("File directory not found")
        choosefile()


with open(choosefile(), 'r') as file:

    csv_reader = csv.reader(file, delimiter=' ')

    packetsReceived = 0
    packetsDropped = 0
    packetsQueued = 0
    packetsDequeued = 0
    ackPackets = 0
    nackPackets = 0

    for line in csv_reader:
        if line[4] == 'ack':
            ackPackets += 1
        if line[4] == 'nack':
            nackPackets += 1
        else:
            if line[0] == 'r':
                packetsReceived += 1
            if line[0] == 'd':
                packetsDropped += 1
            if line[0] == '+':
                packetsQueued += 1
            if line[0] == '-':
                packetsDequeued += 1

    throughput = (packetsReceived / packetsQueued) * 100
    lostPackets = packetsQueued - packetsReceived

    print("Throughput: %s" % throughput)
    print("Dropped Packets: %s" % packetsDropped)
    print("Lost Packets: %s" % lostPackets)
    print("Packets Received: %s" % packetsReceived)
    print("Packets Queued: %s" % packetsQueued)

with open(input("Please enter new file name, file will end in .csv\n") + '.csv', 'w') as newFile:

    csv_writer = csv.writer(newFile)

    csv_writer.writerow(['Throughput', 'Dropped Packets', 'Lost Packets', 'Packets Received', 'Packets Queued'])
    csv_writer.writerow([throughput, packetsDropped, lostPackets, packetsReceived, packetsQueued])

