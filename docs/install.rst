============
Installation
============

.. note::
    After following this instruction Django JET dashboard won't be active (as it is located into
    a separate application). If you want to make it work, you will have to enable dashboard application
    by following :doc:`install_dashboard` steps too.

* Download and install latest version of Django JET:

.. code:: python

    pip install django-jet2
    # or
    easy_install django-jet2

* Add 'jet' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'django.contrib.admin'):

.. code:: python

    INSTALLED_APPS = (
        ...
        'jet',
        'django.contrib.admin',
        ...
    )

* Make sure ``django.template.context_processors.request`` context processor is enabled in settings.py:

.. code:: python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.request',
                    ...
                ],
            },
        },
    ]

* Add URL-pattern to the urlpatterns of your Django project urls.py file (they are needed for related–lookups and autocompletes):

.. code:: python

    urlpatterns = patterns(
        '',
        path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
        path('admin/', include(admin.site.urls)),
        ...
    )

* Create database tables:

.. code:: python

    python manage.py migrate jet

* Collect static if you are in production environment:

.. code:: python

    python manage.py collectstatic

* Clear your browser cache
