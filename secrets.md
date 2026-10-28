# Secrets

Every real API eventually asks for a
credential — a token, a key, a password —
and a saved-request tool has to put that
credential somewhere. Put it in the
request file and the file becomes a leak
waiting for its first commit; Bruno's
whole design is a refusal to do that.
This chapter is the refusal, mechanism by
mechanism, including the two traps the
lab fell into while learning it. Read it
twice, as the README suggested: of all
the chapters, this is the one whose
mistakes travel.

## Declare the name, never the value

An environment file may declare a
variable **secret**. The declaration
lists names only:

```bru
vars:secret [
  apiToken
]
```

The committed file says *that* the
collection needs a token, and nothing
else about it. The request that uses it
looks entirely ordinary — the lab's
`who am i.bru`:

```bru
auth:bearer {
  token: {{apiToken}}
}
```

The value has to arrive from outside the
committed files, at the moment of the
run. How it may arrive is the rest of
this chapter.

## Trap one: the syntax moved

Older Bruno documentation — and the
desktop app's habits as described in
older writing — show the declaration as a
block of bare names:

```bru
vars:secret {
  apiToken
}
```

The current CLI refuses that file before
running anything, and the refusal names
its line and its expectation (transcript
`bruno-lab/transcripts/t90-secret-syntax-trap.txt`,
stack trace trimmed):

```text
Error: Line 4, col 13:
  3 | }
> 4 | vars:secret {
                  ^
  5 |   apiToken
Expected "["
```

The lesson generalises past secrets:
Bruno is young, its grammar is still
settling, and a parse error that looks
like your mistake may be a version's. The
fix here is the array form above, which
is what the lab shipped.

## A secret with no value

Suppose the declaration is right and no
value ever arrives. Bruno does not stop
the run or blank the request theatrically:
it sends the request *without* a usable
token, and the server answers as servers
do. In the lab (transcript t03), with the
practice API's door closed:

```text
who am i (401 Unauthorized) - 3 ms
Assertions
   ✕ res.status: eq 200
      expected 401 to equal 200
   ✕ res.body.user: eq stockroom
      expected undefined to equal 'stockroom'
```

Read that failure correctly: nothing is
wrong with the request file, the
environment file, or the server. The
value simply never showed up. When a
request that "worked yesterday" returns
401 today, the value's journey — not the
request — is the first suspect.

## Supplying the value at run time

The CLI accepts a value on the command
line, per run, leaving every file
unchanged:

```bash
bru run . --env local --env-var apiToken=lab-token-123
```

With that one addition, the lab's full
collection passes, `who am i` included
(transcript t04). A value passed this way
lives in your shell's history and in the
process list while the run lasts —
acceptable for a practice token, worth a
moment's thought for a real one; shells
offer history-suppressing tricks, and CI
systems offer secret stores, for exactly
this.

The desktop app's route is different and
is documented-only here: there, a secret
variable's value is typed into the app
and kept in a local store on your
machine, encrypted where the operating
system offers it, never written into the
collection's files. Same discipline, two
doors — the value is *supplied*, never
*filed*.

## Trap two: the .env that doesn't feed

Bruno also reads a `.env` file in the
collection root — the conventional place
projects keep local secrets — and it is
natural to expect `apiToken` written
there to fill `{{apiToken}}`. It does
not. The lab tried exactly that
(transcript t05): the door stayed shut,
401, because a `.env` feeds the **process
environment**, a separate shelf. Values
on that shelf are reached by their full
address:

```bru
token: {{process.env.apiToken}}
```

With the request written that way and
the same `.env` in place, the run passes
(transcript t05b). Neither spelling is a
bug; they are two different variable
sources (chapter 7), and confusing them
costs exactly one confusing 401 to learn
— the lab paid it so the price is on the
page.

Two corollaries. A `.env` file must be
kept out of git with the same seriousness
as any secret: the lab's collection
carries a `.gitignore` for exactly that
one file, and chapter 12 proves the
arrangement with `git grep`. And a
`.env` is a local convenience, not a
vault: anyone who can read your folder
can read it.

## Vaults and managers

For teams, Bruno's paid editions can
fetch a secret's value at run time from
an external manager — HashiCorp Vault,
AWS Secrets Manager, Azure Key Vault are
the documented set — with the CLI told
where its own credentials for the vault
live via a secrets file of `BRUNO_*`
keys. *(Documented-only: characterised
from the project's documentation, not
run, and beyond what a single-person
collection needs.)* The shape is the
chapter's shape at larger scale: names in
the files, values in a system built to
hold them, the meeting arranged at the
moment of the run.

## The standing warning

Everything above is machinery for one
rule: **a value that has ever been
committed must be treated as
compromised — rotate it, don't just
delete it.** Chapter 12 shows the lab's
collection passing a `git grep` for its
token because the token was never in a
tracked file. If yours ever is, deleting
the line removes the evidence from the
latest copy and none of the history; the
only honest repair is a new credential.
Bruno cannot want this for you. It can
only make the untracked path the easy
one — and, as this chapter showed, it
mostly does.
