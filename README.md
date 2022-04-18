# Plone 6 demo

Repository used for local demos of Plone 6.

## Overview

This repo was created to support [Érico Andrei](https://github.com/ericof)'s "Welcome to Plone 6" presentation at [Python Web Conference 2022](https://2022.pythonwebconf.com/presentations/welcome-to-plone-6).

Currently it uses:

* Plone 6.0.0a4
* Volto 15.4.1
* Volto Addons:

    * volto-slate
    * @eeacms/volto-accordion-block
    * @kitconcept/volto-blocks-grid
    * @kitconcept/volto-heading-block
    * @kitconcept/volto-separator-block


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
make down
```

## Used for

* [Python Web Conference 2022](https://2022.pythonwebconf.com/presentations/welcome-to-plone-6)


## Special thanks

* [kitconcept GmbH](https://kitconcept.com): Create the example content used here.

* [T. Kim Nguyen](https://github.com/tkimnguyen): For pushing me to document stuff I do :-)
