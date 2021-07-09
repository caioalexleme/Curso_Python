from cement.core.controller import CementBaseController, expose
from app.services.dados_service import get_categories

class ListController(CementBaseController):
    class Meta:
        label = 'list'
        description = 'list categories'
        stacked_on = 'base'
        stacked_type = 'nested'
        arguments = [
            (['-f', '--files'], {
                'action': 'store',
                'dest': 'files',
                'help': 'word files',
                'required': False
            })
        ]

    @expose(hide=True)
    def default(self):
        pargs = self.app.pargs
        files = pargs.files
        categories = get_categories(files)
        print('\n'.join(categories))
