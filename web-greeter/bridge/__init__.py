#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  __init__.py
#
#  Copyright © 2017 Antergos
#
#  This file is part of Web Greeter.
#
#  Web Greeter is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  Web Greeter is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  The following additional terms are in effect as per Section 7 of the license:
#
#  The preservation of all legal notices and author attributions in
#  the material or in the Appropriate Legal Notices displayed
#  by works containing it is required.
#
#  You should have received a copy of the GNU General Public License
#  along with Web Greeter; If not, see <http://www.gnu.org/licenses/>.


def language_to_dict(lang):
    return dict(code=lang.get_code(), name=lang.get_name(), territory=lang.get_territory())


def layout_to_dict(layout):
    return dict(
        description=layout.get_description(),
        name=layout.get_name(),
        short_description=layout.get_short_description()
    )


def session_to_dict(session):
    return dict(
        comment=session.get_comment(),
        key=session.get_key(),
        name=session.get_name(),
        type=session.get_session_type(),
    )


def user_to_dict(user):
    return dict(
        display_name=user.get_display_name(),
        home_directory=user.get_home_directory(),
        image=user.get_image(),
        language=user.get_language(),
        layout=user.get_layout(),
        logged_in=user.get_logged_in(),
        session=user.get_session(),
        username=user.get_name(),
        # ---->>> BEGIN DEPRECATED! <<<----
        name=user.get_name(),
        real_name=user.get_real_name(),
        # ---->>> END DEPRECATED! <<<----
    )


from .Greeter import Greeter
from .Config import Config
from .ThemeUtils import ThemeUtils
