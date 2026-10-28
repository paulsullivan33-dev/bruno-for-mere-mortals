# Installing Bruno

Bruno installs two ways, matching its two
faces: a **desktop application** from the
project's download page or your system's
package manager, and a **command line
runner** from npm. This guide's lab
verified the command line route end to
end; the desktop route is the project's
documented one and is described, not
demonstrated, here — the lab's machine
had no desktop to install it on.

## The CLI, with npm

The runner is the npm package
`@usebruno/cli`, so it needs **Node.js**
(the project's documentation asks for a
current LTS release; the lab used Node
24, which its machine already carried).
Installing globally puts `bru` on your
path:

```bash
npm install -g @usebruno/cli
bru --version
```

The lab did the same install with npm's
prefix and cache pointed at a scratch
folder, so the machine itself stayed
untouched — the package, the version and
the behaviour are identical either way,
and the scratch detail is in the lab
notes, not a step you need. One trap the
lab avoided on purpose: do not install
into a Python virtual environment or any
other tool's private folder. npm packages
live where npm puts them; give the CLI
its own place.

Check: the lab's install and version
(transcript
`bruno-lab/transcripts/t00-install-and-version.txt`)
read:

```text
$ npm ls -g @usebruno/cli
/home/.../npm-prefix/lib
`-- @usebruno/cli@4.3.0

$ bru --version
4.3.0
```

(The path is the lab's scratch prefix;
yours will be npm's usual global folder.)

The version matters when you read advice:
Bruno is young and moves quickly, formats
and flags shift between releases, and
this guide's transcripts are all from
**4.3.0**. One shift the lab ran into
head-first — an older secret-declaring
syntax the current CLI refuses to parse —
is shown in full in chapter 8, and it is
the general lesson: when a file that
"used to work" fails, check the version
before you check your typing.

## The desktop app

The app is a free download from the
project's website for Windows, macOS and
Linux, and common package managers carry
it as well (Homebrew's `bruno` cask,
Chocolatey, the Arch repositories, and
others). Installing it gives you the
window described in chapter 2 and nothing
else changes: it opens the same
collection folders, writes the same
`.bru` files, and can be installed
alongside the CLI, each ignoring the
other. *Documented-only in this guide:*
the lab never opened it, so no chapter
will tell you which menu a button lives
in — the file format the app edits, which
is where mistakes and knowledge both
live, is covered completely.

## What an install does not do

Neither face asks you to create an
account, sign in, or connect anything to
a cloud — a deliberate contrast with the
incumbent API clients, and worth
verifying for yourself on first run:
install, disconnect if you like, and
everything in chapters 5 to 11 still
works. Nor does the CLI keep state
between runs beyond what the collection's
files say; a run reads the folder fresh,
which is why chapter 12's git discipline
works at all.

## First commands

```bash
bru --version          # the runner answers
bru run --help         # every flag, from the tool itself
```

`bru run --help` is worth a slow read
before chapter 11: the flags for
environments, reports and exit behaviour
are all there, in the tool's own words,
and they are the version you actually
have — unlike any tutorial, including,
eventually, this one.
