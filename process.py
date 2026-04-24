import sys

'''
Extracts the dictionary syllablized words from The Project Gutenberg eBook
of Webster's Unabridged Dictionary, which can be found
https://www.gutenberg.org/cache/epub/29765/pg29765.txt

The syllables.txt file was generated using this script
'''

with open("pg29765.txt", encoding="utf8") as f:
	last_line = ""
	last_words = []
	clean_words = []
    for i in range(25):
        last_words.append("")
        clean_words.append("")
	for line in f:
		line = str(line.strip().encode("utf8"))[2:-1]
		if len(line) > 0 and len(last_line) > 0 and last_line.upper() == last_line:
			#print(last_line)
			#print(line)
			upper_words = last_line.split("; ")
			words = (line + " , ").split(", ")
			count = min(len(upper_words), len(words))
			matches = True
			for i in range(0,count):
				words[i] = ((words[i] + " (").split(" ("))[0]
				words[i] = ((words[i] + ".").split("."))[0]
				clean_words[i] = words[i].lower().replace("`","").replace('"',"").replace("*","")
				matches = matches and clean_words[i].upper() == upper_words[i]
			if matches:
				for i in range(0,count):
					if words[i] not in last_words:
						print(words[i])
						last_words.append(words[i])
						last_words = last_words[1:]
				if False:
					plural = ""
					if words[count].startswith("n.; pl."):
						plural = words[count].split(".")[1][1:]
						syllables = line.replace("'","-").replace('"',"-").replace("*","-").split("-")
						pos = 0
						for i in range(0,len(syllables)-2):
							pos += len(syllables[i])
						plural = words[0][:pos + len(syllables) - 1] + plural[pos:]
					elif (words[count].startswith("n.") and not words[count].startswith("n. pl.")) or words[count].startswith("v."):
						if words[0][-1:] == "s":
							plural = words[0] + "*es"
						elif words[0][-1:] == "y":
							plural = words[0][:-1] + "ies"
						else:
							plural = words[0] + "s"
					if plural != "" and plural not in last_words:
						print(str(plural.encode("utf8"))[2:-1])
						last_words.append(plural)
						last_words = last_words[1:]
				
		last_line = line
