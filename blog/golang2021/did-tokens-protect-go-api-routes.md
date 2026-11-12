# Passwordless auth for a Go API, one bearer-token middleware at a time

Conf42 Blog, 2021-06-25. https://www.conf42.com/blog/golang2021/did-tokens-protect-go-api-routes

In short: Mohammad Shahbaz Alam (Magic) at Conf42 Golang 2021 on protecting Go API routes with signed decentralized identity tokens instead of passwords

If your users never type a password, there's no password database to leak. At Conf42 Golang 2021, Mohammad Shahbaz Alam, Developer Advocate at Magic, shows what that looks like from the Go side: a gorilla/mux API whose protected routes accept only a decentralized identity (DID) token, validated by a small middleware before the handler runs.

It's a vendor talk built on Magic's SDKs, and it says so from the first slide. The useful part for any Go developer is the shape of the middleware and the split between what the client does and what the server must check.

## What's wrong with passwords, in numbers?

Mohammad opens with the case against the shared-secret model. Users invent a password and hand it to every app they use; per his slides, 59% of users reuse passwords across apps. Many companies roll their own authentication without security expertise, every login exposes the secret again, and a breach takes the users' trust with it: 48% of customers never come back after one, and the Equifax breach cost at least $1.4 billion.

The alternative that came before was key-based, zero-knowledge authentication: random public-private key pairs instead of secrets. Users control their identity and companies never see a secret, but users lose keys, and most people find the whole idea unfamiliar. Magic's answer is delegated key management: keys held in hardware security modules on a large cloud provider, retrieved through familiar flows like an emailed magic link, social login or WebAuthn. Mohammad is upfront about the trade-off he names: reliance on a single infrastructure provider.

## What is a DID token?

A DID token borrows from JWT and the W3C's DID protocol. It's a Base64-encoded JSON tuple of proof and claim. The claim carries the user's data: issuer (the user's public address), issued-at, expiry, subject, not-before and so on. The proof is the claim signed with Ethereum's personal sign method, using elliptic curve cryptography, so the server can verify who signed it.

On the client, the SDK's login-with-magic-link call emails the user, polls every two seconds until they click, then returns a DID token. The default lifespan is 15 minutes; you can request a longer one in seconds (the demo uses 8 hours).

He also gives the cleanest one-line version of the distinction many auth talks blur: authentication asks whether you are who you say you are, authorization asks whether you're allowed to do this action. The demo covers both.

## The Go side is a middleware and three checks

The starting point is a plain Go API on port 9000: a home route and a protected route that, at first, isn't protected. The secured version adds a `checkBearerToken` middleware that wraps the protected handler:

1. Read the Authorization header and reject the request unless it carries the Bearer prefix.
2. Strip the prefix, parse the DID token, and reject it if it's malformed.
3. Validate the token with the Magic admin SDK for Go, using the secret key loaded from an env file (the publishable key stays on the client).

Only then does it call the next handler. As a bonus, the middleware fetches the user's metadata by token (email, issuer, public address) so the handler knows who is calling. The server-side rule is the one to remember.

"Every did token must be validated at server side," Mohammad Shahbaz Alam said at Conf42 Golang 2021.

The demo grabs a token from a Next.js front end scaffolded with the make-magic CLI, pastes it into Postman as a bearer token, and gets the protected page plus the caller's identity back. Without the token the API answers that a bearer token is required.

## Authorization: you can't delete someone else's tweet

The second demo moves from authentication to authorization with a small CRUD API Magic's guides call a scrappy Twitter API. Listing tweets is open. Creating one requires a valid DID token and records the token's email as the author. Deleting a tweet someone else wrote fails with a clear refusal even with a valid token; deleting your own works. That ownership check, using the identity the token proves, is the part most auth tutorials skip.

## Who should watch?

Go developers adding login to an API for the first time, or anyone curious how passwordless and blockchain-key identity look in practice from the server's side. If you already run OAuth or OIDC in production, the middleware will look familiar; the token format and key-custody model are what's new. The code is on GitHub in the speaker's frontend-go-api and magic-go-api repositories.

More Go security from Conf42: [Mahendra Bagul on secured gRPC with mTLS and an NGINX ingress](https://www.conf42.com/Golang_2021_Mahendra_Bagul_KinD_nGinx_Ingress_Controller_Secured_gRPC_server), [Mathilde Raynal on quantum-resistant Go programs](https://www.conf42.com/Golang_2021_Mathilde_Raynal_quantumresistant_native_go_programs), and [Marvin Collins Hosea on building secure webhooks](https://www.conf42.com/Golang_2023_Marvin_Collins_Hosea_building_secure_scalable_webhooks).

[Watch Mohammad Shahbaz Alam's talk](https://www.conf42.com/Golang_2021_Mohammad_Shahbaz_Alam_API_authorization) from [Conf42 Golang 2021](https://www.conf42.com/golang2021).

## From Magic

The talk uses Magic's client SDK for login with magic links and DID tokens, and the Magic admin SDK for Go to validate tokens and read user metadata on the server.

- Magic: [magic.link](https://magic.link)
- Magic docs: [docs.magic.link](https://docs.magic.link)
- Magic admin SDK for Go: [getting started](https://docs.magic.link/admin-sdk/go/get-started)

[Watch the talk on YouTube](https://youtu.be/6JtctR2C0Ww).

## Watch the talk

[Secure your Go APIs with Decentralised Identity Tokens](https://www.conf42.com/Golang_2021_Mohammad_Shahbaz_Alam_API_authorization) at Conf42 Golang 2021.
