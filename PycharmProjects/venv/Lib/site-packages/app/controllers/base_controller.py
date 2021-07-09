from cement.core.controller import CementBaseController, expose
from distutils.dir_util import copy_tree
from app.services.dados_service import get_random_words
from os import path

class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Random word generator'
        arguments = [
            (['-f', '--files'], {
                'action': 'store',
                'dest': 'files',
                'help': 'word files',
                'required': False
            }),
            (['-c', '--category'], {
                'action': 'store',
                'dest': 'category',
                'help': 'word file',
                'required': False
            }),
            (['-n', '--number'], {
                'action': 'store',
                'dest': 'number',
                'help': 'number of random words',
                'required': False
            })
        ]

    @expose(hide=True)
    def default(self):
        pargs = self.app.pargs
        files = pargs.files
        if not files:
            files = path.join(path.expanduser('~'), '.dados')
            if not path.exists(files):
                copy_tree(path.abspath(path.join(path.dirname(path.realpath(__file__)), '..', 'dados')), files)
        category = pargs.category
        number = pargs.number
        if number:
            number = int(number)
        else:
            number = 1
        random_words = get_random_words(files, category=category, count=number)
        print('\n'.join(random_words))
