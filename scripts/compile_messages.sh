echo 'Compiling messages for django-debug-toolbar-force...'
cd src/debug_toolbar_force/
django-admin.py compilemessages -l de
django-admin.py compilemessages -l nl
django-admin.py compilemessages -l ru

echo 'Compiling messages for example projects...'
cd ../../examples/simple/
django-admin.py compilemessages -l de
django-admin.py compilemessages -l nl
django-admin.py compilemessages -l ru