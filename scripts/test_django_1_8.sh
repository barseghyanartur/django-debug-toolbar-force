reset
#./scripts/uninstall.sh
#./scripts/install_django_1_8.sh
#python examples/simple/manage.py test debug_toolbar_force --settings=settings.django_1_8 --traceback -v 3
python examples/simple/manage.py test debug_toolbar_force --settings=settings.testing --traceback -v 3
#./runtests.py
