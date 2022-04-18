FROM node:16-slim as base
FROM base as builder

ENV VOLTO_MAJOR=15
ENV VOLTO_MINOR=4
ENV VOLTO_PATCH=1
ENV VOLTO_PRERELEASE=
ENV VOLTO_VERSION=${VOLTO_MAJOR}.${VOLTO_MINOR}.${VOLTO_PATCH}${VOLTO_PRERELEASE}

RUN apt-get update \
    && buildDeps="python3 build-essential" \
    && apt-get install -y --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir build && chown -R node:node build \
    && npm install --no-audit --no-fund -g yo @plone/generator-volto

USER node
WORKDIR /build

# Generate new volto app
RUN yo @plone/volto \
    plone-frontend \
    --description "Plone frontend using Volto" \
    --addon "volto-slate:minimalDefault,simpleLink" \
    --addon "@eeacms/volto-accordion-block" \
    --addon "@kitconcept/volto-heading-block" \
    --addon "@kitconcept/volto-separator-block" \
    --skip-install \
    --skip-workspaces \
    --volto=${VOLTO_VERSION} \
    --no-interactive

COPY package.json plone-frontend/package.json

RUN cd plone-frontend \
    && yarn install \
    && yarn build

FROM base
LABEL maintainer="Plone Community <dev@plone.org>" \
      org.label-schema.name="plone-frontend" \
      org.label-schema.description="Plone frontend image" \
      org.label-schema.vendor="Plone Foundation" \
      org.label-schema.docker.cmd="docker run -d -p 3000:3000 plone/plone-frontend:15.2.0"

RUN apt-get update \
    && buildDeps="busybox" \
    && apt-get install -y --no-install-recommends $buildDeps \
    && busybox --install -s \
    && rm -rf /var/lib/apt/lists/*

USER node
COPY --from=builder /build/plone-frontend/ /app/

WORKDIR /app
EXPOSE 3000
CMD ["yarn", "start:prod"]