# Limits

An honest chapter about where Bruno ends.
None of these are reasons to avoid it;
all of them are reasons to choose it
knowingly.

## The face this guide could not open

The desktop application is how most
people will use Bruno, and this guide
could not run it — the lab's machine has
no desktop. Everything said here about
its windows, its editors and its local
secret store comes from the project's
documentation and is labelled as such,
but it is a real limit of *this guide*:
if the app and this text disagree about a
menu, believe the app. The CLI, the file
format and the run behaviour — the parts
a transcript can prove — are verified to
the standard the rest of the series
keeps.

## A young format, still moving

Bruno is a young project and its grammar
is still settling. The lab's own bruise
is chapter 8's: a secrets declaration
that older writing shows as a block is
now an array, and the CLI rejects the old
form with a parse error. Expect that
species of change again — collections
written today may need small edits under
tomorrow's CLI, and advice found online
may describe a Bruno that no longer
exists. Pin the CLI version in any CI job
that matters, and treat a sudden parse
error after an upgrade as a version
question before a competence question.

## The centre of gravity is HTTP and JSON

Bruno is built for the world's common
case: HTTP APIs that speak JSON. Around
that centre the ground thins.
Authentication schemes beyond the common
set (bearer, basic, digest, OAuth flows
the app assists with) can mean hand-work
in scripts; protocols that are not plain
HTTP requests are neighbours' territory
(chapter 14); and binary bodies, streaming
responses and enormous payloads are
things a request-file tool handles
awkwardly at best. A collection is also
the wrong shape for a test that needs a
database reset between steps or a
browser's rendering — those belong to
chapter 14's in-house neighbour, the
test suite.

## It is not a load tool

The runner can repeat requests, and CI
flags make repetition easy — which raises
chapter 1's edge in practical form.
Against your own service on your own
machine, repetitions are how you learn.
Against anyone else's API, a loop of
saved requests is a flood with a file
format, and "the tool let me" has never
been the permission that matters. Bruno
also makes no attempt to *measure* under
load — timings in its reports are
per-request courtesies, not benchmarks —
and tools built for load exist and are
better neighbours for that job.

## Secrets are a discipline, not a feature

Chapter 8's machinery prevents the
ordinary accident — the value filed in
the request — and nothing more. Values
passed on a command line can land in a
shell's history; `.env` files are plain
text to anyone who can read the folder;
and the JSON report (chapter 11) records
requests *as sent*, headers included, so
a report of an authenticated run can
carry the very credential the collection
kept out of its files. Treat reports like
recordings: useful, sensitive, and not
for the repository. Bruno gives you the
untracked path; walking it stays your
job, every run.

## Sharing stops at the repository's edge

The open-source core's collaboration
story is chapter 12's git — excellent,
and bounded. There is no shared live
workspace in the free tool, no comment
thread on a request, no central place a
whole company watches; the paid editions
add workspaces and vault integrations,
documented-only here. A team that needs
a platform, rather than a folder and a
discipline, is shopping in chapter 14's
first neighbourhood, and Bruno's own
honesty about that is a point in its
favour.

## The legal and ethical edge

The rule from chapter 1 — *your APIs,
your machines, or explicit permission* —
has teeth outside this guide's opinion:
unauthorised testing of other people's
systems is a crime in many jurisdictions
however polite the client, saved requests
containing someone else's credentials are
a problem however they were obtained,
and an employer's API is explored within
the employer's authorisation, not your
curiosity's. Everything inside the line
encloses years of interesting, useful
work, and needs no apology and no
concealment. Beyond it, you are not
debugging any more.
