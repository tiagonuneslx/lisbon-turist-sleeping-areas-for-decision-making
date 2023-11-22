#!/bin/bash

files=$(ls -1 dist)

cp index.html dist/index.html

html_content="<ul id=\"files\">"

for file in $files; do
    html_content+="\n            <li><a href=\"$file\">$file</a><i class=\"fas fa-chevron-right icon\"></i></li>"
done

html_content+="\n        </ul>"

echo $html_content

perl -0777 -i -pe 's|<ul id="files">.*?</ul>|'"$html_content"'|s' dist/index.html

