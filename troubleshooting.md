# Troubleshooting

The failures this guide's lab actually
met, in the order a beginner is likely to
meet them, each with the output that
names it. The general method comes first:
decide which of chapter 11's three
families the failure belongs to — *never
sent*, *never answered*, *answered and
disagreed* — because each family has one
place to look.

## "connect ECONNREFUSED" — the server is not there

```text
health check (connect ECONNREFUSED 127.0.0.1:18080)
```

(transcript t09). The request was written
correctly; nothing was listening at the
address it was sent to. Almost always the
boring truth: the API is stopped, or it
is running on a different port than the
environment's `host` claims. Prove the
server before touching the collection —
chapter 4's curl checks take ten seconds —
then check the port in
`environments/<name>.bru` against the one
the server printed when it started.

## "Environment file not found" — the name is wrong

```text
Environment file not found: environments/staging.bru
```

(also t09). `--env` takes the file's name
without its folder or extension. If the
name is right and the error persists, you
are standing in the wrong folder: `bru`
reads `environments/` relative to the
collection it was pointed at, so run from
the collection's root, or point at the
collection folder explicitly.

## A 401 on the request that "has" a token

The chapter 8 family, and the most common
confusion in the tool. Three distinct
causes wear the same 401:

- **The value never arrived.** The secret
  is declared, the request is right, and
  no `--env-var`, app store or vault
  supplied a value for this run. The run
  sends the request anyway; the failure
  prints as chapter 8's t03 excerpt.
- **The value is on the wrong shelf.** A
  `.env` feeds `{{process.env.NAME}}`,
  not `{{NAME}}`. Chapter 8's trap two,
  transcript t05 versus t05b.
- **The value is wrong.** The server is
  the authority: chapter 4's curl with
  the header typed by hand settles in one
  line whether the credential or the
  plumbing is at fault.

## The assertion whose "actual" is an error

```text
✕ res.body.headers.X-Lab-Marker: eq ...
   expected { name: 'ReferenceError', … } to equal '...'
```

(chapter 9, transcript t03). The path was
read as arithmetic because the key
contains hyphens. Any key with characters
beyond letters, digits and underscores
needs the bracket form:
`res.body.headers["X-Lab-Marker"]`. When
an "actual" value looks like an error
object instead of data, suspect the path,
never the API.

## A parse error that names its line

```text
Error: Line 4, col 13:
> 4 | vars:secret {
Expected "["
```

(transcript t90). Bruno's grammar reports
the line, the column, and what it
expected — believe all three literally.
If the file "used to work", the grammar
moved: diff your CLI version against the
version the file was written for
(chapter 15) before rewriting anything
else. Secrets in the current grammar are
an array, `vars:secret [ apiToken ]`.

## Everything passes but the run "did nothing"

One request where you expected six: you
pointed `bru` at a single file, or at a
folder whose requests live one level
down without `-r`. Point at the
collection root (`.`, from inside it) for
the whole suite, and check the summary's
Requests line — it always confesses how
many requests actually ran.
