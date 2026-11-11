# Reorder three struct fields, save eight megabytes: Go micro-optimisations

Conf42 Blog, 2023-04-19. https://www.conf42.com/golang2023/squeezing-go-functions-benchmark-first

In short: Jesus Espino (Mattermost) at Conf42 Golang 2023 on benchmark-first Go micro-optimisations, from early returns to escape analysis and goroutine counts

Swapping the order of three fields in a Go struct cut a million-element slice from 24 MB to 16 MB, and made it faster too. That is one of the half-dozen measured micro-optimisations Jesus Espino, Staff Engineer at Mattermost, walked through at Conf42 Golang 2023, each one following the same loop: write a benchmark, change one thing, run it again, believe the numbers rather than your instincts.

The talk is less a list of tricks than a demonstration of the workflow, and it opens with a warning that most of the time you should not be doing this at all.

## Should you be optimising this function?

Probably not yet. Optimising means picking the right target: speed, memory, I/O. His analogy is orange juice, where freshly squeezed wins on taste and a carton wins on convenience. And optimise at the right level: a Formula One car is useless on a dirt road. Go's runtime and compiler are fast, so the bottleneck is usually the architecture, the I/O or a SQL query. When it really is the function, fix it until it stops being the bottleneck, then move on rather than polishing it to absurdity.

Above all, measure. "We are not good at guessing," Jesus Espino said at Conf42 Golang 2023, pointing at disks, context switches and every other process sharing the CPU as reasons intuition fails.

## Benchmarks and pprof, the two instruments

The testing package does the measuring. His warm-up: MD5 runs at 111.5 ns per hash against 216 ns for SHA-256, both with zero allocations once you call ReportAllocs. Opening a file costs 120 bytes and three allocations per call. Add a memory profile to the benchmark run and go tool pprof shows 74.51 MB of the total allocated in os.newFile, down to the exact line, with an SVG graph if you prefer a big red box. The CPU profile puts 30% of the time in Syscall6, written in Go assembly in the standard library, which is a useful lesson in itself: the tool shows you where the time goes, not always something you can fix.

## Do less, allocate less

The examples, all with benchmark output on an Intel Core i7-10750H:

- **Return early.** A naive find that keeps scanning after the match takes 289.7 ns; returning on the first hit takes 172.9 ns.
- **Size the slice.** Appending a million ints to an empty slice takes about 10.5 ms and 39 allocations. Preallocating with make drops it to 0.82 ms and one allocation. A fixed-size array, when the size is known at compile time, gets 0.29 ms and zero heap allocations; the data lives on the stack.
- **Pack your structs.** A bool, a float64 and an int32 in that order get 7 and 4 bytes of padding, 24 bytes per value. Put the float64 first and the bool last and it is 16 bytes. Across a million elements that is 24 MB down to 16 MB, and 2.62 ms down to 2.04 ms, because less memory also means less CPU.

## Inlining is worth a nanosecond, until it meets escape analysis

On its own, inlining a trivial function saves about one nanosecond (1.413 ns down to 0.28 ns), which he admits nobody cares about. Escape analysis matters more: return a pointer to a local and it escapes to the heap, costing 13.38 ns and one allocation, against 1.407 ns for returning the value.

The two together are the most reusable trick in the talk. A constructor that allocates a document and fills it in returns a pointer that escapes: 128.2 ns, 56 bytes, three allocations. Split it into a trivial constructor that the compiler inlines, plus an Init method that does the work, and the document can stay on the caller's stack: 73.23 ns, 32 bytes, two allocations. His rule: keep constructors simple and move complex initialisation into a second method.

## How many goroutines?

For simulated I/O (sleeps), one goroutine per job is fastest at about 10.6 ms but makes 305 allocations; one per CPU takes 91.6 ms with 37; serial takes over a second. Trading memory for time is reasonable there.

For CPU-bound work (MD5 sums), the picture flips. A thousand goroutines take 1.30 ms and 2,001 allocations, slower even than the serial loop at 114 µs. One goroutine per CPU wins at 65.5 µs and 25 allocations.

"Everything is wrong with trying to do cpu bound workloads in unbounded number of go routines," he said. Every allocation also adds garbage collector pressure, so cutting allocations pays twice.

## Who should watch

Go developers who have found a real hot path and want a disciplined way to work on it, and anyone who has never looked at allocs per op. For more, he recommends Efficient Go by Bartlomiej Plotka, Dave Cheney's High Performance Go Workshop, Damian Gryski's go-perfbook and Ardan Labs' Ultimate Go. On Conf42, pair it with [Nishant Roy on heap optimisations](https://www.conf42.com/Golang_2023_Nishant_Roy_heap_optimizations) and [Liam Conroy Hampton on memory management](https://www.conf42.com/Golang_2023_Liam_Conroy_Hampton_memory_management) from the same event, and [Yashvardhan Kukreja on profile-guided optimisation](https://www.conf42.com/Golang_2024_Yashvardhan_Kukreja_profileguided_optimization).

[Watch Jesus Espino's talk](https://www.conf42.com/Golang_2023_Jesus_Espino_squeezing_function)

## From Mattermost

- [Mattermost](https://mattermost.com/): collaboration platform for technical teams.

[Watch the talk on YouTube](https://youtu.be/R3eqwG8wfeE).

## Watch the talk

[Squeezing a go function](https://www.conf42.com/Golang_2023_Jesus_Espino_squeezing_function) at Conf42 Golang 2023.
