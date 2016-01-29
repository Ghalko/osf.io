# -*- coding: utf-8 -*-
from nose.tools import *  # noqa (PEP8 asserts)

from tests.base import OsfTestCase
from website.addons.dropbox.tests.factories import (
    DropboxUserSettingsFactory,
    DropboxNodeSettingsFactory,
    DropboxAccountFactory
)
from website.addons.dropbox.model import DropboxNodeSettings
from website.addons.base import testing

class TestNodeSettings(testing.models.OAuthAddonNodeSettingsTestSuiteMixin, OsfTestCase):

    short_name = 'dropbox'
    full_name = 'dropbox'
    ExternalAccountFactory = DropboxAccountFactory

    NodeSettingsFactory = DropboxNodeSettingsFactory
    NodeSettingsClass = DropboxNodeSettings
    UserSettingsFactory = DropboxUserSettingsFactory

    def _node_settings_class_kwargs(self, node, user_settings):
        return {
            'user_settings': self.user_settings,
            'folder': '1234567890',
            'owner': self.node
        }

    def test_folder_defaults_to_none(self):
        node_settings = DropboxNodeSettings(user_settings=self.user_settings)
        node_settings.save()
        assert_is_none(node_settings.folder)

class TestUserSettings(testing.models.OAuthAddonUserSettingTestSuiteMixin, OsfTestCase):

    short_name = 'dropbox'
    full_name = 'dropbox'
    ExternalAccountFactory = DropboxAccountFactory
