import string

PRINTCHARS = (
    str(string.printable)
    .replace("\n", "")
    .replace("\r", "")
    .replace("\t", "")
    .replace("\x0b", "")
    .replace("\x0c", "")
)
PRINTCHARS_enc = PRINTCHARS.encode()


def hexdumps(mem, width=16, group=1, output=True, start_adr=None, addess_width=6):

    adr = start_adr if start_adr != None else 0

    totstr = ""

    if mem == None:
        mem = []
        if output:
            print("--- no data ---")

    while len(mem) > 0:

        line, mem = mem[:width], mem[width:]

        out = f"{adr:0{addess_width}x}" + " : "
        adr += width

        out += line.hex(" ", group)
        out += " "

        if len(line) < width:
            miss = width - len(line)
            miss_grp = int(miss / group)
            to_insert = (2 * group + 1) * miss_grp
            out += " " * to_insert

        out += ": "

        for by in line:
            out += chr(by) if by in PRINTCHARS_enc else "."

        if output:
            print(out)
        else:
            totstr += out + "\n"

    if not output:
        return totstr


def main():
    import os
    import argparse

    from dryades.heapfile.heap import HeapFile
    from dryades.const import VERSION

    parser = argparse.ArgumentParser(
        prog="hexdump",
        usage="python3 -m dryades.heapfile.%(prog)s [options]",
        description="dump heapfile nodes",
    )
    parser.add_argument(
        "-v",
        "--version",
        dest="show_version",
        action="store_true",
        help="show version info and exit",
        default=False,
    )
    parser.add_argument(
        "-V",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="show more info",
        default=False,
    )

    parser.add_argument(
        "-f",
        "--file",
        dest="file_name",
        action="store",
        help="input file",
        required=True,
    )
    parser.add_argument(
        "-n",
        "--node",
        type=str,
        dest="node_no",
        action="store",
        help="hex address of node. blanks in a quoted string are ignored. (default: %(default)s)",
        default=f"{0:06x}",
    )
    parser.add_argument(
        "-aw",
        "--addess_width",
        type=int,
        dest="addess_width",
        action="store",
        help="hex address width. (default: %(default)s)",
        default=6,
    )
    parser.add_argument(
        "-r",
        "--relative",
        type=int,
        dest="rel_no",
        action="store",
        help="""relative position of node.
            can be combined with -n option when positive.
            when negative it reads from the end of the heap.
            keep in mind that -n is an address and -r is a position.
            (default: %(default)s)""",
        default="0",
    )
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        dest="width",
        action="store",
        help="with of data output (default: %(default)s)",
        default=16,
    )
    parser.add_argument(
        "-g",
        "--group",
        type=int,
        dest="group",
        action="store",
        help="group bytes in data output (default: %(default)s)",
        default=1,
    )
    parser.add_argument(
        "-ho",
        "--header_only",
        dest="header_only",
        action="store_false",
        help="prints only header, no data.",
        default=True,
    )

    args = parser.parse_args()

    if args.show_version:
        print("Version:", VERSION)
        return

    fnam = os.path.expanduser(args.file_name)
    node_nr = int(args.node_no.replace(" ", ""), 16)
    rel_no = args.rel_no
    header_only = args.header_only
    width = args.width
    addess_width = args.addess_width
    group = args.group
    verbose = args.verbose

    hpf = HeapFile(fnam).open()

    node = hpf.read_node(node_nr)

    if rel_no >= 0:
        while rel_no > 0:
            rel_no -= 1
            node = hpf.read_next(node)
    else:
        node = hpf.read_node(0)
        nodes = []
        offs = 0
        while node != None:
            nodes.append(node)
            if node.id == node_nr:
                offs = len(nodes) - 1
            node = hpf.read_next(node)
        node = nodes[offs + rel_no]
        if verbose:
            print("total number of nodes in heap", len(nodes))

    print("node", hex(node.id))
    print("aloc", "/", "used", ":", hex(node.aloc), "/", hex(node.used), end=" ")
    print(":", node.aloc, "/", node.used)

    if header_only:
        data = hpf.read_node_content(node)
        hexdumps(
            data, start_adr=node.id, width=width, group=group, addess_width=addess_width
        )

    hpf.close()


if __name__ == "__main__":
    main()
