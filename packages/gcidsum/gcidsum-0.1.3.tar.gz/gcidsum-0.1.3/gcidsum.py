# -*- coding: utf-8 -*-
#
# Copyright (c) 2022~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
import sys
import re
import pathlib
import os
import xlgcid

def _enumerate_paths(pattern: str):
    try:
        if os.path.isabs(pattern):
            if os.name == 'nt':
                drive, path = os.path.splitdrive(pattern)
                # C: resolve to ~, C:\ resolve to C:, see https://stackoverflow.com/questions/48810950/
                drive += '\\'
                path = path.removeprefix('\\').removeprefix('/')
                items = list(pathlib.Path(drive).glob(path))
            else:
                path = pattern.removeprefix('/')
                items = list(pathlib.Path('/').glob(path))
        else:
            try:
                items = list(pathlib.Path('.').glob(pattern))
            except re.error:
                items = [pattern] if os.path.exists(pattern) else None
    except ValueError as ve:
        __error(ve)
    else:
        if items is None:
            __error(f"can't open '{pattern}': Invalid argument")
        else:
            yield from items

__output_pattern = re.compile('^(?P<gcid>[0-9a-f]{40})  (?P<name>.+)$', re.I)
def __parse_output(line: str):
    if match := __output_pattern.match(line):
        return match.group('gcid'), match.group('name')
    else:
        return None, None

def __get_gcid(path):
    try:
        return xlgcid.get_file_gcid_digest(path).hex().lower()
    except PermissionError:
        __error(f"can't open '{path}': Permission denied")
    except FileNotFoundError:
        __error(f"can't open '{path}': No such file or directory")

def __error(msg: str):
    print(f'gcidsum: {msg}', file=sys.stderr)

def __show_help():
    print('''Usage: gcidsum [-c[swe]|-e] [FILE]...

Print or check GCID checksums

        -c      Check sums against list in FILEs
        -s      Don't output anything, status code shows success
        -w      Warn about improperly formatted checksum lines
        -e      If exist, the first FILE should be a exists gcidsum file to exclude''')

def __parse_args(args: Tuple[str, ...]):
    s, w, e, excluded = [False] * 4

    if c := args[0].startswith('-c'):
        s = 's' in args[0]
        w = 'w' in args[0]
        e = 'e' in args[0]
        fs = args[1:]
    elif e := args[0] == '-e':
        fs = args[1:]
    else:
        fs = args

    if e:
        if fs:
            excluded, *fs = fs
        else:
            __error('Missing the gcidsum file (for -e options)')
            exit()

    return {
        'c': c, 's': s, 'w': w, 'e': e,
        'fs': fs,
        'excluded': excluded,
    }

def gcidsum_main(args: List[str]):
    if not args or args == ('--help', ):
        return __show_help()

    pargs = __parse_args(args)

    def enumerate_from_args(args):
        for arg in args:
            yield from _enumerate_paths(arg)

    os.chdir(r'C:\Users\skyoflw\Downloads\QZJVR')

    if pargs['e']:
        excluded_lines = pathlib.Path(pargs['excluded']).read_text('utf-8').splitlines()
        excluded = set(__parse_output(l)[1] for l in excluded_lines)
    else:
        excluded = ()

    def is_excluded(name: str):
        return str(name) in excluded

    if pargs['c']:
        failed = 0
        total = 0
        for path in enumerate_from_args(pargs['fs']):
            for line in path.read_text('utf-8').splitlines():
                if line:
                    gcid_in_file, name = __parse_output(line)

                    if is_excluded(name):
                        continue

                    if gcid_in_file:
                        eq = (gcid := __get_gcid(name)) and (gcid.lower() == gcid_in_file.lower())
                        total += 1
                        if not eq:
                            failed += 1
                        if not pargs['s']:
                            print(f"{name}: {'OK' if eq else 'FAILED'}")
                    elif pargs['w']:
                        __error(f'invalid format: {line}')
        if failed:
            __error(f'WARNING: {failed} of {total} computed checksums did NOT match')
    else:
        for path in enumerate_from_args(pargs['fs']):
            if is_excluded(path):
                continue

            if gcid := __get_gcid(path):
                output = f'{gcid}  {path}'
                assert __output_pattern.match(output)
                print(output)

def main(argv=None):
    try:
        if argv is None:
            argv = sys.argv
        return gcidsum_main(tuple(argv[1:]))
    except KeyboardInterrupt:
        return 1

if __name__ == '__main__':
    exit(main() or 0)
