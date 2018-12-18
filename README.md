Amnesia
========

Amnesia is a command line tool to clean an AskOmics instance.

The script remove all users files (uploaded files, ttl and results)

- Remove users files (uploaded files, ttl and results)
- Delete rdf graphs
- Empty job and integration database

The purpose of this program is to be executed at regular intervals in order to clean an AskOmics testing instance.

## Install & run

```bash
git clone https://github.com/askomics/amnesia.git
cd amnesia
python3 -m venv venv
source venv/bin/activate
python setup.py install
amnesia --help
```
