

def checkMagicNumber(filename):
    with open(filename,"rb") as file:
        if file.read(2) == b'\x53\x43':
            return
        else:
            print("This is not a valid SC file")

def GetExportNames(filename):
    with open(filename, 'rb') as file:
        bytes = file.read()
        pattern = b'\x1c\x00\x00\x00\x04\x00\x00\x00\x10\x00\x00\x00'
        export_names = []
        start_index = 0
        while True:
            start_index = bytes.find(pattern, start_index)
            if start_index == -1:
                break
            read_index = start_index + len(pattern) + 20 # after pattern, skipping 20 bytes
            export_name = bytearray()
            while read_index < len(bytes):
                if bytes[read_index:read_index + 1] == b'\x00': # reads until \x00
                    break
                export_name.extend(bytes[read_index:read_index + 1])
                read_index += 1
            export_names.append(export_name.decode())
            start_index += 1
    print(export_names)

if __name__ == "__main__":
    filename = input("Enter filename: ")
    checkMagicNumber(filename)
    GetExportNames(filename)

