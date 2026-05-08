{
    'name': 'Odoo Swagger Rest API',
    'version': '1.0.1',
    'category': 'Tools',
    'summary': 'Odoo Swagger & Lightweight Swagger interface & No Need Postman #CRUD Operations',
    'description': """
        <h3>Odoo Swagger - Res API</h3>
        <p>
            This is a comprehensive API testing tool for Odoo ERP system. Add your server URL, complete authorization, and quickly test all available modules including Contacts, Employees, CRM, Sales, Products, Invoices, Projects, and Tasks. Each module provides CRUD operations (Create, Read, Update, Delete) for easy integration testing.
        </p>
        <p>
            It also hosts a small web application for interacting with these endpoints
            from the browser without external tools.
        </p>
    """,
    'author': 'Envision Technolabs',
    'maintainer': 'Envision Technolabs',
    'website': 'https://www.envisiontechnolabs.com',
    'price': 10,
    'currency': 'USD',
   # 'license': 'LGPL-3',
    'license': 'OPL-1',
    'depends': ['base'],
    'data': [],
    # App Store requires image in static/description — not static/src
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
