from django.urls import path

from backtesting.handlers import delete_back_testing_data

urlpatterns = [
    path(
        'delete-backtestings',
        delete_back_testing_data,
        name='delete-backtestings',
    ),
]