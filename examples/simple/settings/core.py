import os

__all__ = (
    'project_dir',
    'gettext',
    'PROJECT_DIR',
    'show_toolbar',
)


def project_dir(base):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), base).replace('\\', '/')
    )


def gettext(s):
    return s


PROJECT_DIR = project_dir


def show_toolbar(request):
    """Determine whether to show the toolbar on a given page."""
    return True
