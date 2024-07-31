from odoo import _, fields, models
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)



class G2PDocumentFile(models.Model):
    _inherit = "storage.file"
    
    def create(self, vals):
        _logger.info("Creating storage file with values: %s", vals)
        if isinstance(vals, dict):
            self._check_profile_tag(vals)
        elif isinstance(vals, list):
            for i in range(len(vals)):
                vals_obj = vals[i]
                self._check_profile_tag(vals_obj)

        return super().create(vals)

    def _check_profile_tag(self, vals_obj):
        _logger.info("Checking profile tag for values: %s", vals_obj)
        profile_tag = self.env["g2p.document.tag"].get_tag_by_name("Profile Image")
        profile_tag_id = profile_tag.id
        tags_ids = vals_obj.get("tags_ids", [])
        has_profile_tag = any(tag[1] == profile_tag_id for tag in tags_ids)

        if has_profile_tag:
            existing_file = self.search(
                [("registrant_id", "=", vals_obj.get("registrant_id")), ("tags_ids", "in", [profile_tag.id])],
                limit=1,
            )

            if existing_file:
                raise UserError(
                    _(
                        "Profile image already exists. To change your profile picture,"
                        "hover over your current image and click the edit button."
                    )
                )
