// A stream is a uniform abstraction for communicating with files and devices that
// consume or produce sequential data such as sockets, keyboards, USB ports, and
// printers.

// C uses the opaque FILE data type to represent streams.
// Streams are frequently reffered to as "file pointers"

// C standard has no concept of directories. since it must be able to work with
// nonhierarchical file systems. you'll generally need to use less portable APIs provided
// by POSIX, Windows, and other platforms to perform I/O in real world applications

// Stream buffering is the process of temporarily storing data in main memory that's
// passing between a process and a device or file, impriving the throughput of I/O
// operations, which often have high latencies.

// When a program requests to write to block-oriented devices like disks., the driver can
// cache the data in memory until it has accumulated enough data for one or more device
// blocks, at which points it writes all data at once, which improves throughput. This
// strategy is called "flushing" the output buffer.

// Like device drivers, streams maintain their own I/O buffers, and typically uses one
// input buffer for each file the program wants to read from, and one output buffer for
// reach it wants to write to.

// A stream can be in one of three states:
// 1. Unbuffered: characters are intended to appear from the soruce or at the destination
// ASAP, e.g., error reporting or logging streams might be unbuffered.
// 2. Fully buffered: characters are intended to be transmitted to or from the host
// environment as a block when a buffer is filled. Streams used for file I/O are normally
// fully buffered.
// 3. Line buffered: characters are intended to be transmitted to or from the host
// environment as a block when a newline character is encountered. Streams connected to
// interactive devices such as terminals are line-buffered when you open them.

// Predefined text streams open and available to use on startup

// stdin: fully buffered standard input stream, conventional input source for the
// program. Associated with keyboard by default but may be redirected to input from a
// file. Not fully buffered if associated with an interactive device such as a
// terminal.

// stdout: full buffered standard output stream, conventional output destination for the
// program. This stream is assocaited with the temrinal that initiated the program but
// can be redirected to output to a file or other stream. Not fully buffered if
// associated with an interactive device.

// stderr standard error stream, for writing diagnostic output. Not fully buffered, error
// reporting can be viewed ASAP.

// you can use POSIX pipes | to redirect stdout to be another programs stdin
// e.g., `echo 'hello robot' | sed 's/hello/yo'` returns "yo robot"

// text streams and binary streams