count = 0
is_newtimeline = True
out = open('out.srt', 'w', encoding='utf-8')
with open('captions(1).sbv', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            is_newtimeline = True
            print(line)
            out.write(line + '\n')
        elif is_newtimeline:
                is_newtimeline = False
                count += 1
                print(count)
                out.write(str(count) + '\n')
                start, end = line.split(',')
                start = start.replace('.', ',')
                end = end.replace('.', ',')
                print("%s --> %s" % (start, end))
                out.write("%s --> %s\n" % (start, end))
        else:
            print(line)
            out.write(line + '\n')
out.close()
