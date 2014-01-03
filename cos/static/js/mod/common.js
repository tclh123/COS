require.config(
    {
        baseUrl: '/static/js/',
        paths: {
            jquery: 'lib/jquery.min',
            bootstrap: 'lib/bootstrap',
        },
        shim: {
            'bootstrap': {
                deps: ['jquery']
            }
        }
    });
