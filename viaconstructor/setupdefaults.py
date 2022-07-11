def setup_defaults(_) -> dict:
    return {
        "mill": {
            "rate_h": {
                "default": 1000,
                "type": "int",
                "min": 1,
                "max": 10000,
                "title": _("Feed-Rate(Horizontal)"),
                "tooltip": _("the Horizotal Feetrate"),
            },
            "rate_v": {
                "default": 100,
                "type": "int",
                "min": 1,
                "max": 10000,
                "title": _("Feed-Rate(Vertical)"),
                "tooltip": _("the Vertical Feetrate"),
            },
            "fast_move_z": {
                "default": 5.0,
                "type": "float",
                "min": 0.0,
                "max": 999.0,
                "title": _("Fast-Move Z"),
                "tooltip": _("the Z-Position for fast moves"),
            },
            "G64": {
                "default": 0.050000,
                "type": "float",
                "min": 0.0,
                "max": 0.1,
                "title": _("G64-Value"),
                "tooltip": _("value for the G64 command"),
            },
            "depth": {
                "default": -9.0,
                "type": "float",
                "min": -999.0,
                "max": 0.0,
                "per_object": True,
                "title": _("Depth"),
                "tooltip": _("the end depth for milling"),
            },
            "step": {
                "default": -9.0,
                "type": "float",
                "min": -999.0,
                "max": 0.0,
                "per_object": True,
                "title": _("Step"),
                "tooltip": _("the maximum depth in one move"),
            },
            "active": {
                "default": True,
                "type": "bool",
                "per_object": True,
                "title": _("Active"),
                "tooltip": _("enable/disable this object"),
            },
            "helix_mode": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Helix"),
                "tooltip": _("Helix"),
            },
            "reverse": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Reverse"),
                "tooltip": _("Reverse"),
            },
            "pocket": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Pocket"),
                "tooltip": _("do pocket operation on this object"),
            },
            "back_home": {
                "default": True,
                "type": "bool",
                "title": _("Back-Home"),
                "tooltip": _("move tool back to Zero-Possition after milling"),
            },
            "small_circles": {
                "default": False,
                "type": "bool",
                "title": _("Small-Circles"),
                "tooltip": _("milling small circles even if the tool is bigger"),
            },
            "overcut": {
                "default": False,
                "type": "bool",
                "title": _("Overcut"),
                "tooltip": _("Overcuting edges"),
            },
            "zero": {
                "default": "original",
                "type": "select",
                "options": (
                    ("original", _("original")),
                    ("bottomLeft", _("bottomLeft")),
                    ("center", _("center")),
                    ("bottomRight", _("bottomRight")),
                    ("topLeft", _("topLeft")),
                    ("topRight", _("topRight")),
                ),
                "title": _("Zero-Position"),
                "tooltip": _("setting the Zero-Postition of the Workpiece"),
            },
        },
        "tool": {
            "number": {
                "default": 1,
                "type": "int",
                "min": 1,
                "max": 99,
                "title": _("Number"),
                "tooltip": _("setting the Tool-Number to load in gcode"),
            },
            "diameter": {
                "default": 4.0,
                "type": "float",
                "min": 0.0,
                "max": 999.0,
                "title": _("Diameter"),
                "tooltip": _("setting the Tool-Diameter to calculate the Offsets"),
            },
            "speed": {
                "default": 10000,
                "type": "int",
                "min": 100,
                "max": 100000,
                "title": _("Speed"),
                "tooltip": _("setting the Tool-Speed in RPM"),
            },
        },
        "view": {
            "path": {
                "default": "simple",
                "type": "select",
                "options": (
                    ("minimal", _("minimal")),
                    ("simple", _("simple")),
                    ("full", _("full")),
                ),
                "title": _("Path"),
                "tooltip": _("how to show the gcode path in the 3d-View"),
            },
            "ruler_show": {
                "default": True,
                "type": "bool",
                "title": _("Ruler-Show"),
                "tooltip": _("showing ruler in 3D preview"),
            },
            "grid_show": {
                "default": True,
                "type": "bool",
                "title": _("Grid-Show"),
                "tooltip": _("showing grid in 3D preview"),
            },
            "grid_size": {
                "default": 10,
                "type": "int",
                "min": 1,
                "max": 1000,
                "title": _("Grid-Size"),
                "tooltip": _("size of the grid"),
            },
            "polygon_show": {
                "default": True,
                "type": "bool",
                "title": _("Show as Polygon"),
                "tooltip": _("showing as polygon in 3D preview"),
            },
        },
        "gcode": {
            "arc_r": {
                "default": False,
                "type": "bool",
                "title": _("Arc-R"),
                "tooltip": _("using radius for arc output instead of j/i"),
            },
        },
    }
