import re
import argparse
import subprocess

parser = argparse.ArgumentParser(description="Trim videos with ffmpeg")
parser.add_argument("f_in", type=str, help="Input filename")
parser.add_argument("cuts", type=str, nargs="+", help="Cut info")

cut_parser = argparse.ArgumentParser()
cut_parser.add_argument("f_out", type=str, help="Output filename")
cut_parser.add_argument("start", type=str, help="Start time (HH:MM:SS)")
cut_parser.add_argument("end", type=str, nargs="?", help="End time (HH:MM:SS)")

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
    cmd = ["ffmpeg", "-hide_banner", "-log_level", "error", "-ss", f"{start}", "-i", f_in]
    if end and end > start: cmd += ["-t", f"{end-start}"]
    cmd += ["-c", "copy", f_out]
    
    subprocess.call(cmd)

    return f_out


def str_to_secs(time: str) -> int:  
    """
    Converts time string of the form HH:MM:SS to seconds
    """
    pattern_text = r"^(((?P<h>\d+):)?(?P<m>\d+):)?(?P<s>\d+)$"
    pattern = re.compile(pattern_text)
    match = pattern.match(time)
    if match:
        h = 0 if match.group("h") is None else int(match.group("h"))
        m = 0 if match.group("m") is None else int(match.group("m"))
        s = 0 if match.group("s") is None else int(match.group("s"))
        return h * 3600 + m * 60 + s
    return 0

def str_to_secs_2(s: str) -> int:
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

    # Parse command line arguments into f_in and cuts
    args = parser.parse_args()

    # Divide cut into groups of three
    for i in range(len(args.cuts) // 3):
        cut_args = cut_parser.parse_args(args.cuts[i * 3:i * 3 + 3])

        # Call trim function
        f_out = trim(args.f_in, cut_args.f_out, cut_args.start, cut_args.end)
        print(f_out)
