#!/usr/local/bin/python3
import os
import subprocess
import argparse
import re

parser = argparse.ArgumentParser(description='Trim videos with ffmpeg')
parser.add_argument('f_in', type=str, help='Input filename')
parser.add_argument('cuts', type=str, nargs='+', help='Cut info')

cut_parser = argparse.ArgumentParser()
cut_parser.add_argument('f_out', type=str, help='Output filename')
cut_parser.add_argument('start', type=str, help='Start time (HH:MM:SS)')
cut_parser.add_argument('end', type=str, nargs='?', help='End time (HH:MM:SS)')

def str_to_secs(time_str): # converts time sring of the form HH:MM:SS to seconds
    pattern_text = r'^(((?P<h>\d+):)?(?P<m>\d+):)?(?P<s>\d+)$'
    pattern = re.compile(pattern_text)
    match = pattern.match(time_str)
    h = 0 if match.group('h') is None else int(match.group('h'))
    m = 0 if match.group('m') is None else int(match.group('m'))
    s = 0 if match.group('s') is None else int(match.group('s'))
    print(h,m,s)
    return h*3600 + m*60 + s

def trim(f_in, args):
    start_s = str_to_secs(args.start)
    end_s = 0

    end_s = str_to_secs(args.end) if args.end != None else 0 

    prefix, ext = f_in.split('.') #mb-###.ts
    f_out = f'{prefix}-{args.f_out}.{ext}'
    print(f_out)
    if end_s == 0:
        cmd = ['ffmpeg', '-ss', f'{start_s}', '-i', f_in, '-c', 'copy', f_out]
        print(cmd)
        subprocess.call(cmd)
    else:
        duration = end_s - start_s
        cmd = ['ffmpeg', '-ss', f'{start_s}', '-i', f_in, '-t', f'{duration}', '-c', 'copy', f_out]
        print(cmd)
        subprocess.call(cmd)

if __name__ == "__main__":
    args = parser.parse_args()
    for i in range(len(args.cuts)//3):
        cut_args = cut_parser.parse_args(args.cuts[i*3:i*3+3])
        trim(args.f_in, cut_args)