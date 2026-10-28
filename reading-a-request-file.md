# Reading a Request File

A `.bru` file is a stack of **blocks**.
Each block is a name, an opening brace,
lines of content, and a closing brace.
The order of blocks in the file does not
matter much to Bruno; the order in this
chapter is the order worth reading them
in. Everything below is from the lab's
own collection, which sits in
`bruno-lab/collection/bookshop-api/` for
you to open alongside.

## meta — the label

```bru
meta {
  name: Place an Order
  type: http
  seq: 4
}
```

`name` is what reports call the request —
it need not match the file name, though
the lab keeps them twins. `type: http`
says what kind of request this is.
`seq` is the running order when a folder
runs: chapter 11's run obeyed these
numbers, which is how the health check
can promise to go first.

## The request block — method as the name

The request block is named for its
method: `get { ... }`, `post { ... }`,
and the rest of HTTP's verbs each have
their block. Inside, three lines do most
of the work:

```bru
post {
  url: {{host}}/orders
  body: json
  auth: none
}
```

`url` is the address, placeholders and
all. `body` names the *kind* of body
(`none`, `json`, `text`, `xml`, form
variants) — the body itself lives in its
own block, next. `auth` names the
authentication scheme, whose details
likewise get their own block when there
are any (chapter 8's bearer token).

## body — what you send

```bru
body:json {
  {
    "bookId": 2,
    "quantity": 3
  }
}
```

The lab's order, from
`place an order.bru`. Notice the shape:
the JSON sits inside the block as itself,
not escaped into a string. That
readability is the format's argument in
one image — the request you review in a
diff is the request that will be sent,
with nothing encoded between you and it.

## headers — the named lines

```bru
headers {
  X-Lab-Marker: {{marker}}
}
```

One header per line, name and value,
values free to use placeholders. Chapter
10's script sets `{{marker}}` just before
this request is sent, and chapter 4's
`/echo` endpoint exists to prove the
header arrived with the value the script
gave it.

## Query strings and paths

Nothing in the format separates the
address's parts: a query string is simply
written into the `url` line
(`{{host}}/echo?source=bruno-lab`), and a
path parameter is just the path
(`{{host}}/books/2`). What you write is
what is sent; the echo endpoint's report
in chapter 10 shows the query arriving
intact.

## The checking blocks

Three blocks attach verdicts to a
request, and each gets a chapter:
`assert { ... }` (chapter 9) holds
one-line checks; `tests { ... }`
(chapter 10) holds JavaScript with names;
`script:pre-request { ... }` and its
post-response sibling hold JavaScript
that runs around the sending. A `docs`
block, when present, holds prose about
the request, written for the humans the
collection is shared with.

## What a file is not

Two absences are worth naming. There is
no place in a request file for a
**response**: responses are what runs
produce, kept in reports (chapter 11),
not in the collection. And there is no
place for a secret's **value**: the
format gives secrets a declaration and
withholds the value on purpose, which is
chapter 8's whole subject. A request file
is the part of your API knowledge that is
safe to show anyone — the format is
designed so that it stays that way.
