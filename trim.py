#!/usr/local/bin/python3
import os
import subprocess
import argparse

def str_to_secs(time_str):#converts time sring of the form HH:MM:SS to seconds
    time_split = time_str.split(':')
    h,m,s = 0,0,0

    if len(time_split) == 3:
        h=int(time_split[0])
        m=int(time_split[1])
        s=int(time_split[2])
    if len(time_split) == 2:
        m=int(time_split[0])
        s=int(time_split[1])
    if len(time_split) == 1:
        s=int(time_split[0])

    tot_secs = h*3600 + m*60 + s
    return tot_secs

parser = argparse.ArgumentParser(description='Trim videos with ffmpeg')
parser.add_argument('f_in', type=str, help='Input filename')
parser.add_argument('cuts', type=str, nargs='+', help='Cut info')

cut_parser = argparse.ArgumentParser()
cut_parser.add_argument('f_out', type=str, help='Output filename')
cut_parser.add_argument('start', type=str, help='Start time (HH:MM:SS)')
cut_parser.add_argument('end', type=str, nargs='?', help='End time (HH:MM:SS)')

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
