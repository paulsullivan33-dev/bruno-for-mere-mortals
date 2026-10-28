# What Bruno Is

Programs talk to each other over **APIs**:
one program sends an **HTTP request** —
*GET this address, here are my headers,
here is my data* — and another answers
with a status and, usually, some **JSON**.
When you are building either side of that
conversation, you spend a lot of time
sending requests by hand and squinting at
what came back. The tool for that job is
an **API client**.

**Bruno is an API client whose memory is
a folder of plain-text files.** Each
request you save becomes one small file,
written in a format called **Bru**. A
folder of those files, plus a small
settings file, is a **collection**. There
is no account to create, no cloud the
collection is uploaded to, and nothing
about your requests stored in a format
only Bruno can read. Open a request file
in any text editor and you can read the
whole request — method, address, headers,
body, and the checks it carries — because
there is nothing else to it.

That one decision shapes everything else
in this guide:

- A collection can live in a **git
  repository**, beside the server code it
  tests. Chapter 12 shows the collection
  from this guide's lab as nine small
  tracked files.
- A change to a request shows up in a
  **diff** like a change to code, so a
  pull request can review it like code.
- Anything that can read text files —
  your editor, your scripts, this series'
  other tools — can work with a
  collection. Nothing is locked in.

## The two faces

Bruno ships as a **desktop application**
for Windows, macOS and Linux: windows,
menus, a form for building a request, a
pane for reading the response. That is
how most people meet it, and chapter 2
describes it.

The same project publishes a **command
line runner**, `bru`, as an npm package.
It reads the identical files and sends
the identical requests, but its output is
text and its verdict is an **exit code**,
which makes it the face that fits scripts
and continuous integration. It is also
the face this guide could run for real,
so it is the face the lab used and the
one most chapters demonstrate. Be clear
about what that means: **this guide's
hands-on verification is the CLI.** The
desktop app is described from the
project's documentation and labelled
documented-only wherever it appears, in
the open, starting here.

## Why anyone would do this

- **Learning an API.** Documentation
  says what an endpoint should do. A
  saved request shows what it did — the
  exact status, the exact body — and
  stays saved when the answer changes.
- **Debugging.** Your program's request
  fails and the server's error is vague.
  Rebuild the request in Bruno, change
  one thing at a time, and watch which
  change fixes it. The request that works
  is evidence, not a memory.
- **Regression-keeping.** A request that
  once exposed a bug can carry **tests**
  (chapter 10) and be re-run after every
  fix, forever, by a machine. A bug you
  can re-send is a bug that stays fixed.
- **Sharing knowledge.** A collection in
  a repository is a new colleague's first
  hour with an API: clone it, run it,
  read real answers. No wiki page rots
  the way a folder of runnable requests
  doesn't.

## The rule, stated before everything else

An API client is a polite tool with an
impolite reach: it will send any request
you save, as often as you ask, to any
address you type. Saved collections make
that easier, not harder — a folder of
requests is a folder of buttons. So this
guide has one rule, and it is not fine
print:

> **Send requests only to APIs that are
> yours — on machines you own, or where
> the people who run the API have given
> you explicit permission.**

Exploring your own service: yes.
Practising against a server you started
for the purpose, as chapter 4 does: yes.
Checking an employer's internal API you
were given credentials for, within the
job you were given them for: that is the
permission you hold. Hammering a public
API to see how much it takes, replaying
someone else's saved requests against
their service, testing whether a token
you found still works: no. Some of that
is illegal in many places; all of it is
outside what this guide teaches. The lab
went further than most readers will need
to: its API, its client, and its one
invented secret all lived on a single
machine, and no request in this guide
ever left it.

Chapter 15 returns to the line with the
load-testing edge spelled out: a tool
that re-sends requests on a loop turns
"checking" into "flooding" at a setting's
distance, and the setting does not change
whose permission you need.

## A first taste

After installing (chapter 3), a first
request is one small file. This is the
whole of the lab's first one,
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

and one command runs it:

```bash
bru run "health check.bru" --env local
```

Check: the lab's run (transcript
`bruno-lab/transcripts/t02-first-run.txt`)
answers:

```text
health check (200 OK) - 23 ms
Assertions
   ✓ res.status: eq 200
   ✓ res.body.status: eq ok
```

The `{{host}}` placeholder is filled from
an **environment** — chapter 7 — so the
same file can aim at a practice server
today and a real one tomorrow. The two
lines under `assert` are checks the
runner performs on the response, and
chapter 9 takes them apart.

## Who it is for

The developer meeting an API for the
first time who wants answers they can
re-run. The tester who is tired of test
cases that live in a tool's private
database and die with the subscription.
The team member who believes the requests
a project depends on should be reviewed
like the code that depends on them. The
common thread is one person, their own
APIs, and a preference for files over
accounts.

## What it is not

Bruno is not a **proxy**: it sends the
requests you write, it does not watch
other programs' traffic (that is this
series' mitmproxy guide). It is not an
**API server** or a mock: it is a client,
and the thing answering it must exist —
chapter 4 builds a small one to practise
against. It is not a **load tester**:
chapter 15 explains why a runner that can
repeat requests is still the wrong
instrument, and a rude one, for finding
out how much traffic a service survives.
And it is not a vault: chapter 8 shows
the discipline that keeps secrets out of
the files, because a collection is meant
to be committed, and committed secrets
are the leak Bruno was built to prevent.
