#!/usr/bin/env python3

'''
OPS445 Assignment2
Author: Vilaskumar Patel
Id: 157545211

'''

import argparse
import os, sys

def parse_command_args() -> object:
    """
    Parse and return command-line arguments using argparse.

    -h : Show help message and exit.
    -H : Print file sizes in human-readable format.
    -l : Set the maximum length of the bar graph (default is 20 characters).
    program : Optional positional argument to specify the name of a running program.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Memory Visualiser -- See Memory Usage Report with bar charts",
        epilog="Copyright 2023"
    )
    parser.add_argument(
        "-l", "--length", type=int, default=20,
        help="Specify the length of the graph. Default is 20."
    )
    parser.add_argument(
        "-H", "--human-readable", action='store_true',
        help="Prints sizes in human-readable format"
    )
    parser.add_argument(
        "program", type=str, nargs='?',
        help="If a program is specified, show memory use of all associated processes. Show only total use if not."
    )
    args = parser.parse_args()
    return args

def percent_to_graph(percent: float, length: int=20) -> str:
    """
    Convert a float between 0.0 - 1.0 into a string of hash symbols and spaces.

    Parameters:
        percent (float): Percentage of the graph to be filled.
        length (int): Length of the graph.

    Returns:
        str: Graph string representation.
    """
    ymin, ymax = 0, length
    xmin, xmax = 0.0, 1.0
    y = ymin + (percent - xmin) * (ymax - ymin) / (xmax - xmin)
    num_hashes = int(y)
    return '#' * num_hashes + ' ' * (length - num_hashes)

def get_sys_mem() -> int:
    """
    Get the total system memory from /proc/meminfo.

    Returns:
        int: Total system memory in KiB.
    """
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if 'MemTotal' in line:
                return int(line.split()[1])
    return 0

def get_avail_mem() -> int:
    """
    Get the available system memory from /proc/meminfo.

    Returns:
        int: Available system memory in KiB.
    """
    with open('/proc/meminfo', 'r') as f:
        for line in f:
            if 'MemAvailable' in line:
                return int(line.split()[1])
    return 0

def pids_of_prog(app_name: str) -> list:
    """
    Get the PIDs of a given program using the pidof command.

    Parameters:
        app_name (str): Name of the application.

    Returns:
        list: List of PIDs associated with the application.
    """
    try:
        result = os.popen(f'pidof {app_name}').read().strip()
        if result:
            return result.split()
    except Exception as e:
        print(f"Error finding PIDs for {app_name}: {e}", file=sys.stderr)
    return []

def rss_mem_of_pid(proc_id: str) -> int:
    """
    Get the Resident Set Size (RSS) memory of a process by its PID.

    Parameters:
        proc_id (str): Process ID.

    Returns:
        int: RSS memory used by the process in KiB, zero if not found.
    """
    rss_total = 0
    try:
        with open(f'/proc/{proc_id}/smaps', 'r') as f:
            for line in f:
                if line.startswith('Rss'):
                    rss_total += int(line.split()[1])
    except FileNotFoundError:
        return 0
    except Exception as e:
        print(f"Error reading RSS memory for PID {proc_id}: {e}", file=sys.stderr)
        return 0
    return rss_total

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    """
    Convert KiB to human-readable format (MiB, GiB, etc.)

    Parameters:
        kibibytes (int): Size in KiB.
        decimal_places (int): Number of decimal places for formatting.

    Returns:
        str: Human-readable format.
    """
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']
    suf_count = 0
    result = kibibytes
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()

    if not args.program:
        # No program specified, show total memory usage
        total_mem = get_sys_mem()
        avail_mem = get_avail_mem()
        used_mem = total_mem - avail_mem
        percent_used = used_mem / total_mem
        graph = percent_to_graph(percent_used, args.length)
        if args.human_readable:
            used_mem = bytes_to_human_r(used_mem)
            total_mem = bytes_to_human_r(total_mem)
        print(f"Memory         [{graph} | {percent_used:.0%}] {used_mem}/{total_mem}")
    else:
        # Program specified, show memory usage for each process
        pids = pids_of_prog(args.program)
        total_mem = get_sys_mem()
        for pid in pids:
            rss_mem = rss_mem_of_pid(pid)
            percent_used = rss_mem / total_mem
            graph = percent_to_graph(percent_used, args.length)
            if args.human_readable:
                rss_mem = bytes_to_human_r(rss_mem)
            print(f"{pid:<14} [{graph} | {percent_used:.0%}] {rss_mem:<15}/{total_mem}")

