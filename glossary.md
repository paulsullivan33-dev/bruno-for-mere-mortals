# Glossary

**API client** — a program for sending
HTTP requests by hand and reading the
responses; Bruno is one (chapter 1).

**Assertion** — a one-line check on a
response, written in an `assert` block:
a place, an operator, a value
(chapter 9).

**Bearer auth** — an authentication
scheme in which a request carries
`Authorization: Bearer <token>`; the
token is the whole credential
(chapter 8).

**Bru** — Bruno's plain-text file
format, and the extension of its files,
`.bru` (chapter 6).

**`bru`** — the command line runner
(the npm package `@usebruno/cli`) that
sends a collection's requests and
reports pass or fail (chapter 3).

**Collection** — a folder of request
files plus a `bruno.json`, Bruno's unit
of organisation (chapter 2).

**Environment** — a file in a
collection's `environments` folder
giving variable values for one target
(chapter 7).

**Exit code** — the number a command
leaves behind for scripts to read;
`bru run` ends 0 when everything
passed, 1 when anything did not
(chapter 11).

**Fixture API** — a practice server
written to be tested against; this
guide's is a small Python program
(chapter 4).

**JSON report** — the machine-readable
record of a run, written with
`--reporter-json` (chapter 11).

**Placeholder** — a `{{name}}` in a
request, filled from a variable when
the request is sent (chapter 7).

**Pre-request script** — JavaScript in
a `script:pre-request` block, run
before its request is sent
(chapter 10).

**Process environment** — the operating
system's variables, plus a collection's
`.env` file, reached as
`{{process.env.NAME}}` (chapters 7–8).

**Sandbox** — the restricted mode
Bruno's scripts run in by default;
a freer developer mode exists behind a
flag (chapter 10).

**Secret variable** — a variable
declared by name in an environment's
`vars:secret` list, whose value is
supplied at run time and never written
into the committed files (chapter 8).

**`seq`** — the number in a request's
`meta` block giving its place in a
folder run's order (chapter 6).

**Test** — a named JavaScript check in
a `tests` block, using `test(...)` and
`expect(...)` (chapter 10).
