

API_HOSTS = {
    'test': "http://localhost:8080/wp-json/wc/v3/",
    'dev': "",
    'prod': "",
}

WOO_API_HOSTS = {
    'test': "http://localhost:8080",
    'dev': "",
    'prod': "",
}

DB_HOSTS = {
    'machine1': {
        'test': {
            'host': 'localhost',
            'database': 'wordpress',
            'table_prefix': 'wp_',
            'port': 3306,
        },
        'dev': {
            'host': 'host.docker.internal',
            'database': 'wordpress',
            'table_prefix': 'wp_',
            'port': 3306,
        },
        'prod': {
            'host': 'host.docker.internal',
            'database': 'wordpress',
            'table_prefix': 'wp_',
            'port': 3306,
        },
    },
    'docker': {
        'test': {
            'host': 'host.docker.internal',
            'database': 'wordpress',
            'table_prefix': 'wp_',
            'port': 3306,
        },
        'dev': {
            'host': 'host.docker.internal',
            'database': 'wordpress',
            'table_prefix': 'wp_',
            'port': 3306,
        },
        'prod': {
            'host': 'host.docker.internal',
            'database': 'wordpress',
            'table_prefix': 'wp_',
            'port': 3306,
        },
    },
    'machine2': {
        'test': {
            'host': 'localhost',
            'database': 'wordpress',
            'table_prefix': 'wp_',
            'port': 3306,
        },
        'dev': {
            'host': 'host.docker.internal',
            'database': 'wordpress',
            'table_prefix': 'wp_',
            'port': 3306,
        },
        'prod': {
            'host': 'host.docker.internal',
            'database': 'wordpress',
            'table_prefix': 'wp_',
            'port': 3306,
        },
    },

}