# Write the play, let the compiler build the state machine

Conf42 Blog, 2021-10-28. https://www.conf42.com/blog/js2021/reach-blockchain-programs-as-a-script

In short: Jay McCarthy (Reach Platform) at Conf42 JavaScript 2021 on why smart contracts are low-level state machines and how Reach compiles them from JavaScript

Most smart contracts are a state machine that exists only in the programmer's head, with the transitions written out by hand. At Conf42 JavaScript 2021, [Jay McCarthy](https://www.conf42.com/JavaScript_2021_Jay_McCarthy_Blockchain_Development), CTO of Reach Platform, explains why that makes blockchain programming low level, dangerous and expensive, and how the Reach language lets a JavaScript developer describe the interaction once and have the compiler derive the rest.

He says up front that this is a talk about ideas, not a coding tutorial; the tutorial lives in the Reach docs. It is also, naturally, a pitch for Reach, and the parts that hold up best are the explanations of what is hard.

## What is blockchain for, if not cryptocurrency?

He sets cryptocurrency aside and treats blockchain as a programming category, in the way client-server or asynchronous programming became one. Two examples carry it. A payment processor sits between your front end, your back end and the banks; it provides a real service, and that position also lets it charge fees and, in principle, take more than it should. A back end that owns a database can censor, sell or rewrite the data its users depend on, as social networks do with your photos.

Blockchain replaces both with peers talking to a decentralized ledger, which is just a database with rules about who may change what. You do not need the cryptography underneath, the same way you can use SQL without knowing how the query optimiser works. His own view is that the trustless payments side is still risky because of cryptocurrency volatility, while the trustless database is ready now.

## Why does Solidity feel like assembly?

Because you are hand-coding the arrows of a state machine. Each contract function is one transition: it starts with a pile of require checks to confirm the program is in the right state, then acts, updates the state and emits events. The machine itself is never written down anywhere. On top of that come low-level limits most JavaScript developers never meet.

Jay McCarthy said at Conf42 JavaScript 2021: "you have to make sure that you never use more than 16 local variables, because otherwise you will overflow the stack."

His evidence that this is not a toy problem is a function from Uniswap's real source, which carries a comment about scoping variables to avoid stack too deep errors.

## How does Reach do it differently?

A Reach program is JavaScript syntax with close-to-JavaScript semantics, written from the point of view of a detached observer: Alice does this, Bob receives that, then everyone sees the result. He compares it to the rulebook of a board game. The rules say who may do what and when; turning them into a program that enforces them is the hard part, and Reach's compiler does that conversion. The technique is endpoint projection, which he developed during his PhD: the multi-party program is sliced into one component per participant, with the actor who starts each step in the active role and everyone else passive.

Cryptographic patterns become features, not implementations. Simultaneous moves, impossible on a real network, are done with the commitment pattern: one party commits secretly, the other plays publicly, then the first reveals. In Reach that is a pair of built-in operations to make and check a commitment. Concurrency follows the model JavaScript developers already know from promises.

## Why does verification matter more here than elsewhere?

A contract exposes the whole database to anyone, constrained only by the rules you wrote, and it cannot be updated after launch. Get the constraints wrong and funds are either stolen or locked forever because the program stops accepting messages. Tests are finite and even property-based testing runs for a limited time, so the field uses formal verification: turn the program into equations and prove properties about them. Reach does this automatically at compile time for a baseline of safety properties, and lets you add your own assertions, which become compile-time checks rather than runtime ones.

The last point is social. Each chain has its own low-level language and a community whose savings are tied to it. Reach compiles to multiple chains, which he presents as a way to collaborate above that tribalism and to avoid learning skills tied to a platform that may not last.

## Who should watch?

JavaScript developers curious about smart contracts who want the mental model before the syntax. If you already write Solidity, the state machine and verification sections are the ones to watch. There is no live coding.

## Related Conf42 talks

- Albert Groothedde on [writing JavaScript clients for smart contracts](https://www.conf42.com/JavaScript_2023_Albert_Groothedde_javascript_client_smart_contracts) at Conf42 JavaScript 2023.
- Kevin Jones on [building on Ethereum with Scaffold-ETH](https://www.conf42.com/Web_30_2022_Kevin_Jones_build_ethereum_easily_scaffoldeth) at Conf42 Web 3.0 2022.
- Luis Cardoza Bird on [building blockchains](https://www.conf42.com/Golang_2021_Luis_Cardoza_Bird_building_blockchains) at Conf42 Golang 2021.

[Watch Jay McCarthy's talk](https://www.conf42.com/JavaScript_2021_Jay_McCarthy_Blockchain_Development), part of [Conf42 JavaScript 2021](https://www.conf42.com/js2021).

## From Reach Platform

Reach Platform makes Reach, a blockchain-agnostic language with JavaScript syntax for decentralized applications, with built-in formal verification and a JavaScript interface for front ends. The docs include a step-by-step tutorial.

- [Reach website](https://reach.sh/)

[Watch the talk on YouTube](https://youtu.be/xawcd75C3M4).

## Watch the talk

[Breaking Into Blockchain Development with JavaScript](https://www.conf42.com/JavaScript_2021_Jay_McCarthy_Blockchain_Development) at Conf42 JavaScript 2021.
