# Recipes

Four jobs Bruno earns its keep on, each
small enough to do in one sitting and
each built from pieces the earlier
chapters verified. The APIs in every
recipe are yours (chapter 1's rule), and
the lab's bookshop stands in for them in
the examples.

## Meet an API you have just been handed

You have a base address and, perhaps, a
document you half trust. Start a
collection, put the address in an
environment as `host`, and write the one
request every API seems to have — a
health check, a root, a list of
something. Run it. Then grow the
collection one endpoint at a time, in the
order *you* need them, saving each
request the moment it first works and
adding a status assertion before you move
on. In an afternoon the collection *is*
your understanding of the API, executable
and diffable — and where the document
disagreed with the server, the saved
requests remember which one lied.

## Turn a bug report into a saved request

Someone — often you, last month — reports
that an endpoint misbehaves. The instinct
is to fix it; the discipline is to
capture it first. Reproduce the call as a
Bruno request, with the exact body the
report describes, and write the test that
asserts the *correct* behaviour. It will
fail — that red run is the bug, in a form
that cannot be argued with, attached to
the issue, runnable by whoever picks the
issue up. Fix the server; the same
request goes green; it then lives in the
collection forever as the regression
test. Chapter 10's deliberately wrong
test shows the mechanics; here the wrong
is the API's, and the test is the part
that was missing all along.

## A smoke test for your own service

Your service is deployed somewhere new
and you want one command that says "the
basics are alive" before anyone clicks
anything. Take the collection, add an
environment for the deployment (its
`host`, its secret declared the chapter 8
way), and let the folder's `seq` order
put the health check first and the
read-only requests after it. The smoke
test is chapter 11's command with that
environment's name, gateable on its exit
code. Keep it read-only: a smoke test
that places orders is a small incident
with good intentions, and write-then-read
journeys deserve their own collection and
their own chapter of caution.

## Pin the contract you depend on

Another team's API feeds your program,
and it changes without asking. The
requests your program depends on, saved
as a collection with assertions on the
fields you actually consume — not the
whole response, just your contract — are
an early-warning system that runs in CI
against *their* staging environment (with
their knowledge; chapter 1) and goes red
the week the field you need is renamed,
not the week your users notice. When it
fires, the failing assertion names the
field — which makes the conversation with
the other team short, specific, and
entirely free of blame.

## The common shape

Every recipe is the same three moves:
save the request the moment it teaches
you something, attach the check that
would catch the lesson being lost, and
keep both in the repository where they
can be reviewed like the knowledge they
are. Bruno's contribution is making those
moves cheap enough — a text file, a few
lines, one command — that they actually
get made.
