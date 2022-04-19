# Copyright (c) 2022, SDC and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import today

class DailyDiary(WebsiteGenerator):
	def before_save(self):
		self.date=today()
		self.username=frappe.db.get_value("User",{"name":frappe.session.user},"full_name")
	
