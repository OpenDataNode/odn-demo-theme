'''
Created on 11.9.2015

@author: mvi
'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class OdnDemoThemeICPlugin(plugins.SingletonPlugin):
    '''ODN theme plugin for Internal Catalog
    '''
    plugins.implements(plugins.IConfigurer)
    
    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates') # html (jinja2)
        toolkit.add_public_directory(config, 'public') # css and js
