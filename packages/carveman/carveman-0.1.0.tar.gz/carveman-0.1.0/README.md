# Description

File carving for pictures, documents and other files based on it's header an footer signatures. Does work for non fragmented files only at the moment.

# Available Files:

- .jpg

# Installation

`pip install carveman`

# Usage

**From command line:**

`python -m carveman --path PATH`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to carving source (dd, raw) |
|--outdir | -o | String | carveman-result | Path to carving source |


# Example

`python -m carveman -p path/to/carving-source/example.dd`

The carved .jpg files will be located in `carveman-result`

```
###########################################################################################

Carveman by 5f0
File carving for pictures, documents and other files

Current working directory: path/to/carving-source
        Investigated file: /example.dd

                      MD5: f447df8d455f6da4239dfd1616df4831
                   SHA256: f50643b8986900667151e362df7a8ff4a5a96f5306474d1323948f1a9c3fd385

     Path to carved files: carveman-result

 Datetime: 01/01/1970 19:20:21

###########################################################################################

--> Carving started

------> JPEG detected!
        Found header signature at: 0x1c5200 Int: 1856000
        Found footer signature at: 0x1ca9c9 int: 1878473
        Writing carved .jpg as 0x1c5200.jpg

------> JPEG detected!
        Found header signature at: 0x1caa00 Int: 1878528
        Found footer signature at: 0x1fd74f int: 2086735
        Writing carved .jpg as 0x1caa00.jpg

------> JPEG detected!
        Found header signature at: 0x1fd800 Int: 2086912
        Found footer signature at: 0x207a1a int: 2128410
        Writing carved .jpg as 0x1fd800.jpg

------> JPEG detected!
        Found header signature at: 0x207c00 Int: 2128896
        Found footer signature at: 0x211465 int: 2167909
        Writing carved .jpg as 0x207c00.jpg

------> JPEG detected!
        Found header signature at: 0x211600 Int: 2168320
        Found footer signature at: 0x22534a int: 2249546
        Writing carved .jpg as 0x211600.jpg

--> Carving finished

###########################################################################################

Execution Time: 0.326188 sec
```


# License

MIT