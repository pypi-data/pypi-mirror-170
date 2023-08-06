
# btreecore - B-Tree (core persistence)

`btreecore` provides core methods for persisting a 
[`B-Tree/B+Tree/B*Tree`](https://en.wikipedia.org/wiki/B-tree) 
Node, and a list of such Nodes, in a `heapfile` / `dllfile`.

for expert reading: 
[B-tree_and_UB-tree](http://www.scholarpedia.org/article/B-tree_and_UB-tree)

this module contains not the logic for searching, inserting, or deleting data in a tree.
it also provides only a minimal set of integrity checks.


# memory / file layout

a list of B-Tree element nodes resides inside a dllfile, and heap node as data part. 
see also 
[`dllfile`](./dllfile.md), and
[`heapfile`](./heapfile.md) 
for layout.


## general node layout

### BTree node 

| name | size (bytes) | description |
| --- | --- | --- | 
| flags| 1 | boolean bit flags to indicate which fields to persist (see below) |
| len_high | 1 | key and data len high nibbles combined, this exists only if key, or data is set |
| key_len_low | 1 | key len low byte (2 nibbles), this exists only if key is set |
| data_len_low | 1 | data len low byte (2 nibbles), this exists only if data is set |
| key | k bytes | key value, this exists only if key flag is set |
| data | d bytes | data value, this exists only if data flag is set |
| left | xpos bytes | left node pointer, this exists only if flag is set |
| right | xpos bytes | right node pointer, this exists only if flag is set |

a list of nodes is stored as continuously stream of bytes inside a heap node.


### BTree node flags

| name | value | description |
| --- | --- | --- | 
| F_LEAF | 1 << 0 | node is leaf |
| F_KEY | 1 << 1 | node key to persist |
| F_DATA | 1 << 2 | node data to persist |
| F_LEFT | 1 << 3 | node left xpos to persist |
| F_RIGHT | 1 << 4 | node right xpos persist |


### BTree node list  

| name | size / value | description |
| --- | --- | --- | 
| parent | xpos bytes | parent node pointer |
| stream| n bytes | stream of btcore nodes |

a node list resides inside a `dllfile` (Double Linked List) as data part.
refer also for layout [`dllfile`](./dllfile.md)


## remark on hexdump tool

hexdump tool raise error when configured not properly. use valid hex address for node and link.
the internal hexdump tool for dumping single b-tree nodes from the btcorefile can be called with:

    usage: python3 -m dryades.btreecore.hexdump [options]

    dump heapfile b-tree elements

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show version info and exit
      -V, --verbose         show more info
      -f FILE_NAME, --file FILE_NAME
                            input file
      -n NODE_NO, --node NODE_NO
                            hex address of node. blanks in a quoted string are ignored. address of 0x0 will read the 2nd heap node since a dll element node can not be
                            stored in first heap node. (default: 000000)
      -l LINK_NO, --link LINK_NO
                            hex address of dll element node. blanks in a quoted string are ignored. (default: 000000)
      -aw ADDESS_WIDTH, --addess_width ADDESS_WIDTH
                            hex address width. (default: 6)
      -ls LINK_SIZE, --link_size LINK_SIZE
                            link size. (default: 8)
      -r REL_NO, --relative REL_NO
                            relative position of dll element node. can be combined with -n or -l option. when negative it reads backwards starting from the -n/-l node.
                            keep in mind that -n is an address and -r is a position. (default: 0)
      -nav NAVIGATE, --navigate NAVIGATE
                            combined navigate string such as: {hexnumber[p|l|r]}+, where p: parent, l: left, r: right -: prev leaf node in double linked list +: succ leaf
                            node in double linked list e.g. "-nav 0l1lpp" will navigate node[0].left -> node[1].left -> node.parent -> node.parent (will be again the
                            starting node)
      -w WIDTH, --width WIDTH
                            with of data output (default: 16)
      -g GROUP, --group GROUP
                            group bytes in data output (default: 1)
      -ho, --header_only    prints only header, no data.



## limitations

- see other limits also here [`dllfile`](./dllfile.md)
- see other limits also here [`heapfile`](./heapfile.md)
- key and data field len is limited to 12 bits (3 nibbles) 2**12 == 4096 bytes max len
  - remark: the data field could be used to point to a location inside the `heapfile` e.g. a (file position/memory) reference to a more complex object 
- 


