odn-demo-theme
-------

ODN theme for CKAN

Plugin for extending package extras view.

Installation
-------

To enable plugin, change property in your production.ini:
```
ckan.plugins = odn_demo_theme odn_demo_theme_ic odn_demo_theme_pc odn_package_extras

# version displayed in header and About page (current version)
ckan.odn_version = 1.0.2

# link to midpoint in the header: Tools > User management
ckan.user_management.url = https://host/midpoint

# link to midpoint in the header: Tools > Unified Views
odn.uv.url = http://host/unifiedviews
```

set in .ini:
* ckan.site_title = COMSODE - Open Data Node 
* ckan.site_logo = /base/images/odnlogo.png


Restart of apache AS is required: ``` service apache2 restart ```


Internationalization (i18n)
-------
CKAN supports internationalization through babel (```pip install babel```). This tool extracts the messages from source code and html files
and creates .pot file. Next using commands (step 2 or 3) it creates or updates .po files. The actual translation are in these .po files.

1. To extract new .pot file from sources
	```
	python setup.py extract_messages
	```
	
	This need to be done if there is no .pot file or there were some changes to messages in source code files or html files.

2. To generate .po for new localization (this example uses 'sk' localization)
	```
	python setup.py init_catalog --locale sk
	```

3. If only updating existing .po file (e.g. new messages were extracted through step 1)
	```
	python setup.py update_catalog --locale sk
	```

Licenses
-------

Dual licensing is used for ODN theme.
* Code unde [GNU Affero General Public License, Version 3.0](http://www.gnu.org/licenses/agpl-3.0.html) (see LICENSE.code)
* Artwork under [Create Commons Attribution-ShareAlike 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode) (see LICENSE.artwork)
