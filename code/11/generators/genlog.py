# genlog.py
#
# Sum up the megabytes transferred in an Apache server log using
# generator expressions

wwwlog = open("access-log")
bytecolumn = (line.rsplit(None, 1)[1] for line in wwwlog)

print(list(bytecolumn))
bytes = (int(x) for x in bytecolumn if x != '-')
total = int(sum(bytes) / 1024 / 1024)

print(f"Total {total} Mb")
