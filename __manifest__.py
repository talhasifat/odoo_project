{
    'name': 'School Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage student information',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/students_views.xml',
        'views/teacher_views.xml',
        'views/student_report.xml',
        # 'views/reports.xml',
        'views/dashboard_view.xml',

        'views/configuration_views.xml',
        'views/teacher_report.xml',
        'views/menu.xml',

    ],

'assets': {
    'web.assets_backend': [
        'student_information/static/src/js/dashboard.js',
        'student_information/static/src/xml/dashboard_template.xml',
    ],
},

    'installable': True,
    'application': True,
}
