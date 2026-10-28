# Tests and Scripts

Assertions (chapter 9) check a response
one line at a time. **Tests** are the
other half of the checking story: small
JavaScript programs inside the request
file that can reason — compare two
fields, do arithmetic, loop — and that
carry **names**, so a failure report
reads like a sentence instead of a
coordinate. **Scripts** are JavaScript
that runs around the request rather than
judging it: before it is sent, or after
the response lands. This chapter runs
both, and keeps one genuine failure under
glass.

## A test block

From the lab's `get one book.bru`
(transcript t04, both passing):

```bru
tests {
  test("status is 200", function() {
    expect(res.getStatus()).to.equal(200);
  });

  test("the book is A Wizard of Earthsea", function() {
    const body = res.getBody();
    expect(body.title).to.equal("A Wizard of Earthsea");
    expect(body.inStock).to.be.above(0);
  });
}
```

The shape is `test("a name", function()
{ ... })`. Inside, `res` is the response:
`res.getStatus()` its code, `res.getBody()`
its parsed body. `expect(...)` opens a
claim, and the claim is finished with a
matcher — `to.equal`, `to.be.above`, and
a family of kin borrowed from the Chai
assertion library, which Bruno's
documentation names as its model. Names
are not decoration: they are what the
report prints, and what a colleague will
search the file for in six months.

The order request shows tests doing what
assertions cannot: reaching *into* the
echo of a sent body and checking the
reply against the sending
(`body.received.quantity` equals the 3
the file sent) — a round trip verified,
not a value assumed.

## A failure, kept

The lab also wrote a test that is wrong
on purpose — it claims the stock count is
five, when the fixture holds seven — and
ran it in a scratch copy of the
collection. The output (transcript t07):

```text
get one book (200 OK) - 21 ms
Tests
   ✕ the stock count is five
      expected 7 to equal 5
   ✓ the book is A Wizard of Earthsea
```

Three things to learn from two lines.
The request itself *succeeded* (200 OK):
a failed test is not a failed request,
and Bruno reports them separately. The
message gives the two numbers in the
assertion style — expected the real 7,
wanted the claimed 5 — so the wrongness
is located in the test, not the API.
And the run's summary counts the damage
precisely (`Tests 1/2`, status FAIL, exit
code 1): a wrong test is a failing
suite, which is exactly the treatment
that keeps suites honest. Write your
tests so that this output would make
sense to you at 3 a.m.; the name is the
part you will read first.

## Scripts before the request

A **pre-request script** runs before the
request is sent, in a block named
`script:pre-request`. The lab's echo
request uses one to stamp itself:

```bru
script:pre-request {
  bru.setVar("marker", "sent-by-the-pre-request-script");
}

headers {
  X-Lab-Marker: {{marker}}
}
```

`bru` is the script's handle on Bruno
itself: setting variables, reading them,
reading environment values
(`bru.getEnvVar`, `bru.getProcessEnv`),
and more the documentation enumerates.
The proof that the machinery works is
not the script but chapter 4's `/echo`
endpoint, which reported the header
arriving with exactly the value the
script set — asserted, in the same file,
with chapter 9's bracket syntax
(transcript t04).

Scripts also run **after** the response
(`script:post-response`) — the natural
home for extracting a value from one
response (a token, an id) into a variable
the next request in a folder run will
use. That chaining pattern is how
multi-step journeys are built in Bruno;
the lab's collection does not need it,
and it is described here rather than
demonstrated, because a chain is only as
honest as its links and the lab kept
every link it shows.

## The sandbox

Scripts are code, and a collection you
clone from anywhere is code you are about
to run. Bruno runs scripts in a
**sandbox**: by default a restricted one
(the CLI calls it `safe`), with a
`developer` sandbox — permitting modules
and wider access — available behind
`--sandbox developer` at run time or a
collection setting. The default is the
right default. Chapter 15 returns to
this: treat a stranger's collection the
way you would a stranger's script,
because that is precisely what it is.
