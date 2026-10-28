# Assertions

A request you only send is a question.
A request with **assertions** is a
question with the answer checked.
Assertions are the lighter of Bruno's two
checking styles: one line each, no
programming, written in an `assert` block
inside the request file. This chapter
teaches the style from the lab's working
collection — every assertion quoted below
ran, and its tick or cross is in the
transcripts.

## The shape of a line

```bru
assert {
  res.status: eq 200
}
```

Each line names a **place** in the
response, a colon, and an **expectation**:
an operator and a value. `res.status` is
the response's status code; `eq` is the
operator; `200` is what it must equal.
The lab's health check carries two:

```bru
assert {
  res.status: eq 200
  res.body.status: eq ok
}
```

`res.body` is the response body, and
because the practice API answers JSON,
`res.body.status` walks into it — the
body's `status` field. Both lines passed
in transcript t02.

## Places in the body

Dotted paths reach as deep as the JSON
goes, and square brackets index into
lists. The catalogue request asserts all
three shapes (transcript t04):

```bru
assert {
  res.status: eq 200
  res.body: isArray
  res.body: length 3
  res.body[0].author: eq Ursula K. Le Guin
}
```

`isArray` is an expectation with no value
— the place must *be* an array. `length`
asks a place how long it is; applied to
the body itself, it counts the list's
items. `res.body[0].author` is the first
book's author. Note what the style is
good at: shape and spot values, stated so
plainly that a reader who has never seen
the API can check the claims against the
response by eye.

## Operators

The set is deliberately small: equality
and inequality (`eq`, `neq`), comparisons
(`gt`, `lt` and their or-equal kin),
`contains`, `matches` for patterns, type
tests like `isArray`, `isString`,
`isNumber`, `isBoolean`, and existence.
Chapter 10's tests exist for everything
beyond that set — arithmetic, logic
combining several facts, anything you
would need a semicolon to say.

## Reading a failure

A failed assertion prints the place, the
expectation, and the two values that
disagreed (transcript t03):

```text
   ✕ res.status: eq 200
      expected 401 to equal 200
```

That second line is the whole debugging
method: *expected* what the line claimed,
*wanted* what the file asked. When the
two differ, one of three things is true —
the API changed, the request went
somewhere else, or the file's claim was
never right — and chapter 10 shows a
failure of the third kind kept on
purpose, to make the reading practice
safe.

## The hyphen trap

Header names contain hyphens, and hyphens
break dotted paths. The lab's echo
request carries this assertion:

```bru
res.body.headers["X-Lab-Marker"]: eq sent-by-the-pre-request-script
```

The bracket form is not decoration. The
lab first wrote the natural dotted
version, `res.body.headers.X-Lab-Marker`,
and the assertion failed with an actual
value that was not a string at all but an
error object — the evaluator had tried to
read the path as arithmetic (something
minus `Lab` minus `Marker`) and reported
the wreckage (transcript t03, the third
failure in that run). The lesson is worth
the space: **when an assertion's "actual"
value looks like an error rather than
data, suspect the path before the API.**
Any key containing a character that is
not a letter, digit or underscore gets
brackets and quotes.

## Assertions or tests?

The boundary the lab settled on:
assertions for what a single line can say
about a single response — status, shape,
a field's value. The moment a check needs
a name a human will search for later, or
a second step, it graduates to chapter
10's tests. Neither is a lesser tool;
the summary in chapter 11 counts them in
separate columns because they fail
differently and mean different things
when they do.
