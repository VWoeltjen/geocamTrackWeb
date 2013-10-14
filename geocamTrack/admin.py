# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

from django.contrib import admin

# pylint: disable=W0401

from geocamTrack.models import *
from geocamTrack import settings

admin.site.register(Resource)
admin.site.register(IconStyle)
admin.site.register(LineStyle)
admin.site.register(Track)
admin.site.register(ResourcePosition)
admin.site.register(PastResourcePosition)
