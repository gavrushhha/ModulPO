import sys
import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output')
parser.add_argument('-s', '--source', default='/files/')
args = parser.parse_args(sys.argv[1: ])
def parse_file(filepath, dirpath):
    file_cond = os.path.exists(filepath) and os.path.isfile(filepath)
    dir_cond = os.path.exists(dirpath) and os.path.isdir(dirpath)
    if file_cond and dir_cond:
        if dirpath[-1] != '/':
            dirpath += '/'
        with open (filepath, 'r') as fp:
            filepath = filepath[filepath.rfind('/'):] if '/' in filepath else filepath
            fn, ext = filepath.split('.')
            i = 1
            for line in fp:
                with open(f'{dirpath}{fn}_{str(i)}.{ext}', 'w') as fw:
                    fw.write(line)
                i += 1
                print('file #', i, ' was written\n')
    else:
        print('Source or output not specified!')
print(parse_file('file.txt', 'files'))
# print(args.output)
# print(args.source)