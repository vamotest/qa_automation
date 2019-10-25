### How to use:

* Необходимо скачать образ [Selenium Grid Extras](https://github.com/groupon/Selenium-Grid-Extras/releases/download/v2.0.4/SeleniumGridExtras-2.0.4-SNAPSHOT-jar-with-dependencies.jar) и запустить его в роли `hub`
```sh
mkdir hub && cd hub && wget -O hub.jar https://github.com/groupon/Selenium-Grid-Extras/releases/download/v2.0.4/SeleniumGridExtras-2.0.4-SNAPSHOT-jar-with-dependencies.jar && java -jar hub.jar  && cd ..
```
* Необходимо скачать образ [Selenium Grid Extras](https://github.com/groupon/Selenium-Grid-Extras/releases/download/v2.0.4/SeleniumGridExtras-2.0.4-SNAPSHOT-jar-with-dependencies.jar) и запустить его в роли `node`
```sh
mkdir node_local && cd node_local && wget -O node_local.jar https://github.com/groupon/Selenium-Grid-Extras/releases/download/v2.0.4/SeleniumGridExtras-2.0.4-SNAPSHOT-jar-with-dependencies.jar && java -jar node_local.jar  && cd ..
```
* Во время настройки необходимо задать IP-адрес Selenium Grid Hub. Также указываем, что данная `node_local` не будет использовать `Firefox`/`Chrome`.
```
What is the HOST for the Selenium Grid Hub?
Default Value: 127.0.0.1
IP-address
'IP-address' was set as your value
```
```
Will this node run 'Firefox' (1-yes/0-no)
Default Value: 0
0
'0' was set as your value

Will this node run 'Chrome' (1-yes/0-no)
Default Value: 0
0
'0' was set as your value
```
* На удаленной системе необходимо скачать образ [Selenium Grid Extras](https://github.com/groupon/Selenium-Grid-Extras/releases/download/v2.0.4/SeleniumGridExtras-2.0.4-SNAPSHOT-jar-with-dependencies.jar) и запустить его в роли `node`
```sh
mkdir node_remote && cd node_remote && wget -O node_remote.jar https://github.com/groupon/Selenium-Grid-Extras/releases/download/v2.0.4/SeleniumGridExtras-2.0.4-SNAPSHOT-jar-with-dependencies.jar && java -jar node_remote.jar  && cd ..
```
* Во время настройки необходимо задать IP-адрес Selenium Grid Hub. Также указываем, что данная `node_remote` будет использовать `Firefox`/`Chrome`.
```
What is the HOST for the Selenium Grid Hub?
Default Value: 127.0.0.1
IP-adress
'IP-adress' was set as your value
```
```
Will this node run 'Firefox' (1-yes/0-no)
Default Value: 0
1
'1' was set as your value

What version of 'Firefox' is installed?
Default Value: 69

'69' was set as your value
```
```
Will this node run 'Chrome' (1-yes/0-no)
Default Value: 0
1
'1' was set as your value

What version of 'Chrome' is installed?
Default Value: 78
78
'78' was set as your value
```
* На удаленной системе должен быть установлен [ChromeDriver 78.0.3904.70](https://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.70/) и [Geckodriver 0.26](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0)