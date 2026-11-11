# Stop waiting for the build. Evaluate the module instead

Conf42 Blog, 2022-11-17. https://www.conf42.com/blog/js2022/repl-driven-development-kills-the-build-wait

In short: James Diacono (Equimaps) at Conf42 JavaScript 2022 on fast feedback loops, batch processing history and REPL-driven development in JavaScript

The save, rebuild, reload, poke-around loop gets slower as every project grows, and James Diacono thinks JavaScript developers have quietly accepted that. At Conf42 JavaScript 2022, the Equimaps software engineer made the case for REPL-driven development: evaluate code straight from your editor into a running browser or Node.js process, and let the build and reload steps disappear from the loop.

James works in a family business that makes apps for horse riders: his sister designs, his dad is the sysadmin, his mum is the boss and he writes the code. The talk is half computing history, half live demo, and both halves earn their place.

## Why does slow feedback hurt?

He splits the typical web developer loop into doing steps (change code, test, debug) and waiting steps (rebuild, reload). On a new project the waiting is invisible. As the build chain grows, sub-second delays become longer, and in the worst case you spend more time waiting than doing.

His three reasons it matters are good ones. Programmers are creative people who respond badly to tedium, and a slow step knocks you out of the zone. Slow feedback tempts you to make many changes at once, which hides where the mistake is and means more debugging, of the most thankless kind: nobody thanks you for fixing a bug you created 15 minutes ago. And it's hard to end the day feeling accomplished after spending much of it waiting.

## A short history of waiting

Before the microcomputer, machines were huge, slow and astronomically expensive, so owners kept them busy with batch processing: stitch programs into a batch, run them back to back, and let an operator load the next one. Owners loved it. Programmers, queuing their test runs behind the payroll job, did not; a 48-hour turnaround wasn't unusual.

Then someone connected a teleprinter, an electric typewriter on a phone line, to a computer in 1955, and the command line interface arrived. In 1959 John McCarthy described a programmer at a keyboard who can try a program, interrogate data or code, make a change and try again. That was interactive programming, too expensive for one person to occupy a mainframe. His fix was timesharing, first built by his team in 1962, which James traces through to the internet and AWS Lambda.

McCarthy also created Lisp, which introduced conditionals, recursion, first-class functions and garbage collection to high-level languages, plus the REPL: read, eval, print, loop. JavaScript has all five, so, as James puts it, anything that's true for Lisp is essentially true for JavaScript.

## The REPL you already have

Every modern browser ships one: the console in the developer tools. James uses it to evaluate expressions, touch the DOM, schedule a setTimeout and show why every call returns a value even when it's just undefined. He also uses it to ask the language questions, like what getYear returns. It's the number of years since 1900, a quirk copied from Java, which gave a date method designed in 1995 about five years of sensible answers.

The limit is that the console only knows the language and what you typed into it. Real applications are modules in files edited in a text editor, and you can't paste import or export statements into the prompt. Lisp programmers solved this decades ago when they got screens.

## Writing a component in the REPL

The demo is the payoff. In VS Code, a keyboard shortcut sends the selected code to a REPL running in the browser and shows the result inline. It handles modules, so James imports Vue, checks its version (3.2.30) and builds a component from nothing.

He writes a plain-English specification first, then a demo instead of an automated UI test, because simulating a human is hard. The demo fails with a ReferenceError since the component doesn't exist yet, which is the point: you test the test. Then he writes the props and setup function, a render function using h to make a button, adds a click handler, reruns, and exports. The demo stays in the file, commented out, for next time.

He calls the result a whole module: specification, demo and implementation in one file. It travels between projects intact, and when you land on a buggy line in an unfamiliar code base, the spec and demo are right there. The new loop has no build or reload, the test runs only this module, and debugging excludes bugs elsewhere in the app.

## Replete

The REPL is Replete, which James wrote to find out whether REPL-driven development worked in JavaScript. It's open source on GitHub, with editor plugins for Sublime Text, VS Code, Neovim and Emacs; the VS Code one is about 60 lines, because all it does is send code to Replete on a shortcut. It evaluates in any modern browser, including on a phone, in Node.js and in Deno. He uses it for front end, back end, experiments and production code.

"So programmer time is now the most precious resource in any software project, so we just can't afford to waste it," James Diacono said at Conf42 JavaScript 2022.

## Who should watch

Front-end developers whose hot reload has stopped feeling hot, anyone curious why Lisp people talk about the REPL with such affection, and teams wondering whether every component needs a full app around it to be tested. The history section is worth it on its own.

Related Conf42 talks: [Austin Gil on TypeScript checking with JSDoc](https://www.conf42.com/JavaScript_2022_Austin_Gil_jsdocs_typescript), which also skips a build step, [Robert Aboukhalil on interactive command-line tutorials with WebAssembly](https://www.conf42.com/JavaScript_2022_Robert_Aboukhalil_interactive_commandline_tutorials_webassembly), and [Domenico Musto on developer productivity after serverless](https://www.conf42.com/JavaScript_2022_Domenico_Musto_development_productivity_post_serverless_world).

[Watch James Diacono's talk](https://www.conf42.com/JavaScript_2022_James_Diacono_feedback_repl) from [Conf42 JavaScript 2022](https://www.conf42.com/js2022).

## From Equimaps

James introduces Equimaps as his family's company, which makes apps for horse riders.

- Equimaps: [crosscountryapp.com](https://www.crosscountryapp.com/)

[Watch the talk on YouTube](https://youtu.be/7WztZrcCjqI).

## Watch the talk

[Feedback and the REPL](https://www.conf42.com/JavaScript_2022_James_Diacono_feedback_repl) at Conf42 JavaScript 2022.
