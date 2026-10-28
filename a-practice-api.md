# A Practice API

Every request in this guide is answered
by a server, so the lab built one worth
practising on: small enough to read in
one sitting, honest enough to teach with.
It is a single Python file using only the
standard library — no packages to
install — and it lives in the repository
at `bruno-lab/server/fixture_api.py`.

It pretends to be the stock room of an
invented bookshop. (Invented matters:
chapter 1's rule starts with your own
machine, and a fixture you wrote is the
one API you will ever meet whose
permission is never in doubt.) Its
endpoints:

| Endpoint | What it does |
|---|---|
| `GET /health` | Answers `{"status": "ok"}` — the hello of APIs |
| `GET /books` | The whole catalogue as a JSON list |
| `GET /books/2` | One book as JSON; a number it doesn't know gets a 404 |
| `POST /orders` | Reads a JSON body and echoes it back inside a receipt |
| `GET /whoami` | Refuses with 401 unless the request carries the lab's token |
| `GET /echo` | Reports the query string and two headers it received |
| anything else | A 404, on purpose |

Each endpoint exists to make one later
chapter possible: the list for assertions
about arrays, the echo for proving what a
script actually sent, `/whoami` for
chapter 8's secrets, the deliberate 404
for learning that a "failure" is
sometimes the correct answer.

## Starting it

```bash
python3 bruno-lab/server/fixture_api.py 18080
```

It listens on **127.0.0.1** — this
machine only, never the network — and
runs until you stop it with Ctrl-C. The
port, 18080, is chosen because nothing
else on a typical machine wants it; if
yours does, pass another number and
change one line in the environment file
in chapter 7 to match.

## Checking it without Bruno

Before any client enters the story, prove
the server stands on its own. With it
running, in a second terminal:

```text
$ curl http://127.0.0.1:18080/health
{"status": "ok"}
$ curl http://127.0.0.1:18080/whoami   (no token)
{"error": "missing or bad token"}
```

The lab's full set of checks — catalogue,
a 404 with its headers, the refused
`/whoami` — is transcript
`bruno-lab/transcripts/t01-server-checks.txt`.
Checking the server first is a habit, not
a courtesy: when a request later fails,
you will already know which side of the
conversation to suspect, and chapter 16
leans on that more than once.

## The token

`/whoami` opens for exactly one header,
`Authorization: Bearer lab-token-123`.
The value is invented for this guide,
printed here and in the server's source
because it guards nothing but a fiction —
and that is the last time in this guide a
secret's value appears in print.
Chapter 8 treats it the way a real token
deserves: declared in the collection,
valued nowhere in the committed files,
and supplied only at the moment of the
run. If you adapt this fixture for
anything real, change the token first and
keep the new value out of the repository
the same way.

## Stopping it

Ctrl-C in its terminal. A stopped server
is not a problem to avoid but a chapter
to read: chapter 11's runner meets one,
and transcript t09 keeps what `bru` has
to say about a refused connection.
