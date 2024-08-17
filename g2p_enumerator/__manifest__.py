{
    "name": "G2P Enumerator",
    "category": "G2P",
    "version": "17.0.1.2.0-develop",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "depends": ["g2p_registry_group", "base"],
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/g2p_enumerator_view.xml",
        "views/group_view.xml",
        "views/registration_portal_view.xml",
    ],
    "assets": {
        "web.assets_frontend": [],
        "web.assets_common": [],
        "website.assets_wysiwyg": [],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
