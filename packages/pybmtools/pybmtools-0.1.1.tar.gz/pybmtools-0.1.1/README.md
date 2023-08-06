
[![bioconda-badge](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg)](http://bioconda.github.io)

# pyBMtools
A python extension, written in C, for quick access to BM files and access to and creation of BM files. This extension uses [bmtools](https://github.com/ZhouQiangwei/bmtools) for local and remote file access.

Table of Contents
=================

  * [Installation](#installation)
    * [Requirements](#requirements)
  * [Usage](#usage)
    * [Load the extension](#load-the-extension)
    * [Open a BM file](#open-a-BM-file)
    * [Determining the file type](#determining-the-file-type)
    * [Access the list of chromosomes and their lengths](#access-the-list-of-chromosomes-and-their-lengths)
    * [Print the header](#print-the-header)
    * [Compute summary information on a range](#compute-summary-information-on-a-range)
      * [A note on statistics and zoom levels](#a-note-on-statistics-and-zoom-levels)
    * [Retrieve values for individual bases in a range](#retrieve-values-for-individual-bases-in-a-range)
    * [Retrieve all intervals in a range](#retrieve-all-intervals-in-a-range)
    * [Add a header to a BM file](#add-a-header-to-a-BM-file)
    * [Adding entries to a BM file](#adding-entries-to-a-BM-file)
    * [Close a BM file](#close-a-BM-file)
  * [A note on coordinates](#a-note-on-coordinates)

# Installation
You can install this extension directly from github with:

    pip install pybmtools

or with conda

    conda install pybmtools -c bioconda

## Requirements

The follow non-python requirements must be installed:

 - libcurl (and the `curl-config` config)
 - zlib

The headers and libraries for these are required.

# Usage
Basic usage is as follows:

## Load the extension

    >>> import pybmtools as pybm

## Open a BM file

This will work if your working directory is the pybmtools source code directory.

    >>> bm = pybm.openfile("test/test.bm")

Note that if the file doesn't exist you'll see an error message and `None` will be returned. Be default, all files are opened for reading and not writing. You can alter this by passing a mode containing `w`:

    >>> bm = pybm.openfile("test/output.bm", "w")

Note that a file opened for writing can't be queried for its intervals or statistics, it can *only* be written to. If you open a file for writing then you will next need to add a header (see the section on this below).


## Access the list of chromosomes and their lengths

`binaMethFile` objects contain a dictionary holding the chromosome lengths, which can be accessed with the `chroms()` accessor.

    >>> bm.chroms()
    dict_proxy({'chr1': 195471971L, 'chr10': 130694993L})

You can also directly query a particular chromosome.

    >>> bm.chroms("chr1")
    195471971L

The lengths are stored a the "long" integer type, which is why there's an `L` suffix. If you specify a non-existant chromosome then nothing is output.

    >>> bm.chroms("chr1")
    >>> 

## Print the header

It's sometimes useful to print a BM's header. This is presented here as a python dictionary containing: the version (typically `4`), the number of zoom levels (`nLevels`), the number of bases described (`nBasesCovered`), the minimum value (`minVal`), the maximum value (`maxVal`), the sum of all values (`sumData`), and the sum of all squared values (`sumSquared`). The last two of these are needed for determining the mean and standard deviation.

    >>> bm.header()
    {'version': 61951, 'nLevels': 1, 'nBasesCovered': 2669, 'minVal': 0, 'maxVal': 1, 'sumData': 128.40874156728387, 'sumSquared': 97.26764956510321}


## Compute summary information on a range

BM files are used to store values associated with positions and ranges of them. Typically we want to quickly access the average value over a range, which is very simple:

    >>> bm.stats("chr1", 0, 10000)
    [0.2000000054637591]

Suppose instead of the mean value, we instead wanted the maximum value:

    >>> bm.stats("chr1", 0, 1000, type="max")
    [0.30000001192092896]

Other options are "weighted" (the weighted average DNA methylation value)

It's often the case that we would instead like to compute values of some number of evenly spaced bins in a given interval, which is also simple:

    >>> bm.stats("1",99, 200, nBins=2)
    [1.399999976158142, 1.5]

`nBins` defaults to 1, just as `type` defaults to `mean`.

If the start and end positions are omitted then the entire chromosome is used:

    >>> bm.stats("chr1")
    [1.3351851569281683]

## Retrieve values for individual bases in a range

While the `stats()` method **can** be used to retrieve the original values for each base (e.g., by setting `nBins` to the number of bases), it's preferable to instead use the `getvalues()` accessor.

    >>> bm.getvalues("chr1", 0, 3)
    [0.10000000149011612, 0.20000000298023224, 0.30000001192092896]

The list produced will always contain one value for every base in the range specified. If a particular base has no associated value in the BM file then the returned value will be `nan`.

    >>> bm.getvalues("chr1", 0, 4)
    [0.10000000149011612, 0.20000000298023224, 0.30000001192092896, nan]

## Retrieve all intervals in a range

Sometimes it's convenient to retrieve all entries overlapping some range. This can be done with the `intervals()` function:

    >>> bm.intervals("chr1", 0, 3)
    ((0, 1, 0.10000000149011612), (1, 2, 0.20000000298023224), (2, 3, 0.30000001192092896))

What's returned is a list of tuples containing: the start position, end end position, and the value. Thus, the example above has values of `0.1`, `0.2`, and `0.3` at positions `0`, `1`, and `2`, respectively.

If the start and end position are omitted then all intervals on the chromosome specified are returned:

    >>> bm.intervals("chr1")
    ((0, 1, 0.10000000149011612), (1, 2, 0.20000000298023224), (2, 3, 0.30000001192092896), (100, 150, 1.399999976158142), (150, 151, 1.5))

## Add a header to a BM file

If you've opened a file for writing then you'll need to give it a header before you can add any entries. The header contains all of the chromosomes, **in order**, and their sizes. If your genome has two chromosomes, chr1 and chr2, of lengths 1 and 1.5 million bases, then the following would add an appropriate header:

    >>> bm.addHeader([("chr1", 1000000), ("chr2", 1500000)])

BM headers are case-sensitive, so `chr1` and `Chr1` are different. Likewise, `1` and `chr1` are not the same, so you can't mix Ensembl and UCSC chromosome names. After adding a header, you can then add entries.

By default, up to 10 "zoom levels" are constructed for BM files. You can change this default number with the `maxZooms` optional argument. A common use of this is to create a BM file that simply holds intervals and no zoom levels:

    >>> bm.addHeader([("chr1", 1000000), ("chr2", 1500000)], maxZooms=0)

If you set `maxTooms=0`, please note that IGV and many other tools WILL NOT WORK as they assume that at least one zoom level will be present. You are advised to use the default unless you do not expect the BM files to be used by other packages.

## Adding entries to a BM file

Assuming you've opened a file for writing and added a header, you can then add entries. Note that the entries **must** be added in order, as BM files always contain ordered intervals. There are three formats that BM files can use internally to store entries.

    chr1	0	100	0.0
    chr1	100	120	1.0
    chr1	125	126	200.0

These entries would be added as follows:

    >>> bm.addEntries(["chr1", "chr1", "chr1"], [0, 100, 125], ends=[5, 120, 126], values=[0.0, 1.0, 200.0])

Each entry occupies 12 bytes before compression.

Note that pybmtools will try to prevent you from adding entries in an incorrect order. This, however, requires additional over-head. Should that not be acceptable, you can simply specify `validate=False` when adding entries:

    >>> bm.addEntries(["chr1", "chr1", "chr1"], [100, 0, 125], ends=[120, 5, 126], values=[0.0, 1.0, 200.0], validate=False)

You're obviously then responsible for ensuring that you **do not** add entries out of order. The resulting files would otherwise largley not be usable.

## Close a BM file

A file can be closed with a simple `bm.close()`, as is commonly done with other file types. For files opened for writing, closing a file writes any buffered entries to disk, constructs and writes the file index, and constructs zoom levels. Consequently, this can take a bit of time.

# Numpy

As of version 0.3.0, pyBigWig supports input of coordinates using numpy integers and vectors in some functions **if numpy was installed prior to installing pyBigWig**. To determine if pyBigWig was installed with numpy support by checking the `numpy` accessor:

    >>> import pybmtools as pybm
    >>> pybm.numpy
    1

If `pybm.numpy` is `1`, then pybmtools was compiled with numpy support. This means that `addEntries()` can accept numpy coordinates:

    >>> import pybmtools as pybm
    >>> import numpy
    >>> bm = pybm.openfile("test/outnp.bm", "w")
    >>> bm.addHeader([("chr1", 1000)], maxZooms=0)
    >>> chroms = np.array(["chr1"] * 10)
    >>> starts = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], dtype=np.int64)
    >>> ends = np.array([5, 15, 25, 35, 45, 55, 65, 75, 85, 95], dtype=np.int64)
    >>> values0 = np.array(np.random.random_sample(10), dtype=np.float64)
    >>> bm.addEntries(chroms, starts, ends=ends, values=values0)
    >>> bm.close()

Additionally, `getvalues()` can directly output a numpy vector:

    >>> bm = bm.openfile("test/outnp.bm")
    >>> bm.values('1', 0, 10, numpy=True)
    [ 0.74336642  0.74336642  0.74336642  0.74336642  0.74336642         nan
         nan         nan         nan         nan]
    >>> type(bm.values('1', 0, 10, numpy=True))
    <type 'numpy.ndarray'>


# A note on coordinates and library using
BM files use 1-based coordinates. And pybmtools and bmtools are based on [libbigwig](https://github.com/dpryan79/libBigWig) and [pyBigWig](https://github.com/deeptools/pyBigWig)
