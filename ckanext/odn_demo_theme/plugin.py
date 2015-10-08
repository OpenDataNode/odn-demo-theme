import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import ckan.lib.helpers as h
from ckan.common import c
from ckan.lib.app_globals import auto_update
from pylons import config
from ckan.model.user import User
import pylons

auto_update.append('ckan.odn_version')

def localized_url_for_static(link):
    return h.url_for_static("{lang}/{link}".format(lang=h.lang(), link=link))

def get_uv_url():
    return config.get('odn.uv.url', '')

def get_user_management_url():
    return config.get('ckan.user_management.url', '')

def user_display_name():
    logged_user = c.userobj
    actor_id = pylons.session.get('ckanext-cas-actorid')
    if actor_id:
        found_user = User.by_name(actor_id)
        if found_user:
            return u'{0} ({1})'.format(logged_user.display_name, found_user.display_name)
    return logged_user.display_name


class OdnDemoThemePlugin(plugins.SingletonPlugin):
    '''An comsode theme plugin.

    '''
    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)
    
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_public_directory(config, '../i18n')
    
    def get_helpers(self):
        return {'localized_url_for_static': localized_url_for_static,
                'get_uv_url': get_uv_url,
                'get_user_management_url': get_user_management_url,
                'user_display_name':user_display_name}

