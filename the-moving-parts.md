# The Moving Parts

Bruno looks like one program and is
better understood as five pieces with a
strict rule about which piece holds what.
When something confuses you later — a
variable that will not fill in, a secret
that is not where you left it — the
confusion almost always names one of
these pieces.

## The collection folder

The unit of organisation is the
**collection**: a folder on disk. At its
root sits one small file, `bruno.json`,
which names the collection and says it
is one:

```json
{
  "version": "1",
  "name": "Bookshop Stockroom API",
  "type": "collection"
}
```

Everything else in the folder is requests,
subfolders of requests, and an
`environments` folder. There is no
database and no hidden state; the lab's
whole collection, listed in transcript
t06, is nine files. If you can see the
folder, you have the collection — copying
it copies it, and chapter 12 puts it in
git.

## The request file

Each request is one **`.bru` file**:
plain text in the Bru format, blocks of
`key: value` lines between braces. One
file holds the request itself (method,
address, headers, body, authentication),
plus any **assertions**, **tests** and
**scripts** attached to it, plus
documentation. Chapter 6 reads a file
block by block. Because the file is the
request, two requests are two files, and
a request's checks travel with it
wherever the file goes.

## The two faces

The **desktop app** is the interactive
face: it shows the collection as a tree,
one request as a form, and the response
in panes. Building and editing files by
clicking is its job. *This guide does not
run it* — the lab had no desktop to open
it on — so its windows are
documented-only here, described from the
project's own documentation in the
chapters that mention them.

The **`bru` CLI** is the headless face,
published as the npm package
`@usebruno/cli`. Given a file, a folder,
or a whole collection, it sends the
requests, evaluates their assertions and
tests, prints a readable report, and
exits 0 or 1. Everything the lab
demonstrates, it demonstrates through
this face: the same files the app would
open, exercised by the runner that CI
systems use.

The two faces read and write the same
files, which is the point of the design:
a request built by clicking in the app is
runnable by `bru` that night, and a
request written by hand in an editor —
every request in this guide was — opens
in the app unchanged.

## Environments and variables

A request file rarely contains a real
address. It contains a placeholder —
`{{host}}` — and an **environment** file
supplies the value. Environments live in
the collection's `environments` folder,
one `.bru` file each, and hold
**variables**: names and values for one
place the collection can aim. Chapter 7
takes this apart; chapter 8 is about the
special kind of variable, the **secret**,
whose value is deliberately kept out of
the committed files.

Around those sit two more sources: the
**process environment** (variables from
the operating system and a `.env` file,
reached as `{{process.env.NAME}}`), and
values set while a run is going, by
scripts. Knowing which source a value
came from is most of debugging Bruno,
and chapter 7 gives the lookup order.

## Scripts, tests and reports

Request files can carry small JavaScript
programs: a **pre-request script** that
runs before sending (to set a variable or
compute a value), a **post-response
script**, and a **tests** block that
checks the response with named
expectations. Chapter 10 runs all three
for real. Scripts run in a **sandbox**:
by default a restricted one, with a
freer "developer" mode behind a flag —
the sandbox exists because a collection
you cloned is code you are about to run,
and chapter 15 says what that means.

What a run produces is a **report**: the
terminal summary this guide quotes, an
exit code, and — on request — a JSON,
JUnit or HTML file with every request,
response and check recorded (chapter 11).
The report is the piece CI reads.

## The editions, briefly

Bruno the open-source project covers
everything in this guide. The project
also sells editions with multi-user
workspaces, a visual Git interface, and
integrations that fetch secrets from
external vaults (chapter 8 names them).
Those are documented-only here —
characterised, not run — and nothing in
the core format depends on them: the
files stay files, and editions read the
same ones.
