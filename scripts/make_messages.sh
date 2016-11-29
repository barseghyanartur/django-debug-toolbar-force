echo 'Making messages for django-debug-toolbar-force...'
cd src/debug_toolbar_force/
django-admin.py makemessages -l de
django-admin.py makemessages -l nl
django-admin.py makemessages -l ru

echo 'Making messages for example projects...'
cd ../../examples/simple/
django-admin.py makemessages -l de
django-admin.py makemessages -l nl
django-admin.py makemessages -l ru
