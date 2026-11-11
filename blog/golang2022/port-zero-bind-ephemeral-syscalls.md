# What Go actually does when you listen on port 0

Conf42 Blog, 2022-04-01. https://www.conf42.com/blog/golang2022/port-zero-bind-ephemeral-syscalls

In short: Kazuki Higashiguchi (Autify) at Conf42 Golang 2022 on tracing net.Listen down to bind, listen and getsockname, and why port 0 means an ephemeral port

Pass port 0 to net.Listen and Go hands you a free port, a trick every httptest server relies on. At Conf42 Golang 2022, Kazuki Higashiguchi, Software Engineer at Autify, followed that call through the Go 1.18 standard library down to the system calls, and the answer to where the port comes from turns out to live in your operating system, not in Go.

It is a short, focused code-reading talk: about ten minutes, one question, one stack of functions.

## Why read the source for a one-liner?

Because the one-liner hides infrastructure decisions. Kazuki said at Conf42 Golang 2022: "Knowing the internal specification will help you make more profound design decisions." His examples: which infrastructure can run a server like this, and which range of ports it will end up on.

The documented behaviour is simple. The net package docs say that if the port in the address is empty or 0, a port number is chosen automatically. The standard library uses this itself: httptest.NewServer calls an unexported newLocalListener, which listens on TCP port 0.

## The call chain, step by step

Kazuki walks the path one function at a time:

1. **net.Listen** delegates to **ListenConfig.Listen**. A daily-life tip from the talk: use ListenConfig directly when you want to pass a context.
2. ListenConfig.Listen calls the **DefaultResolver** to resolve the address list.
3. The resolver calls **LookupPort**, which is exported, so you can try it yourself. Give it 0 and it returns 0. Go deliberately does not choose a port; it leaves it at zero.
4. For TCP, a **sysListener** calls **listenTCP**.
5. listenTCP calls **internetSocket**, which returns a network file descriptor ready for asynchronous I/O via the network poller, using socket type SOCK_STREAM. A UDP server would get SOCK_DGRAM instead.
6. For stream sockets, the code calls **listenStream**.
7. listenStream runs three system calls in order: **bind**, **listen** and **getsockname**.

The first argument to net.Listen matters along the way too: tcp4 is IPv4 only, tcp6 is IPv6 only, and plain tcp accepts either.

## So who picks the port?

The kernel, during bind. Bind assigns the socket address, listen marks the socket passive so accept can take connections, and getsockname reads back the address the kernel actually assigned. With a zero port, Linux binds to an ephemeral (dynamic) port, basically 49152 to 65535, the range IANA defines. Windows Vista and later use the same range; Windows Server 2003 and earlier used 1025 to 5000.

## What to check before relying on it

Kazuki ends with three practical checks:

- **Confirm the bind specification** of the OS you deploy to.
- **Check your infrastructure can use an ephemeral port.** His example is AWS Fargate, where you cannot bind one this way.
- **Check the ephemeral port range**, since firewall rules may need to allow it if you use this on a remote server.

## Who should watch

Go developers who use httptest every day and never wondered how it finds a port, and anyone who wants a gentle, guided tour of the net package internals. Short enough for a coffee break.

## Related Conf42 talks

- Adelina Simion and Andy Kuszyk on [load testing with F1](https://www.conf42.com/Golang_2022_Adelina_Simion_Andy_Kuszyk_load_testing_f1) at Conf42 Golang 2022.
- Julien Breux on [testing with Testcontainers](https://www.conf42.com/Golang_2024_Julien_Breux_test_testcontainers_container) at Conf42 Golang 2024.
- Divya Darshana on [HTTP communication and APIs in Go](https://www.conf42.com/Golang_2025_Divya_Darshana_http_communication_apis) at Conf42 Golang 2025.

[Watch Kazuki Higashiguchi's talk](https://www.conf42.com/Golang_2022_Kazuki_Higashiguchi_http_server_on_random_available_port)

## From Autify

Kazuki introduces Autify as a no-code, AI-powered test automation platform: it records a user's actions on the service under test, turns them into a test scenario, and uses AI to update scenarios as the application changes. It comes in two products, Autify for Web and Autify for Mobile.

- Autify: [autify.com](https://autify.com/?utm_campaign=conf42s&utm_source=conf42&utm_medium=conf42)

[Watch the talk on YouTube](https://youtu.be/bYSo78dwgH8).

## Watch the talk

[HTTP Server on random available port in Go](https://www.conf42.com/Golang_2022_Kazuki_Higashiguchi_http_server_on_random_available_port) at Conf42 Golang 2022.
