from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.safe_eval import safe_eval
from datetime import date, datetime, timedelta
import logging

_logger = logging.getLogger(__name__)


class PandJProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.onchange('product_generic_id','product_item_type_id','product_brand_id','size','length','width','height','thickness',
                  'size_uom','length_uom','width_uom','height_uom','thickness_uom')
    def onchange_product_name(self):
        generic = (self.product_generic_id.name+": ") if self.product_generic_id else ""
        item_type = (self.product_item_type_id.name+": ") if self.product_item_type_id else ""
        brand = (self.product_brand_id.name+": ") if self.product_brand_id else ""
        size = (str(self.size) + self.size_uom.name+" ") if (self.size and self.size_uom) else ""
        length = ("L:" + str(self.length) + self.length_uom.name+" ") if (self.length and self.length_uom) else ""
        width = ("W:" + str(self.width) + self.width_uom.name+" ") if (self.width and self.width_uom) else ""
        height = ("H:" + str(self.height) + self.height_uom.name+" ") if (self.height and self.height_uom) else ""
        thickness = (str(self.thickness) + self.thickness_uom.name + " thick") if (self.thickness and self.thickness_uom) else ""
        if (generic or brand or size or length or width or height or thickness) != "":
            self.name = generic + item_type + brand + size + length + width + height + thickness
        else:
            self.name = ""
