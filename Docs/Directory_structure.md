# Directory Structure

/static/styles -> all stylesheets, js and images. Within HTML files to link to a stylesheet:     

```html
<link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='styles/style.css') }}">
```
/templates -> all html files. <br>

/database -> any code related to the database. <br>

/app -> point of entry to the app, all requests go through here. <br>