# Collections in Git

Everything so far has been leading to a
party trick that is not a trick: because
a collection is plain-text files, it can
live in **version control** like code —
and requests, being files, get code's
whole inheritance of diffs, reviews,
blame and history. This chapter does it
for real, with the lab's own collection,
and then sets down the discipline that
keeps the repository an asset instead of
a leak.

## The collection, committed

The lab initialised a git repository in
its collection folder, added everything,
and committed (transcript t06). The
tracked result:

```text
.gitignore
bruno.json
echo request vars.bru
environments/local.bru
get one book.bru
health check.bru
list books.bru
place an order.bru
who am i.bru
```

Nine files, every one of them readable
text. One file that exists in the folder
is *not* in that list — `.env`, holding
the token's value — because the
collection's `.gitignore` names it:

```text
# The one file that holds real secret values. Everything else
# in this collection is safe to commit; this one is not.
.env
```

And the proof that the arrangement works
is one command, run over the committed
repository:

```text
$ git grep -n "lab-token-123" || echo "no tracked file contains the token value"
no tracked file contains the token value
```

The environment file is tracked — with
the secret's *declaration* in it, and no
value. The value is on the machine, in an
ignored file, where chapter 8's design
put it.

## What git buys a collection

**Diffs.** Change a request's body and
`git diff` shows the changed lines of
JSON, exactly as sent. Compare that with
the incumbent tools' exports — a single
monolithic JSON blob in which one changed
header re-writes a thousand lines — and
the design argument of chapter 1 is over.

**Review.** A pull request that adds a
request can be read like a pull request
that adds a function: here is the
endpoint, here is what it sends, here are
the tests it carries. A reviewer can run
it. Nothing about the review requires
Bruno to be installed on the reviewer's
machine for the *reading* to make sense.

**History.** When an API changes and a
collection's checks turn red, the history
answers "what did this request look like
when it passed?" — which is often the
fastest route to whether the API moved or
the collection rotted.

**Onboarding.** A new colleague clones
two repositories now — the service and
its collection — and has, in the second,
a runnable, tested description of the
first one's API. It cannot silently rot
the way a wiki page does, because chapter
11's runner goes red when it stops being
true.

## The discipline

Three rules, all enforced by habit since
git cannot enforce them for you:

- **Secrets never enter the repository —
  at all, ever.** Not "removed before
  pushing": history is forever, and
  chapter 8's warning applies without
  discount: a committed credential is a
  compromised credential, to be rotated,
  not deleted.
- **Ignore the local by name.** The
  `.env` file, and any per-machine
  overrides, belong in `.gitignore` from
  the first commit, not after the first
  scare. A `.gitignore` checked in *with*
  the collection (as the lab's is) makes
  the safe path the default path for
  everyone who clones it.
- **Commit collections like code:**
  small changes, messages that say what
  the request now proves, and the tests
  run before the commit — chapter 11's
  exit code makes that a one-line habit
  or a one-line pre-commit check.

## Sync beyond git

The desktop app offers workspace features
for teams in the paid editions, and
nothing in this guide depends on them:
for a single person or a small team, the
repository *is* the sync — clone, pull,
push, the verbs this series' Git guide
teaches, applied to a folder that was
designed from the first file to deserve
them. *(Documented-only: the hosted
workspace features are characterised
here, not run; the git workflow above is
the verified path.)*
