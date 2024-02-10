import argparse
import subprocess

parser = argparse.ArgumentParser(description="Trim videos with ffmpeg")
parser.add_argument("f_in", type=str, help="Input filename")
parser.add_argument("f_out", type=str, help="Output filename")
parser.add_argument("start", type=str, help="Start time (HH:MM:SS)")
parser.add_argument("end", type=str, nargs="?", help="End time (HH:MM:SS)")


def trim(f_in: str, f_out: str, start_ts: str, end_ts: str = "0") -> str:
    """
    Extract a clip from a media file
    """
    start = str_to_secs(start_ts)
    end = str_to_secs(end_ts)

    #  Build output filename
    _, ext = f_in.split(".")
    f_out = f"{f_out}.{ext}"
    
    #  Build ffmpeg command
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{start}", "-i", f_in]

    if end and end > start:
        cmd += ["-t", f"{end-start}"]

    cmd += ["-c", "copy", f_out]
    
    subprocess.call(cmd)

    return f_out


def str_to_secs(s: str) -> int:
    """
    Converts time string of the form HH:MM:SS to seconds
    """
    components = s.split(":")
    if len(components) == 1:
        s = components[0]
        return int(s)
    elif len(components) == 2:
        m, s = components
        return int(m) * 60 + int(s)
    elif len(components) == 3:
        h, m, s = components
        return int(h) * 3600 + int(m) * 60 + int(s)
    else:
        raise ValueError("Time format must be HH:MM:SS")


if __name__ == "__main__":
    args = parser.parse_args()
    f_out = trim(args.f_in, args.f_out, args.start, args.end)
    print(f_out)
