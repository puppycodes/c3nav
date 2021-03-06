import numpy as np
from django.conf import settings
from django.utils.functional import cached_property

from c3nav.routing.connection import GraphConnection


class GraphPoint():
    def __init__(self, x, y, room):
        self.x = x
        self.y = y
        self.room = room
        self.xy = np.array((x, y))
        self.i = None

        self.connections = {}
        self.connections_in = {}

    @cached_property
    def level(self):
        return self.room and self.room.level

    def serialize(self):
        return (
            self.x,
            self.y,
            None if self.room is None else self.room.i,
        )

    @cached_property
    def ellipse_bbox(self):
        x = self.x * settings.RENDER_SCALE
        y = self.y * settings.RENDER_SCALE
        return ((x-5, y-5), (x+5, y+5))

    def connect_to(self, other_point, ctype='', distance=None):
        connection = GraphConnection(self, other_point, ctype=ctype, distance=distance)
        self.connections[other_point] = connection
        other_point.connections_in[self] = connection

    @cached_property
    def arealocations(self):
        return tuple(name for name, points_i in self.level.arealocation_points.items() if self.i in points_i)

    def __repr__(self):
        return '<GraphPoint x=%f y=%f room=%s>' % (self.x, self.y, (id(self.room) if self.room else None))
