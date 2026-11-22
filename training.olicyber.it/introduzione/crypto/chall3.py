from base64 import b64decode

# primo dato -> stringa codificata in base64
b64_en = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="

# decodifica primo dato
data_1 = b64decode(b64_en).decode("utf-8")


# secondo dato -> numero da codificare in bytes secondo il formato big endian
n = 664813035583918006462745898431981286737635929725

# decodifica secondo dato
# trovo la lunghezza di bytes necessari per rappresentarlo
bytes_len = (n.bit_length() + 7) // 8
# converto in bytes big endian il numero
data_2 = n.to_bytes(bytes_len, byteorder="big").decode("utf-8")

# stampo la flag
print(data_1 + data_2)

