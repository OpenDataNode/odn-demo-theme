Internationalization i18n
-------

The localization files should be generated to this package. The steps are mentioned in the
main readme file. Each localization should have following hierarchy

```
i18n/{localization}/LC_MESSAGES/ckan.po
i18n/{localization}/base/images/image_name.jpg
```
The localization .po files are generated automatically.

For images, you need to add the base/images folder and add the image there. Then in the html file use:
```html
<img src="{{ h.localized_url_for_static('base/images/my_image.jpg') }}" onerror="this.src='{{ h.url_for_static('base/images/my_image.jpg') }}'"/>
```

The ``` h.localized_url_for_static('image_path') ``` will produce correct link to the localized img file. The ``` onerror ```
html attribute will make so if the localization doesn't have the image. it will display the image
from odn_demo_theme/public/image_path