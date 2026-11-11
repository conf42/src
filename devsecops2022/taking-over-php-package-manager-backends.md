# Two researchers, one week, and the servers behind Composer and PEAR

Conf42 Blog, 2022-11-30. https://www.conf42.com/devsecops2022/taking-over-php-package-manager-backends

In short: Thomas Chauchefoin and Paul Gerste (SonarSource) at Conf42 DevSecOps 2022 on how they took over the PHP package registries Packagist and PEAR

Most supply chain worries stop at a malicious package. At Conf42 DevSecOps 2022, Thomas Chauchefoin and Paul Gerste, vulnerability researchers at SonarSource, showed the bigger prize: the registry itself. They found ways to run code on Packagist, the registry behind Composer, twice (CVE-2021-29472 and CVE-2022-24828), and on the PEAR server, and each time an attacker could have rewritten where package names point. The takeaway: the middleman in your dependency tree is soft, and the fix is to stop having to trust it.

## Why go after the registry and not a package?

A package manager installs by name, and the backend maps that name to a location: a tarball URL, a Git repository, whatever the client supports. Change that mapping and every developer who runs an update downloads the attacker's archive, then executes it at some point. One server, every downstream build.

The PHP numbers make this less academic than it sounds. Their rough estimate: PHP runs behind about 78% of the web, WordPress (which doesn't need Composer) is 43% of that, and about 68% of PHP projects use Composer, so maybe 20% of web servers pull from Packagist one way or another. Packagist serves around 2 billion package downloads a month. Thomas Chauchefoin said at Conf42 DevSecOps 2022: "Even if everybody tried to tell you that PHP is dead, that's really not the case."

## Escaping is not enough: argument injection

Packagist imports a package from any repository URL you submit, and calls git, svn or Mercurial (hg) to check it. The URL was escaped against shell command injection, so the obvious trick fails. But escaping only stops the shell from interpreting the string; it still arrives as an argument. A URL that starts with a dash becomes an option to hg, and Mercurial's config lets you define an alias that overrides a built-in command and, with an exclamation mark, runs a shell command. Submitting that "URL" gave them a shell on the registry.

The live demo is the good part: a test package called stunning-waffle prints happy emojis, the attacker edits the JSON metadata on the server, and the next composer update quietly fetches something else. The maintainers deployed a hotfix within hours of the report.

A year later they came back. The standard fix for argument injection is the double dash that ends option parsing, but it had been removed from one call because git show gives the double dash a different meaning. That call read the file named in the composer.json readme key, straight from the attacker's manifest, into Mercurial. Same class of bug, same impact, fixed the next day, with the official note finding no exploitation on the public instance other than theirs.

## PEAR: a weak random number plus a known CVE

Paul Gerste took the second half. PEAR dates from 1999 and has served about 290 million downloads; PEAR accounts need manual approval, so they started with what works before login. SonarSource's own SonarQube flagged mt_rand in the password reset: the token was an MD5 of a random number between 4 and 13, the username, the server time (handily sent back in the Date header) and the new password. About 50 guesses take over any account, and the bug was 15 years old.

Account takeover is noisy, so they went for code execution. PEAR extracted uploaded packages with an outdated Archive_Tar affected by CVE-2020-36193: a tar with a symlink pointing into the web root, followed by a regular file of the same name, writes attacker-chosen PHP where the web server will execute it. Chain the two and every PEAR package can be backdoored quietly. The fix was committed quickly but took months to reach the live server, which is its own lesson.

## What should ecosystems change?

Their two answers. Reduce impact with mandatory code signing, so you trust the developer's identity rather than the registry; Sigstore, an append-only public ledger with ephemeral signing keys, is the project they point to. Paul Gerste said at Conf42 DevSecOps 2022: "In the end they are just simple tubes, a tunnel that you reach through to get what you want." Signing only works if it is mandatory, since an unsigned dependency of a signed package breaks the chain.

And reduce risk by actually reviewing the code. They know of fewer than ten researchers publishing bugs on these targets, and the bug bounty they tried did not accept these findings. He put it plainly: "So who's auditing all this open source software? We do it, but we can't audit all of it." Client-side tools have the opposite problem: nobody agrees on a threat model for running composer in an untrusted directory.

## Who should watch

Anyone running a private registry or depending on a public one, AppSec engineers who like a clean exploit chain, and PHP teams still pulling from PEAR (their advice: the popular packages are on Composer too, with a faster-patching community). It pairs well with [Henrik Plate on code-centric vulnerability management](https://www.conf42.com/DevSecOps_2022_Henrik_Plate_opensource_vulnerability_management_source), [Ciara Carey on making SBOMs actionable](https://www.conf42.com/DevSecOps_2022_Ciara_Carey_software_bill_of_materials_sboms_actionable) and [Sven Ruppert on supply chain security in open source projects](https://www.conf42.com/Cloud_Native_2023_Sven_Ruppert_supply_chain_security_opensource_projects).

[Watch Thomas Chauchefoin and Paul Gerste's talk](https://www.conf42.com/DevSecOps_2022_Thomas_Chauchefoin_Paul_Gerste_somebody_in_my_package_manager)

## From SonarSource

- [SonarSource](https://www.sonarsource.com/): SonarQube, SonarCloud and SonarLint, the static analysis tools the team used to start the PEAR research.

[Watch the talk on YouTube](https://youtu.be/hHDpuSEOfBM).

## Watch the talk

[Oops, there's somebody in my package manager!](https://www.conf42.com/DevSecOps_2022_Thomas_Chauchefoin_Paul_Gerste_somebody_in_my_package_manager) at Conf42 DevSecOps 2022.
