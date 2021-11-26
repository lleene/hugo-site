---
title: "Domain Setup ☄💻"
date: 2021-09-19T17:14:03+02:00
draft: false
---



## DNS Records

The main part of setting up a domain is configuring your
[DNS Records](https://en.wikipedia.org/wiki/List_of_DNS_record_types). This
basically dictates how your physical machine address is mapped to your human
readable service names. I mainly use this domain for web services together
self hosted email. As such I outlined the relevant records below that these
services require.

| Name                                            | Description
| ----------------------------------------------- | -----------------------  
| `A`       Address record                        | // physical IPv4 address associated with this domain 
| `CNAME`   Canonical name record                 | Alias name for A record name. This is generally for subdomains (i.e. other.domain.xyz as alias for domain.xyz both served the same machine)
| `CAA`     Certification Authority Authorization | DNS Certification Authority Authorization, constraining acceptable CAs for a host/domain.
| `DS`      Delegation signer                     | The record used to identify the DNSSEC signing key of a delegated zone
| `MX`      Mail exchange record                  | Maps a domain name to a list of message transfer agents for that domain
| `TXT`     Text record                           | Carries machine-readable data, such as specified by RFC 1464, opportunistic encryption, Sender Policy Framework, DKIM, DMARC, DNS-SD, etc.

The essential records for web services are the A and CNAME records which enable
correct name look up when outside you private network. Nowadays SSL should be
part and so specifying which certification authority you use should be set in
the CAA record. Most likely this will be `letsencrypt.org` which pretty much
provides SSL certificate signing free of charge securing your traffic to some
extent. In combination there should be a DS record here that presents your
public signing key used by your machine's SSL setup and allows you to
setup DNSSEC on your domain.

The other records are required for secure email transfer. First you need the
equivalent of a name record, the MX record which should point to another A
record and may or may not the same machine / physical address as the domain
hosting your web-services. Signing your email is similar to SSL encryption
should be an essential part of your setup. A SMTP set-up with postfix
can do so by using [openDKIM](http://www.opendkim.org/). This will require
you to similarly provide your public signing key as a TXT record.

```bash
"v=DKIM1;k=rsa;p=${key_part1}"
"${key_part2}"
```

The TXT record will look something like the above statement. There are some
inconveniences unfortunately when using RSA in combination with a high entropy
which yields a long public key. You need to break this key up into multiple
strings which the `openkdim` tool may or may not do by default as there is a
maximum character length for each TXT entry element. As long as no semi-colons
are inserted this should just work as expected.

### Debugging DNS Issues

Often is things don't go as expected. Especially with DNS related issues since
caching prevents real-time corrections.

```bash
nslookup leene.dev
dig $DOMAIN_NAME $RECORD_NAME
```

Two of the better tools here is nslookup and dig. The first will generally
tell you how and where you name lookup is being resolved. Sometimes this
may not be as expected so its always good to double check. The second is
literally a DNS utility that lets you query specific records. For example
testing your openDKIM setup relies on the DNS record correctly being set.
