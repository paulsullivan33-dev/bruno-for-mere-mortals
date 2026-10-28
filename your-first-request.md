# Your First Request

This chapter takes you from an empty
folder to a passing check: one request,
written by hand in a text editor, run by
`bru`, against the practice API from
chapter 4. Start that server first and
leave it running; everything here talks
to it.

## The shape of a collection

Make a folder and give it the one file
that makes it a collection,
`bruno.json`:

```bash
mkdir bookshop-api
cd bookshop-api
```

```json
{
  "version": "1",
  "name": "Bookshop Stockroom API",
  "type": "collection"
}
```

That is the whole ceremony. The desktop
app would write this file for you; by
hand it is four lines, and reading it
tells you what the app would have hidden:
a collection is a folder that declares
itself.

## The environment

The request needs an address, and the
guide's rule is that addresses live in
**environments**, not in requests. Make
the folder and its first file,
`environments/local.bru`:

```bru
vars {
  host: http://127.0.0.1:18080
}
vars:secret [
  apiToken
]
```

Two blocks. The first sets an ordinary
variable, `host`. The second declares
`apiToken` a **secret** and — notice —
gives it no value. Chapter 8 is devoted
to that empty space; for this chapter,
the health check does not need the token,
so its absence costs nothing yet. Keep
the square brackets exactly as written;
chapter 8 shows the error the older
braces form earns, because the lab earned
it first.

## The request

Now the request itself, in a file named
`health check.bru`:

```bru
meta {
  name: Health Check
  type: http
  seq: 1
}

get {
  url: {{host}}/health
  body: none
  auth: none
}

assert {
  res.status: eq 200
  res.body.status: eq ok
}
```

Three blocks, each a chapter of this
guide in miniature. `meta` names the
request and gives it a running order
(`seq`) for when the whole folder runs.
`get` is the request: a GET to
`{{host}}/health`, the placeholder filled
from the environment. `assert` is two
checks on the response: the status is
200, and the body's `status` field is
`ok`. Chapter 6 reads the format closely;
for now, trust that what you see is all
there is.

## Running it

From inside the collection folder:

```bash
bru run "health check.bru" --env local
```

The quotes matter — the file name has a
space, and so will most of yours, because
requests named in plain words are the
ones you can still read in a year.
`--env local` chooses the environment
file `environments/local.bru` by name.

Check: the lab's run (transcript
`bruno-lab/transcripts/t02-first-run.txt`):

```text
health check (200 OK) - 23 ms
Assertions
   ✓ res.status: eq 200
   ✓ res.body.status: eq ok

📊 Execution Summary
...
│ Status        │    ✓ PASS    │
...
bru exit code: 0
```

Read it in three parts. The first line
is the request's name, the answer's
status, and how long it took. The middle
is your checks, each with its tick. The
table is the verdict — and below it, the
exit code is 0, which is the form of the
verdict a script or a CI system reads.
Chapter 11 runs the whole folder and
takes the summary apart; here, one
request passing is the outcome, and you
have it.

## If yours did not pass

The three beginners' failures are all in
chapter 16 with their real output: the
server is not running (connection
refused, transcript t09), the environment
name is wrong (Bruno says so in one
line), or a `{{placeholder}}` was typed
with spaces inside the braces, which
makes it a different variable that has no
value. Start there before suspecting the
format.
