# Installer for weewx-wxgraphic
# Distributed under the terms of the GNU Public License (GPLv3)
# Copyright 2018 - 2020 by Glenn McKechnie
#
# https://github.com/glennmckechnie/weewx-wxgraphic

from setup import ExtensionInstaller
import random
import string


def loader():
    return WXgraphicInstaller()


class WXgraphicInstaller(ExtensionInstaller):
    def __init__(self):

        super(WXgraphicInstaller, self).__init__(
            version='0.6.3',
            name='wxgraphic',
            description='Weather Graphic image generator via a php'
                        ' script',
            author='anolecomputer, modified for weewx installation'
                   'by Glenn McKechnie',
            author_email="<glenn.mckechnie@gmail.com>",
            config={
                'StdReport': {
                    'WXgraphic': {
                        'HTML_ROOT': 'wxgraphic',
                        'skin': 'WXgraphic',
                        'enable': 'True'}}},
            files=[('skins/WXgraphic', [
                    'skins/WXgraphic/skin.conf',
                    'skins/WXgraphic/DATA/wxgraphic_weewx.txt.tmpl',
                    'skins/WXgraphic/avatar.gif',
                    'skins/WXgraphic/avatar.jpeg',
                    'skins/WXgraphic/avatar.png',
                    'skins/WXgraphic/banner_big.gif',
                    'skins/WXgraphic/banner_big.jpeg',
                    'skins/WXgraphic/banner_big.png',
                    'skins/WXgraphic/banner.gif',
                    'skins/WXgraphic/banner.jpeg',
                    'skins/WXgraphic/banner.png',
                    'skins/WXgraphic/config.txt',
                    'skins/WXgraphic/default.gif',
                    'skins/WXgraphic/default.jpeg',
                    'skins/WXgraphic/default.png',
                    'skins/WXgraphic/license.txt',
                    'skins/WXgraphic/PHP_verify.php',
                    'skins/WXgraphic/README.txt',
                    'skins/WXgraphic/index.php',
                    'skins/WXgraphic/wxgraphic.php',
                    'skins/WXgraphic/icons/day_clear.gif',
                    'skins/WXgraphic/icons/day_clear.jpeg',
                    'skins/WXgraphic/icons/day_clear.png',
                    'skins/WXgraphic/icons/day_cloudy.gif',
                    'skins/WXgraphic/icons/day_cloudy.jpeg',
                    'skins/WXgraphic/icons/day_cloudy.png',
                    'skins/WXgraphic/icons/day_heavy_rain.gif',
                    'skins/WXgraphic/icons/day_heavy_rain.jpeg',
                    'skins/WXgraphic/icons/day_heavy_rain.png',
                    'skins/WXgraphic/icons/day_light_rain.gif',
                    'skins/WXgraphic/icons/day_light_rain.jpeg',
                    'skins/WXgraphic/icons/day_light_rain.png',
                    'skins/WXgraphic/icons/day_mostly_sunny.gif',
                    'skins/WXgraphic/icons/day_mostly_sunny.jpeg',
                    'skins/WXgraphic/icons/day_mostly_sunny.png',
                    'skins/WXgraphic/icons/day_partly_cloudy.gif',
                    'skins/WXgraphic/icons/day_partly_cloudy.jpeg',
                    'skins/WXgraphic/icons/day_partly_cloudy.png',
                    'skins/WXgraphic/icons/day_rain.gif',
                    'skins/WXgraphic/icons/day_rain.jpeg',
                    'skins/WXgraphic/icons/day_rain.png',
                    'skins/WXgraphic/icons/day_sleet.gif',
                    'skins/WXgraphic/icons/day_sleet.jpeg',
                    'skins/WXgraphic/icons/day_sleet.png',
                    'skins/WXgraphic/icons/day_snow.gif',
                    'skins/WXgraphic/icons/day_snow.jpeg',
                    'skins/WXgraphic/icons/day_snow.png',
                    'skins/WXgraphic/icons/day_tstorm.gif',
                    'skins/WXgraphic/icons/day_tstorm.jpeg',
                    'skins/WXgraphic/icons/day_tstorm.png',
                    'skins/WXgraphic/icons/fog.gif',
                    'skins/WXgraphic/icons/fog.jpeg',
                    'skins/WXgraphic/icons/fog.png',
                    'skins/WXgraphic/icons/haze.gif',
                    'skins/WXgraphic/icons/haze.jpeg',
                    'skins/WXgraphic/icons/haze.png',
                    'skins/WXgraphic/icons/mist.gif',
                    'skins/WXgraphic/icons/mist.jpeg',
                    'skins/WXgraphic/icons/mist.png',
                    'skins/WXgraphic/icons/night_clear.gif',
                    'skins/WXgraphic/icons/night_clear.jpeg',
                    'skins/WXgraphic/icons/night_clear.png',
                    'skins/WXgraphic/icons/night_cloudy.gif',
                    'skins/WXgraphic/icons/night_cloudy.jpeg',
                    'skins/WXgraphic/icons/night_cloudy.png',
                    'skins/WXgraphic/icons/night_heavy_rain.gif',
                    'skins/WXgraphic/icons/night_heavy_rain.jpeg',
                    'skins/WXgraphic/icons/night_heavy_rain.png',
                    'skins/WXgraphic/icons/night_light_rain.gif',
                    'skins/WXgraphic/icons/night_light_rain.jpeg',
                    'skins/WXgraphic/icons/night_light_rain.png',
                    'skins/WXgraphic/icons/night_partly_cloudy.gif',
                    'skins/WXgraphic/icons/night_partly_cloudy.jpeg',
                    'skins/WXgraphic/icons/night_partly_cloudy.png',
                    'skins/WXgraphic/icons/night_rain.gif',
                    'skins/WXgraphic/icons/night_rain.jpeg',
                    'skins/WXgraphic/icons/night_rain.png',
                    'skins/WXgraphic/icons/night_sleet.gif',
                    'skins/WXgraphic/icons/night_sleet.jpeg',
                    'skins/WXgraphic/icons/night_sleet.png',
                    'skins/WXgraphic/icons/night_snow.gif',
                    'skins/WXgraphic/icons/night_snow.jpeg',
                    'skins/WXgraphic/icons/night_snow.png',
                    'skins/WXgraphic/icons/night_tstorm.gif',
                    'skins/WXgraphic/icons/night_tstorm.jpeg',
                    'skins/WXgraphic/icons/night_tstorm.png',
                    'skins/WXgraphic/icons/sleet.gif',
                    'skins/WXgraphic/icons/sleet.jpeg',
                    'skins/WXgraphic/icons/sleet.png',
                    'skins/WXgraphic/icons/tornado.gif',
                    'skins/WXgraphic/icons/tornado.jpeg',
                    'skins/WXgraphic/icons/tornado.png',
                    'skins/WXgraphic/icons/windy.gif',
                    'skins/WXgraphic/icons/windy.jpeg',
                    'skins/WXgraphic/icons/windy.png'])]
            )