# questa e' una stringa codificata in esadecimale
s = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"

# per ottenere la sua decodifica posso applicare un metodo della classe
# bytes ovvero "

print(bytes.fromhex(s).decode("utf-8"))


''' NOTE:

	. La classe bytes si dichiara con b"<bytes>"

	CODIFICA
	. La classe bytes ha come metodo <string>.hex che converte i bytes in esadecimale
		(va chiamato su una stringa)

	DECODIFICA
	. La classe bytes ha come metodo .fromhex(<stringa>) che converte i byte in esadecimale
		(va chiamato su un oggetto bytes)

'''
