# dbgclient
`dbgclient` is a simple module that can help you to make bot HTTP API requests.
Currently support `GET and POST` method only, please pay attention currently this module is `pre-release` so is under development.
**GET and POST** I think enought to your build API bot.
In the future this module may can added some HTTP requests method like `PUT, PATCH, DELETE or CUSTOM` defined by your choice :) .
So you guys I hope you can enjoy by this first time release, some feature are described below

# Feature
- Indonesian Fake Data
- GET or POST support HTML Inspector by CSS Selector
- Storage Utils (append, write)

# Class Method
> DbgHttp and BaseClient

This method to make new client of http client request.
# Usage
```python
from dbgid import DbgHttp, BaseClient
#ClientBase Example
client = BaseClient('url here',verbose=False)
print(client._get({}))
"""Note BaseClient are same attribute with DbgHttp.
To call DbgHttp must use with, For BaseClient is not require with"""

with DbgHttp('url here',verbose=False) as client:
 #get method
 
 client._get(headers={'accept':'*/*})
 
 #post method support output json/html
 
 client._post({'accept':'*/*','content-type':'application/x-www-form-urlencoded'},{'body':'this is body string'},json=False)
 
 #get text element by css class, support span,p,div
 
 client._get_text_element_by_class('html content','span','class-text')
 
 #get input value by name
 
 client._get_input_value_by_name('html content','email')
 
 #get input value by id
 
 client._get_input_value_by_id('html content','email')
 
 #json post data
 
 client.__post_json({'accept':'application/json'},{'key':'value'})
```

> dbgStorage

This method for save data to local storage
# Usage
```python
from dbgid import dbgStorage

#save append file

dbgStorage.save('filename.txt','a','string to save')

#read file

dbgStorage.read('filename.txt')

#read as binary

dbgStorage.readBinary('filename.txt')

#read file each line

dbgStorage.readLine('filename.txt')

#read json file
dbgStorage.readJson('filename.json')
```

> dbgFaker

This method can generate indonesian data fake

# Usage

```python
from dbgid import dbgFaker

fake = dbgFaker()
print(fake.getData()) #return dict data
```

Insyallah in next update will rich feature added soon.
If you have bug issues don't hestitate to tell me guys