# The Neighbours

Bruno is one answer to "how do I talk to
an API by hand, and keep what I learn?"
Several neighbours answer it differently,
and an honest map helps you choose per
job rather than per habit. The neighbours
are characterised from their documented
behaviour, not benchmarked; the lab ran
Bruno only.

## Postman

The incumbent, and the tool Bruno's
design is a reply to. Postman is a
capable, polished client whose
collections live in its own cloud
workspaces, tied to accounts; sharing
means inviting people into that
workspace, and the canonical form of a
collection is Postman's, not a folder
you own. For teams already living there,
its collaboration, mock servers and
monitoring are real advantages. The trade
is exactly chapter 1's: your requests are
data inside someone else's system,
exportable but not natively files, and
the diff-and-review life of chapter 12 is
not available in the same way. Bruno
imports Postman collections, which makes
the experiment cheap to try.

## Insomnia

Kong's client, the other well-known
name: a clean desktop app, collections
in its own storage (with a git-sync
option in its model), a plug-in
ecosystem. Closer to Bruno in spirit than
Postman — it is a tool, not a platform
pitch — but its sync story still leans on
its own machinery, and its headless story
(`inso`) is a separate tool to learn.
Bruno's bet is that plain files plus the
git you already have beat both.

## curl and HTTPie

The command line's own clients — this
series has a curl guide, and chapter 1 of
it will feel familiar. `curl` is
everywhere, scriptable, and answers one
request at a time with total honesty; it
keeps nothing, checks nothing, and its
long commands live in shell history,
which is where API explorations go to be
forgotten. HTTPie dresses the same job in
friendlier syntax and readable output.
Bruno is what happens when those one-off
commands deserve to be kept: the request
file is a curl command that learned to
file itself, carry its own checks, and
run with its siblings. Nothing stops you
using both — curl for the question of
the moment, Bruno for the questions you
will ask again.

## Stoplight, Swagger UI and friends

The documentation wing of the
neighbourhood: tools that render an
**OpenAPI** description as browsable,
try-it-out documentation. They answer
"what does this API claim to offer?" from
the API's own description of itself.
Bruno answers "what does it do?" from
evidence. The two are complements —
Bruno can import an OpenAPI description
to seed a collection, and a collection's
saved behaviour is the check on the
description's honesty — and confusing
them is the common error: a beautiful
documentation page is a claim, and a
passing run is a measurement.

## Your language's test suite

The neighbour inside your own house:
requests written as tests in the server's
own language and framework. Those tests
can reach things no client can — the
database, the internals — and they belong
in every project. What they cannot do is
see the API as an outsider sees it, from
the far side of the network, in the form
a real client meets. A Bruno collection
in the repository is the outsider's
suite, and the two check each other's
blind spots.
