# Plone 6 demo

Repository used for local demos of Plone 6.

## Overview

This repo was created to support [Érico Andrei](https://github.com/ericof)'s "Welcome to Plone 6" presentation at [Python Web Conference 2022](https://2022.pythonwebconf.com/presentations/welcome-to-plone-6).

Currently it uses:

* Plone 6.0.0rc1
* Volto 16.0.0-alpha.52
* Volto Addons:

    * [@eeacms/volto-accordion-block](https://www.npmjs.com/package/@eeacms/volto-accordion-block)
    * [@kitconcept/volto-blocks-grid](https://www.npmjs.com/package/@kitconcept/volto-blocks-grid)
    * [@kitconcept/volto-button-block](https://www.npmjs.com/package/@kitconcept/volto-button-block)
    * [@kitconcept/volto-heading-block](https://www.npmjs.com/package/@kitconcept/volto-heading-block)
    * [@kitconcept/volto-separator-block](https://www.npmjs.com/package/@kitconcept/volto-separator-block)
    * [@kitconcept/volto-slider-block](https://www.npmjs.com/package/@kitconcept/volto-slider-block)
    * [volto-slate](https://www.npmjs.com/package/volto-slate)


## Usage

Clone this repository

```bash
git clone git@github.com:collective/plone6-local-demo.git
cd plone6-local-demo
make run
```

Then point your browser to: http://6.localhost or http://classic.localhost. (username and password: **admin**)

To clean up the images, use:


```bash
make stop
```

## Used for

* [Plone Symposium South America 2022](https://plone.org.br/eventos/2022/plone-symposium-south-america-2022)
* [Python Web Conference 2022](https://2022.pythonwebconf.com/presentations/welcome-to-plone-6)
* [Welcome to Plone 6](https://www.youtube.com/watch?v=16JZPRnkZ9w)
* [Live de Python](https://www.youtube.com/watch?v=CcYqwUfp6UQ)


## Special thanks

* [kitconcept GmbH](https://kitconcept.com): Created the example content used here.

* [T. Kim Nguyen](https://github.com/tkimnguyen): For pushing me to document stuff I do :-)
