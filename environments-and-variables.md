# Environments and Variables

A collection that can only talk to one
server is a diary. What makes it a tool
is that the same files can aim at your
practice server today, a test server
tomorrow, and the real service when you
are ready — without editing a single
request. The mechanism is two pieces:
**variables**, named values used as
`{{placeholders}}`, and **environments**,
files that give those names values for
one target.

## The environment file

Environments live in the collection's
`environments` folder, one file each, and
are chosen by name when you run:
`--env local` reads
`environments/local.bru`. The lab's is
the smallest useful one:

```bru
vars {
  host: http://127.0.0.1:18080
}
vars:secret [
  apiToken
]
```

A second target — say a test server on
another machine — would be a second file,
`environments/staging.bru`, with a
different `host` and its own secret
declaration, and the same requests would
run against it unchanged. A run that
names an environment which does not exist
fails before sending anything, in one
plain line (transcript t09):

```text
Environment file not found: environments/staging.bru
```

That bluntness is a virtue: a typo in
`--env` can never silently aim a
collection at the wrong server carrying
the wrong token.

## Where variables come from

When Bruno meets `{{host}}`, it looks the
name up in a definite order. The sources,
as the documentation sets them out and
the lab confirmed for the ones it used:

- **The chosen environment** — its `vars`
  block, and its declared secrets once a
  value reaches them (chapter 8).
- **Command line overrides** —
  `--env-var host=http://127.0.0.1:9999`
  beats the file, which is how chapter 11
  points the whole collection at a server
  on a different port without editing
  anything.
- **Runtime variables** — set by scripts
  while a run is going, with
  `bru.setVar` (chapter 10). These live
  only for the run.
- **Collection and folder variables** —
  values declared once for a whole
  collection or one folder of it, in
  files the app edits and the CLI reads.
  *(Described from the documentation; the
  lab's collection is small enough to
  live without them.)*
- **The process environment** — the
  operating system's variables and a
  `.env` file in the collection root,
  reached by a different spelling:
  `{{process.env.NAME}}`. Chapter 8 shows
  why the spelling matters — the lab's
  most instructive 401 came from using
  the wrong one.

A placeholder that finds no value
anywhere is left as-is in the outgoing
request — one reason chapter 5 warns
about stray spaces inside braces:
`{{ host }}` is a different, emptier
variable than `{{host}}`.

## Variables inside values

A variable's value may itself contain
placeholders — `host` could be built from
a `scheme` and a `port` variable — and
Bruno resolves them when the request is
sent. The lab kept its environment flat
on purpose: an environment file is read
most often at the moment something else
has already gone wrong, and flat files
confess faster.

## Choosing names

Two habits pay for themselves. Name the
target, not the machine's owner or
purpose: `local`, `staging`, `prod` will
outlive any particular box. And keep the
set of variable *names* identical across
environments — a name missing from one
file is a request that goes out with a
raw `{{placeholder}}` in it, which the
receiving server will reject in some
confusing dialect of 400. The collection
is the contract; the environments are
just the addresses written on it.
