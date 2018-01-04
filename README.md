# Spaming-Phishers
Send fake datas to phishers

This script send fake datas (identity, mail address, passwords, credit cards ...) to phishing pages in order to flood the phisher with false informations. The purpose is to avoid the phisher to sell phished infos where legit datas could be included.

This script send
* fake useragent
* fake IP using TOR
* fake datas

In the example provided (a real case scenario on an OVH phishing), the target page is flooded with:
* fake french firstname using prenomfr.txt
* fake french name using nomfr.txt
* fake CC number using fakecc.txt
* fake CC month validity
* fake CC year validity
* fake CCV

Dictionary files are not provided.
