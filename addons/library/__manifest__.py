{
    "name": "Library",
    "summary": "Módulo pare gestionar la organización y alquiler de libros.",
    "description": """Módulo para gestionar:
        - Clientes
        - Libros
    """,
    "license": "OPL-1",
    "author": "SantiagoGutierrezHernandez",
    "website": "https://github.com/SantiagoGutierrezHernandez/curso-odoo-libreria",
    "category": "Custom Modules/Library",
    "depends": ["base"],
    "data": [
        "security/library_groups.xml",
        "security/ir.model.access.csv",
        "views/book_list_action.xml",
        "views/book_menuitem.xml",
    ],
    "demo": [
        "demo/book_demo.xml"
    ],
    "application": True,
}