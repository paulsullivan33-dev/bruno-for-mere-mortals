# Running Collections

One request at a time is learning. A
**run** — the whole folder, in order,
with a verdict at the end — is testing.
This chapter is about `bru run` as a
runner: what it executes, in what order,
what it prints, what it writes down, and
the three ways a run can go wrong that
the lab captured for real.

## The command

From the collection's root:

```bash
bru run . --env local --env-var apiToken=lab-token-123
```

`.` is the path — a whole collection, a
folder inside one, or a single file all
work, which is how chapters 5 and 10 ran
individual requests out of the same
collection. `--env` chooses the
environment; `--env-var` supplies the
secret's value for this run only
(chapter 8). Add `-r` to recurse into
subfolders when you point at a folder
that contains them.

## Order and the summary

Requests run in the order their `seq`
numbers give them — the lab's health
check at 1 through the echo at 6 — and
each reports as it goes: name, status,
time, then its checks. The run ends with
the table this guide has quoted in
pieces. In full, from the passing run
(transcript t04):

```text
📊 Execution Summary
┌───────────────┬──────────────┐
│ Status        │    ✓ PASS    │
│ Requests      │ 6 (6 Passed) │
│ Tests         │     4/4      │
│ Assertions    │    11/11     │
│ Duration (ms) │     1018     │
└───────────────┴──────────────┘
```

Requests, tests and assertions are
counted separately because they fail
separately: a 401 fails assertions while
its request "succeeded" in the sending,
and chapter 10's wrong test failed a test
while its request returned 200. The
**exit code** collapses all of it into
one bit for scripts and CI: **0 if
everything passed, 1 if anything did
not** — including, as the next section
shows, requests that never received an
answer at all.

## The report files

A terminal scrolls away; a report stays.
`--reporter-json results.json` writes the
whole run as structured data — every
request as it was actually sent (headers
resolved, placeholders filled), every
response, every assertion's verdict
(transcript t08 shows the health check's
entry, including the runner's own
`User-Agent: bruno-runtime/4.3.0`, which
is also how a server sees that Bruno, not
a browser, called). JUnit and HTML
reports ride the same flags
(`--reporter-junit`, `--reporter-html`),
aimed at CI dashboards and humans
respectively. A CI job, in the end, is
this chapter's command plus a report
flag, gating a merge on the exit code.

## The three failures

The lab broke its own run three ways,
and each failure has its own voice.

**The server is not there.** With the
fixture stopped, a run reports the
connection's refusal in the request's own
line and fails the run (transcript t09):

```text
health check (connect ECONNREFUSED 127.0.0.1:18080)
```

No assertions are counted — there was no
response to assert about — and the exit
code is 1. A refused connection almost
always means the boring thing: the API
is not running, or the environment's
`host` points at the wrong port.

**The environment is not there.** A
mistyped `--env` stops the run before it
starts, in one line (also t09):
`Environment file not found:
environments/staging.bru`. Nothing was
sent; nothing could be mis-aimed.

**Something in the middle disagrees.**
The missing secret (chapter 8) and the
wrong expectation (chapter 10) both leave
the machinery intact and fail on content:
statuses, bodies, numbers. Their output
names the two values that clashed. When
a run fails, the first diagnostic act is
sorting the failure into one of these
three families — *never sent*, *never
answered*, *answered and disagreed* —
because each family has exactly one place
to look.

## Working habits

Run the single file while you write it
and the folder when you finish; the
folder run is the regression suite, and
its green table is the collection's
definition of "still true". Use `--bail`
when you want the run to stop at the
first failure — during debugging, the
fifth red line is rarely news. And when a
run surprises you, reach for the JSON
report before re-running: what was
*actually sent* is in it, placeholders
already filled, which ends most arguments
between a request file and its author.
