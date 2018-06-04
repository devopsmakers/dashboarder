# dashboarder
A really simple dashboard rotator helper web app.


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
