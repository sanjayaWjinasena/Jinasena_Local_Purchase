# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : SubModule : Purchase : Local Purchase',
    'version': '17.0.1.0.2',
    'summary': 'Bug fixes for the Local Purchase (Credit) workflow',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Purchases',
    'license': 'LGPL-3',
    # bugfix_purchase already moves the "Update PR" step into
    # button_confirm (v0.7) and hides the manual Update PR button via
    # _get_view. But the Studio inherit on purchase.order.form still
    # gates button_confirm with x_studio_pr_update==True AND
    # x_studio_receive_status=='Pending', so the button never appears
    # in the first place. This module supplies the missing view-inherit
    # that drops those two now-redundant clauses.
    'depends': ['base_setup', 'purchase', 'BugFix-Purchase'],
    'data': [
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
