# Part of Markdown Forever Add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file LICENSE for more details.
# Copyright 2019-2021 André-Abush Clause, Sof and other contributors. Released under GPL.
# <https://github.com/aaclause/nvda-markdownForever>

from html import escape as escapeHTML

from logHandler import log
import tones
import time
import core
import controlTypes
import api
import addonHandler
addonHandler.initTranslation()

lastSec = 0


def isVirtualDocument():
	obj = api.getReviewPosition().obj
	return hasattr(obj, "rootNVDAObject")


def getHTML(obj, previousTag=None, pre=True):
	global lastSec
	try:
		lastSec_ = int(time.strftime('%S'))
		if lastSec_ != lastSec and not (lastSec_ % 3):
			lastSec = lastSec_
			tones.beep(250, 42)
		if not obj:
			return ''
		out = []
		tag = None
		if hasattr(obj, "IA2Attributes") and "tag" in obj.IA2Attributes.keys():
			tag = obj.IA2Attributes["tag"]
		elif hasattr(obj, "HTMLNodeName"):
			tag = obj.HTMLNodeName.lower()
		if tag and pre:
			if tag == 'a':
				out.append('\n<a href="%s">' %
						   (obj.value.strip() if obj.value else '#'))
			else:
				out.append("\n<%s>" % tag)
		if pre:
			if controlTypes.STATE_CHECKED in obj.states:
				out.append("✓")
			elif controlTypes.STATE_CHECKABLE in obj.states:
				out.append("◻")
			if controlTypes.STATE_HALFCHECKED in obj.states:
				out.append("<->")
		if obj.children:
			for child in obj.children:
				try:
					out.append(getHTML(child, tag))
				except core.CallCancelled:
					out.append(getHTML(child, tag, pre=False))
		elif previousTag != "li" or (previousTag == "li" and obj.name not in ["• "]):
			if obj.name and (obj.parent.role != controlTypes.ROLE_LABEL or (obj.parent.role == controlTypes.ROLE_LABEL and obj.parent.name != obj.name)):
				out.append(obj.name)
		if obj.role == controlTypes.ROLE_EDITABLETEXT:
			out.append("………")
			if obj.value:
				beg = "<pre>" if controlTypes.STATE_MULTILINE in obj.states else '<code>'
				end = "</pre>" if controlTypes.STATE_MULTILINE in obj.states else '</code>'
				out.append(beg + escapeHTML(obj.value) + end)
		if tag:
			out.append("</%s>\n" % tag)
	except core.CallCancelled:
		log.debug("error!")
	return ''.join(out)


def getAllHTML():
	if not isVirtualDocument():
		return _("Invalid document"), True
	obj = api.getReviewPosition().obj
	return ''.join(getHTML(obj.rootNVDAObject)), False
