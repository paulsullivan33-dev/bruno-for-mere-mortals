# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's traffic is the lab talking to itself.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 15 names what the tool
   cannot do: a desktop application this guide could not open
   and therefore teaches only from its documentation, a young
   file grammar that still moves between versions, ground that
   thins beyond HTTP and JSON, repetition that is not load
   testing, reports that record requests as sent (credentials
   included), sharing that stops at the repository's edge, and
   the legal edge around testing anything that is not yours.
8. **The ethics rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *your APIs, your machines,
   or explicit permission* — before any procedure depends on
   it, and later chapters point back to it where the tooling
   would make crossing the line easy.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is an Ubuntu 24.04 sandbox with Python
3.12.3 and Node.js 24.22.1 already present. Bruno CLI
**4.3.0** (the npm package `@usebruno/cli`) was installed
with npm, with npm's prefix and cache pointed into the lab's
scratch folder so the machine's global state never changed,
and exercised against a fixture API written for this guide
(`bruno-lab/server/fixture_api.py`, Python standard library
only), running on loopback only. The lab's collection is
`bruno-lab/collection/bookshop-api/`; all transcripts live in
`bruno-lab/transcripts/`.

Run for real, with transcripts as evidence:

- Install of `@usebruno/cli` and its version, 4.3.0 (t00).
- The fixture API proven on its own with curl before Bruno
  entered the story: health, catalogue, a deliberate 404 with
  headers, `/whoami` refusing a missing token (t01).
- A first request written by hand and run: assertions passing,
  exit code 0 (t02).
- A six-request collection (health, list, one item, an order
  POST with a JSON body, a bearer-auth request, an echo
  request with a pre-request script) run as a folder: order
  by `seq`, 4/4 tests and 11/11 assertions passing, exit
  code 0, with the secret's value supplied by `--env-var`
  (t04).
- The same run with the secret declared but no value
  supplied: the request is sent anyway, the server answers
  401, and the assertions fail with both values named (t03).
- The two secret traps, both fallen into and then fixed for
  real: the current grammar's `vars:secret [ ... ]` array
  against the older block form, whose parse error is kept
  verbatim (t90); and the `.env` file, which does not feed a
  plain `{{name}}` variable (t05) but does feed
  `{{process.env.NAME}}` (t05b).
- The hyphen trap in assertion paths, found in a real failing
  run (the evaluator reporting a ReferenceError object) and
  fixed with bracket syntax, re-run green (t03, t04).
- A deliberately wrong test — a stock count of five claimed
  against a fixture holding seven — failing with both
  numbers printed and exit code 1 (t07).
- The JSON report of a full run, read back and inspected:
  the request as actually sent, the response, and each
  assertion's verdict (t08).
- A run with the server stopped (`connect ECONNREFUSED`,
  exit code 1) and a run naming an environment that does
  not exist (one-line error, nothing sent) (t09).
- The collection committed to a real git repository:
  nine tracked text files, the `.env` excluded by the
  collection's own `.gitignore`, and `git grep` proving no
  tracked file contains the token's value (t06).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- The desktop application: its windows, editors, and its
  local, encrypted store for secret values. The sandbox has
  no desktop; every hands-on claim in this guide is about
  the CLI and the file format, and chapters say so wherever
  the app appears.
- Collection and folder variables, and post-response
  variable chaining between requests (chapter 7 and 10
  describe them; the lab's collection runs without them).
- The paid editions' external secret managers (HashiCorp
  Vault, AWS Secrets Manager, Azure Key Vault) and team
  workspace features.
- GraphQL requests, OAuth helper flows, and imports from
  Postman or OpenAPI descriptions.
- The comparison tools in chapter 12 are characterised, not
  benchmarked.

Fixtures are this guide's own and deliberately generic: the
stock room of an invented bookshop with a handful of
endpoints, a three-book catalogue, and one invented token
(`lab-token-123`) that guards a fiction and unlocks nothing
anywhere else. No example is modelled on any real person,
network, service or organisation, and no request in the lab
ever left the machine it was written on.
