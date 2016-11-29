import base64
import tempfile

from PIL import Image
from six import BytesIO

__title__ = 'debug_toolbar_force.tests.factories.files'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2016 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'BASE64_PREFIX',
    'TEMPORARY_FILE_LIST',
    'TEMPORARY_FILE_LIST_FILE_CONTENT',
    'TEMPORARY_FILE_LIST_FILE_BASE64',
    'TEMPORARY_FILE_VIEW',
    'TEMPORARY_FILE_VIEW_FILE_CONTENT',
    'TEMPORARY_FILE_VIEW_FILE_BASE64',
    'TEMPORARY_FILE_ADD',
    'TEMPORARY_FILE_ADD_FILE_CONTENT',
    'TEMPORARY_FILE_ADD_FILE_BASE64',
    'TEMPORARY_FILE_CHANGE',
    'TEMPORARY_FILE_CHANGE_FILE_CONTENT',
    'TEMPORARY_FILE_CHANGE_FILE_BASE64',
    'TEMPORARY_FILE_CHANGE_CHANGED',
    'TEMPORARY_FILE_CHANGE_CHANGED_FILE_CONTENT',
    'TEMPORARY_FILE_CHANGE_CHANGED_FILE_BASE64',
    'TEMPORARY_FILE_DELETE',
    'TEMPORARY_FILE_DELETE_FILE_CONTENT',
    'TEMPORARY_FILE_DELETE_FILE_BASE64',
)


def get_temporary_file(prefix):
    """Get a temporary file.

    :return:
    """
    image = Image.new('RGBA', size=(100, 100), color=(256, 0, 0))
    tmp_file = BytesIO()
    _tmp_file = tempfile.NamedTemporaryFile(prefix=prefix, suffix='.png')
    image.save(tmp_file, "PNG")
    tmp_file.seek(0)
    tmp_file.name = _tmp_file.name
    return tmp_file


BASE64_PREFIX = 'data:image/png;base64,'

TEMPORARY_FILE_LIST = get_temporary_file(prefix='LIST')
TEMPORARY_FILE_LIST_FILE_CONTENT = TEMPORARY_FILE_LIST.read()
TEMPORARY_FILE_LIST_FILE_BASE64 = BASE64_PREFIX + base64.b64encode(
    TEMPORARY_FILE_LIST_FILE_CONTENT
).decode()
TEMPORARY_FILE_LIST.seek(0)

TEMPORARY_FILE_VIEW = get_temporary_file(prefix='VIEW')
TEMPORARY_FILE_VIEW_FILE_CONTENT = TEMPORARY_FILE_VIEW.read()
TEMPORARY_FILE_VIEW_FILE_BASE64 = BASE64_PREFIX + base64.b64encode(
    TEMPORARY_FILE_VIEW_FILE_CONTENT
).decode()
TEMPORARY_FILE_VIEW.seek(0)

TEMPORARY_FILE_ADD = get_temporary_file(prefix='ADD')
TEMPORARY_FILE_ADD_FILE_CONTENT = TEMPORARY_FILE_ADD.read()
TEMPORARY_FILE_ADD_FILE_BASE64 = BASE64_PREFIX + base64.b64encode(
    TEMPORARY_FILE_ADD_FILE_CONTENT
).decode()
TEMPORARY_FILE_ADD.seek(0)

TEMPORARY_FILE_CHANGE = get_temporary_file(prefix='CHANGE')
TEMPORARY_FILE_CHANGE_FILE_CONTENT = TEMPORARY_FILE_CHANGE.read()
TEMPORARY_FILE_CHANGE_FILE_BASE64 = BASE64_PREFIX + base64.b64encode(
    TEMPORARY_FILE_CHANGE_FILE_CONTENT
).decode()
TEMPORARY_FILE_CHANGE.seek(0)

TEMPORARY_FILE_CHANGE_CHANGED = get_temporary_file(prefix='CHANGE_CHANGED')
TEMPORARY_FILE_CHANGE_CHANGED_FILE_CONTENT = \
    TEMPORARY_FILE_CHANGE_CHANGED.read()
TEMPORARY_FILE_CHANGE_CHANGED_FILE_BASE64 = BASE64_PREFIX + base64.b64encode(
    TEMPORARY_FILE_CHANGE_CHANGED_FILE_CONTENT
).decode()
TEMPORARY_FILE_CHANGE_CHANGED.seek(0)

TEMPORARY_FILE_DELETE = get_temporary_file(prefix='DELETE')
TEMPORARY_FILE_DELETE_FILE_CONTENT = TEMPORARY_FILE_DELETE.read()
TEMPORARY_FILE_DELETE_FILE_BASE64 = BASE64_PREFIX + base64.b64encode(
    TEMPORARY_FILE_DELETE_FILE_CONTENT
).decode()
TEMPORARY_FILE_DELETE.seek(0)
