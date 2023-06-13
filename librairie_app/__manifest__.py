# -*- coding: utf-8 -*-
{
    "name": "Librairie Management",
    "summary": "Manage library catalog and book lending.",
    "author": "Med Lehbib Youba",
    "license": "AGPL-3",
    "website": "https://github.com/PacktPublishing"
    "/Odoo-15-Development-Essentials",
    "version": "15.0.1.0.0",
    "depends": ["base"],
    "data": [
            "security/librairie_security.xml",
            "security/ir.model.access.csv",
            "views/book_view.xml",
            "views/librairie_menu.xml",
            "views/book_list_template.xml",
            ],
    "category": "Services/Librairie",
    "installable": True,
    "application": True,
}
