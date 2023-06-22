{
    "name": "Library Members",
    "license": "AGPL-3",
    "description": "Manage members borrowing books.",
    "author": "Daniel Reis",
    "depends": ["librairie_app", "mail"],
    "application": False,
     "data": [
        #"security/library_security.xml",
        #"security/ir.model.access.csv",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/member_view.xml",
        "views/library_menu.xml",
        #"views/member_view.xml",
        #"views/library_menu.xml",
        "views/book_list_template.xml",
    ],
}