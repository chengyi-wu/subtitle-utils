import sys

def convert(src, dst='out.srt'):
    count = 0
    is_newtimeline = True
    out = open(dst, 'w', encoding='utf-8')
    with open(src, 'r', encoding='utf-8') as f:
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

if __name__ == '__main__':
    src = sys.argv[1]
    convert(src)