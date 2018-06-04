# dashboarder

A super-simple app designed to make getting dashboard screens working a bit
easier and more flexible.

## Overview

Usually, when we want to get dashboard screens up and running we have either
some client side scripts or plugins to rotate through tabs or load up different
browser windows.

If we want to add / remove urls we usually have to interact on the display /
client side. This is fine with a single screen but what if you have multiple
dashboard screens in different locations? It becomes an annoyance.

`dashboarder` is a flask app that reads in a list of urls (currently from a YAML
file) and returns a `302` redirect with a Location header to a url from your
configuration. This means you can setup Chrome plugin like the
[Rotisserie URL Rotator plugin](https://chrome.google.com/webstore/detail/rotisserie-url-rotator/iljemanjjfjlglhkmojkmfbpphiaheja?hl=en)
to point at a single URL (dashboarder) and refresh periodically to change what
is displayed.

Currently, there's two rotation options:

Round-robin ordering (default):
```
timbirk at C02T8D59GTFL in ~
$ while true ; do date ; curl -s -I localhost:5000 | grep Location ; sleep 15 ; done
Mon Jun  4 11:47:59 BST 2018
Location: https://logs.infraprd.talpay.itvcloud.zone/goto/9ab9d95645762c526a1065b3c5c51a03
Mon Jun  4 11:48:14 BST 2018
Location: https://ci.infradev.talpay.itvcloud.zone/view/Talpay/
Mon Jun  4 11:48:29 BST 2018
Location: https://status.infraprd.talpay.itvcloud.zone/#/events
Mon Jun  4 11:48:44 BST 2018
Location: https://dashboard.infradev.talpay.itvcloud.zone/talpay
Mon Jun  4 11:48:59 BST 2018
Location: https://logs.infraprd.talpay.itvcloud.zone/goto/9ab9d95645762c526a1065b3c5c51a03
```

Random ordering:
```
timbirk at C02T8D59GTFL in ~
$ while true ; do date ; curl -s -I localhost:5000 | grep Location ; sleep 15 ; done
Mon Jun  4 11:50:13 BST 2018
Location: https://ci.infradev.talpay.itvcloud.zone/view/Talpay/
Mon Jun  4 11:50:28 BST 2018
Location: https://logs.infraprd.talpay.itvcloud.zone/goto/9ab9d95645762c526a1065b3c5c51a03
Mon Jun  4 11:50:43 BST 2018
Location: https://status.infraprd.talpay.itvcloud.zone/#/events
Mon Jun  4 11:50:58 BST 2018
Location: https://dashboard.infradev.talpay.itvcloud.zone/talpay
Mon Jun  4 11:51:13 BST 2018
Location: https://ci.infradev.talpay.itvcloud.zone/view/Talpay/
Mon Jun  4 11:51:28 BST 2018
Location: https://logs.infraprd.talpay.itvcloud.zone/goto/9ab9d95645762c526a1065b3c5c51a03
Mon Jun  4 11:51:43 BST 2018
Location: https://dashboard.infradev.talpay.itvcloud.zone/talpay
```

# Running

# Developing

# Future Features
