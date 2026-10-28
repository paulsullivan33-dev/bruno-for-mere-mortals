# Bruno for Mere Mortals

An **API client** is the program you use
to talk to an API by hand: you type a
request — a method, an address, some
headers, maybe a body — and it shows you
the response, so you can learn what the
API really does before you write code
against it. The best-known client,
Postman, stores your requests inside its
own account and database. **Bruno** made
a different choice: every request is a
small **plain-text file** on your disk,
in a folder you own. That folder is a
**collection**, and because it is only
files, it can live in a **git**
repository next to the code that uses the
API — reviewed in pull requests, diffed
like code, shared by cloning.

Bruno has two faces. The **desktop app**
is a window for building and sending
requests by clicking. The **`bru` command
line** is its headless runner: it reads
the same files, sends the same requests,
checks the answers against **assertions**
and **tests** written into the files, and
reports pass or fail with an exit code a
script can use. The command line is the
centre of this guide, for a practical
reason: it is the face that runs in a
sandbox, in CI, and in this guide's lab —
and everything it does can be shown to
you as a transcript. The desktop app is
described honestly wherever it matters
and is labelled documented-only; the lab
never opened it.

The rule for this material is the series'
usual one, and it is stated in chapter 1:
**test your own APIs, on your own
machines, or with explicit permission.**
An API client sends whatever you tell it
to send, and Bruno's saved requests make
it easy to send them again, faster and in
bulk. The lab obeyed the rule in its
strictest form: every request in this
guide went to a practice server the lab
wrote itself, running on the same
machine, and the one "secret" in the
story is an invented token that unlocks
nothing anywhere else.

The lab behind this guide ran the real
thing: **Bruno CLI 4.3.0** (the npm
package `@usebruno/cli`, on Node.js 24),
installed into a scratch folder so
nothing on the machine changed. Against
it stood a **fixture API** — a small
Python program written for this guide
that serves an invented bookshop's stock
room: a health check, a list of books,
one book at a time, an order endpoint
that echoes what it was sent, and one
door that opens only for the right token.
The lab wrote a six-request collection as
files, ran it until every check passed,
then broke it on purpose three different
ways — a missing secret, a wrong
expectation, a stopped server — and kept
the failure output of each, because the
failures are where a test tool earns its
keep. It also put the collection into a
real git repository and proved, with
`git grep`, that the token's value is in
no tracked file.

What the lab could not do, it did not
fake. The desktop application never ran
here, so its windows are described from
the project's documentation, not
demonstrated; the same goes for the
commercial editions' secret-manager
integrations and the newest workspace
features. `criteria.md` keeps the full
ledger of what was run and what was only
read.

## What this guide covers

- [**What Bruno is**](what-bruno-is.md) —
  the mental model: requests as files, a
  collection as a folder, and the rules
  that come with a tool that sends
  whatever you saved
- [**The moving parts**](the-moving-parts.md) —
  the desktop app, the `bru` runner, the
  `.bru` file format, environments and
  variables, scripts and reports — and
  which part holds what
- [**Installing Bruno**](installing-bruno.md) —
  the desktop downloads, and the npm
  install of the CLI that this guide's
  lab used and verified
- [**A practice API**](a-practice-api.md) —
  the fixture server: endpoints that
  answer JSON, check a token, and echo
  what they receive, all on your own
  machine
- [**Your first request**](your-first-request.md) —
  one `.bru` file written by hand, run
  with `bru`, and read line by line
- [**Reading a request file**](reading-a-request-file.md) —
  the anatomy of the format: blocks,
  bodies, headers, and the placeholders
  that variables fill in
- [**Environments and variables**](environments-and-variables.md) —
  one collection, many targets: the
  `{{host}}` trick, environment files,
  and the order variables are looked up
- [**Secrets**](secrets.md) — declaring
  a variable secret, where its value may
  live if not in the committed files, and
  the two traps the lab fell into so you
  don't have to
- [**Assertions**](assertions.md) — the
  checkbox style of checking: status,
  body values, and the hyphen trap in
  header names
- [**Tests and scripts**](tests-and-scripts.md) —
  JavaScript checks with names, a
  genuinely failing test read closely,
  and scripts that run before a request
- [**Running collections**](running-collections.md) —
  the whole folder at once: order,
  summaries, exit codes, and the reports
  a CI system can eat
- [**Collections in git**](collections-in-git.md) —
  the payoff of files: diffing a request,
  reviewing one, and what the repository
  must never contain
- [**Recipes**](recipes.md) — explore an
  API you just met, turn a bug report
  into a saved failing request, keep a
  smoke test for your own service
- [**The neighbours**](the-neighbours.md) —
  Postman and Insomnia, curl and HTTPie,
  and the API documentation tools: what
  each keeps that Bruno doesn't, and
  vice versa
- [**Limits**](limits.md) — a desktop
  app this guide could not open, formats
  that strain, no shared cloud, and the
  ethical edge, stated plainly
- [**Troubleshooting**](troubleshooting.md) —
  the refused connection, the environment
  that isn't there, the secret with no
  value, and the parse error that names
  its own line
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Testing other people's APIs without
permission — chapter 1 explains the line,
and load-testing a service you do not
run sits on the far side of it. The
desktop application's windows in
click-by-click detail: the lab could not
run it, and a guide that invents
screenshots would be lying to you; its
file format, which is where the durable
knowledge lives, is covered completely.
The paid editions' team workspaces and
secret-manager integrations are
characterised in chapters 2 and 13, not
taught. Writing APIs themselves is the
neighbouring guide in this series (see
the footer); this one stays on the
client side of the conversation.

## How to use this guide

Read chapter 1 for the model and the
rules, and chapter 2 before installing
anything — knowing which part is the
file, which part is the runner, and
which part is the window turns later
confusion into a named problem. Chapter 4
builds the practice API and chapter 5
sends it your first request in the same
sitting; keep both on your own machine
until running a collection feels boring.
Chapter 8, on secrets, is the chapter to
read twice: Bruno's whole design is an
answer to "my saved requests keep leaking
credentials", and the answer only works
if you use it the way chapter 8 shows.
The lab's transcripts live in
`bruno-lab/transcripts/`; its fixture
server is `bruno-lab/server/` and its
collection `bruno-lab/collection/`; its
notes are `examples/lab-notes.txt`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [APIs for Mere Mortals](https://paulsullivan33-dev.github.io/api-for-mere-mortals/)
- [curl for Mere Mortals](https://paulsullivan33-dev.github.io/curl-for-mere-mortals/)
- [Git for Mere Mortals](https://paulsullivan33-dev.github.io/git-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/bruno-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/bruno-for-mere-mortals/blob/main/LICENSE-CODE).
