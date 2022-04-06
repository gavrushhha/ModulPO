import sys
import argparse
# print(sys.argv)

# class SourseNotFound(Exception): 
#     pass
# def check_source():
#     args = sys.argv[1: ]
#     if '--source' in args:
#         source_index = args.index('--source') + 1
#         if source_index < len(args):
#             return args[source_index]
#     else:
#         raise
# print(check_source())


parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output')
parser.add_argument('-s', '--source', default='/home/')
args = parser.parse_args(sys.argv[1: ])
print(args.output)
print(args.source)
