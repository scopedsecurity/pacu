#!/usr/bin/env python
""" configure_settings.copy_settings_template_into_settings_file_if_not_present
is run automatically at pacu.py execution, if no settings file is found. """
import os


def copy_settings_template_into_settings_file_if_not_present() -> None:
    directory = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(directory + '/settings.py'):
        print('\nsettings.py file not found. Creating one from settings_template.py')
        with open(directory + '/settings_template.py', 'r') as settings_template:
            with open(directory + '/settings.py', 'w+') as settings_file:
                settings_file.write(settings_template.read())
        print('  Settings file created.\n')


# This removes the need to call the function in the middle of pacu.py's imports
copy_settings_template_into_settings_file_if_not_present()
