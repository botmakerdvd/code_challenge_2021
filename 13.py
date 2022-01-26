#!/usr/bin/python3
file = open("here-is-the-position", "rb")


byte = file.read(1)

while byte:
    print(byte)

    byte = file.read(1)