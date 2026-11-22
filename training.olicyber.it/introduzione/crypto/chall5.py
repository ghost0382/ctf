def xor(a, b):
	return bytes([x^y for x, y in zip(a, b)])

plain = None
cypher = bytes.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c")

for i in range(256):
	key = bytes([i]) * len(cypher)
	plain = xor(key, cypher)

	if all(32 <= b <= 126 for b in plain):
		print("flag{" + plain.decode("utf-8") + "}")
		break
