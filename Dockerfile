
FROM alpine

LABEL description="Hugo static build process."
LABEL maintainer="Lieuwe Leene <lieuwe@leene.dev>"

ENV HUGO_VERSION=0.105.0
ENV HUGO_ID=hugo_${HUGO_VERSION}
ENV BASE_URL="http://localhost/"

RUN wget -O - https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_ID}_Linux-64bit.tar.gz | tar -xz -C /tmp \
    && mkdir -p /usr/local/sbin \
    && mv /tmp/hugo /usr/local/sbin/hugo \
    && rm -rf /tmp/${HUGO_ID}_linux_amd64 \
    && rm -rf /tmp/LICENSE.md \
    && rm -rf /tmp/README.md

VOLUME /public

RUN apk add --update git asciidoctor libc6-compat libstdc++ \
    && apk upgrade \
    && apk add --no-cache ca-certificates \
    && git clone https://github.com/lleene/hugo-site.git /src \
    && git clone https://github.com/lleene/hermit.git /src/themes/hermit \
    && /usr/local/sbin/hugo -b ${BASE_URL} -s /src -d /public --minify
