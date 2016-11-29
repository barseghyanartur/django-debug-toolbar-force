reset
./scripts/uninstall.sh
./scripts/install_django_1_10.sh
#python examples/simple/manage.py test debug_toolbar_force --settings=settings_django_1_10 --traceback -v 3
./runtests.py
