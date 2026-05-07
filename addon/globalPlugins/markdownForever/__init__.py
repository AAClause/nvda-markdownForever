# Part of Markdown Forever Add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file LICENSE for more details.
# Copyright 2019-2022 André-Abush Clause, Sof and other contributors. Released under GPL.
# <https://github.com/aaclause/nvda-markdownForever>

import codecs
import json
import os
import os.path
import re
import sys

import gui
import wx

import addonHandler
import api
import config
import globalPluginHandler
import languageHandler
import scriptHandler
import ui
from logHandler import log

from . import updatecheck
from .common import (
	convertToHTML, convertToMD, copyToClipAsHTML,
	getText, extractMetadata, getMetadataAndTextForMarkDown,
	addonSummary, addonVersion,
	addonPath, baseDir, configDir,
	defaultLanguage,
	migrate_legacy_markdown_extensions_config,
)

addonHandler.initTranslation()

addonDir = os.path.join(os.path.dirname(__file__), "..", "..")
addonUpdateChannel = addonHandler.Addon(addonDir).manifest["updateChannel"]
confSpecs = {
	"autoCheckUpdate": "boolean(default=True)",
	"lastNVDAVersion": 'string(default="unknown")',
	"updateChannel": f'option("dev", "stable", default={addonUpdateChannel})',
	"lastCheckUpdate": "float(min=0, default=0)",
	"toc": 'boolean(default=False)',
	"toc-back": 'string(default="")',
	"autonumber-headings": 'boolean(default=False)',
	"extratags": 'boolean(default=True)',
	"extratags-back": 'boolean(default=True)',
	"detectExtratags": 'boolean(default=True)',
	"genMetadata": 'boolean(default=True)',
	"IM_defaultAction": 'integer(min=0, max=4, default=0)',
	"defaultPath": r'string(default="%USERPROFILE%\documents")',
	"defaultFileName": 'string(default="")',
	"markdownEngine": 'option("html2markdown", "html2text", default="html2text")',
	"HTMLTemplate": 'string(default="default")',
	"markdownExtensions": 'string(default="break-on-newline,fenced-code-blocks,footnotes,header-ids,strike,tables,task_list")',
	"markdown2Extras": 'string(default="")',
	"HTMLTemplates": {},
	"HTTPServer": {
		"host": 'string(default="127.0.0.1")',
		"port": "integer(min=1, max=65535, default=8794)",
		"defaultEncoding": 'string(default="UTF-8")',
		"rootDirs": {}
	}
}
config.conf.spec["markdownForever"] = confSpecs
migrate_legacy_markdown_extensions_config()

if not os.path.exists(configDir):
	os.mkdir(configDir)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = addonSummary

	def __init__(self):
		self.createMenu()
		self.updatecheckThread = updatecheck.UpdateCheck()
		self.updatecheckThread.start()
		if not self.updatecheckThread.is_alive():
			log.error("Update check system not started")
		super().__init__()

	def createMenu(self):
		self.submenu = wx.Menu()
		documentationsMenu = wx.Menu()
		self.submenu.AppendSubMenu(documentationsMenu, _("Documentation"), _("Documentation submenu"))
		langs = self.getDocumentationLanguages()
		for lang, langDesc in langs.items():
			item = documentationsMenu.Append(wx.ID_ANY, langDesc, _(
				"Open the add-on documentation in this language."))
			gui.mainFrame.sysTrayIcon.Bind(
				wx.EVT_MENU, lambda evt, lang=lang: self.onDoc(evt, lang), item)
		item = self.submenu.Append(wx.ID_ANY, "%s..." %
								   _("Settings"), _("Add-on settings"))
		gui.mainFrame.sysTrayIcon.Bind(
			wx.EVT_MENU,
			lambda event: wx.CallAfter(gui.mainFrame._popupSettingsDialog, self._get_settings_dialog()),
			item
		)
		item = self.submenu.Append(
			wx.ID_ANY, _("&HTTP server"), _("Start HTTP server"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onHTTPServer, item)
		item = self.submenu.Append(wx.ID_ANY, "%s..." % _(
			"&Check for update"), _("Checks if update is available"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onUpdate, item)
		item = self.submenu.Append(wx.ID_ANY, _(
			"&Web site"), _("Open the GitHub Repository"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onWebsite, item)
		self.submenu_item = gui.mainFrame.sysTrayIcon.menu.InsertMenu(
			2, wx.ID_ANY, "%s (%s)" % (_("&Markdown Forever"), addonVersion), self.submenu)

	def getDocumentationLanguages(self):
		langs = {}
		docDir = os.path.join(baseDir, "..", "..", "doc", "")
		ls = os.listdir(docDir)
		for f in ls:
			if os.path.isfile(os.path.join(docDir, f)) and f.lower().endswith(".md"):
				lang = f.replace(".md", '')
				langDesc = languageHandler.getLanguageDescription(lang)
				if langDesc:
					langs[lang] = langDesc
		return langs

	def removeMenu(self):
		gui.mainFrame.sysTrayIcon.menu.DestroyItem(self.submenu_item)

	def terminate(self):
		self._get_http_server().stop()
		self.removeMenu()
		self.updatecheckThread.stop()
		self.updatecheckThread.join()
		if self.updatecheckThread.is_alive():
			log.debug("Update check system stopped")
		super().terminate()

	@staticmethod
	def onHTTPServer(evt):
		http_server = GlobalPlugin._get_http_server()
		if not http_server.isRun():
			http_server.run()
		host = config.conf["markdownForever"]["HTTPServer"]["host"]
		port = config.conf["markdownForever"]["HTTPServer"]["port"]
		os.startfile(f"http://{host}:{port}/")

	@staticmethod
	def _get_settings_dialog():
		from . import settings
		return settings.AddonSettingsDialog

	@staticmethod
	def _get_http_server():
		from . import HTTPServer
		return HTTPServer

	@staticmethod
	def onDoc(evt, lang=defaultLanguage.split('_')[0]):
		MDLocation = os.path.join(addonPath, "doc", lang + ".md")
		if not os.path.exists(MDLocation):
			MDLocation = os.path.join(addonPath, "doc", "en"+".md")
		f = codecs.open(MDLocation, "rb")
		raw = f.read()
		if raw.startswith(codecs.BOM_UTF8):
			raw = raw[3:]
		metadata, text = extractMetadata(raw.decode("UTF-8"))
		HTMLLocation = MDLocation.replace(".md", ".html")
		convertToHTML(
			text, metadata,
			save=True,
			src=False, useTemplateHTML=True,
			display=True, fp=HTMLLocation
		)

	@staticmethod
	def onUpdate(evt):
		return updatecheck.checkUpdates()

	@staticmethod
	def onWebsite(evt):
		return os.startfile("https://github.com/aaclause/nvda-markdownForever")

	def script_md2htmlSrcInNVDA(self, gesture):
		text, err = getText()
		if err:
			return ui.message(err)
		if not text:
			return ui.message(_("No text"))
		metadata, text = extractMetadata(text)
		convertToHTML(text, metadata, save=False,
					  src=True, useTemplateHTML=False)
	script_md2htmlSrcInNVDA.__doc__ = _("Show the HTML source from Markdown")

	def script_html2md(self, gesture):
		metadata, text = getMetadataAndTextForMarkDown()
		if not text:
			return ui.message(_("No text"))
		if metadata:
			convertToMD(text, metadata)
	script_html2md.__doc__ = _("HTML to Markdown conversion")

	def extractMetadata(self, text):
		return extractMetadata(text)

	def convertToMD(self, text, metadata):
		return convertToMD(text, metadata)

	def script_md2htmlInNVDA(self, gesture):
		text, err = getText()
		if err:
			return ui.message(err)
		if not text:
			return ui.message(_("No text"))
		metadata, text = extractMetadata(text)
		convertToHTML(text, metadata)
	script_md2htmlInNVDA.__doc__ = _("Markdown to HTML conversion. The result is displayed in a virtual buffer of NVDA")

	def script_md2htmlInBrowser(self, gesture):
		text, err = getText()
		if err:
			return ui.message(err)
		if not text:
			return ui.message(_("No text"))
		metadata, text = extractMetadata(text)
		convertToHTML(text, metadata, save=True)
	script_md2htmlInBrowser.__doc__ = _("Markdown to HTML conversion. The result is displayed in your default browser")

	def script_copyHTMLSrcToClip(self, gesture):
		text, err = getText()
		if err:
			return ui.message(err)
		if not text:
			return ui.message(_("No text"))
		metadata, text = extractMetadata(text)
		api.copyToClip(convertToHTML(text, metadata, src=True,
									 display=False, useTemplateHTML=False))
		ui.message(_("HTML source copied to clipboard"))
	script_copyHTMLSrcToClip.__doc__ = _("Markdown to HTML source conversion. The result is copied to clipboard")

	def script_copyFormattedHTMLToClip(self, gesture):
		text, err = getText()
		if err:
			return ui.message(err)
		if not text:
			return ui.message(_("No text"))
		metadata, text = extractMetadata(text)
		if copyToClipAsHTML(convertToHTML(text, metadata, src=True, display=False, save=False)):
			return ui.message(_("Formatted HTML copied to clipboard"))
		else:
			ui.message(_("An error occured"))
	script_copyFormattedHTMLToClip.__doc__ = _(
		"Markdown to formatted HTML conversion. The result is copied to clipboard")

	def script_copyMarkdownToClip(self, gesture):
		metadata, text = getMetadataAndTextForMarkDown()
		if not metadata:
			return
		if not text:
			return ui.message(_("No text"))
		res = convertToMD(text, metadata, display=False)
		if res:
			api.copyToClip(res)
			ui.message(_("Markdown copied to clipboard"))
		else:
			ui.message(_("An error occured"))
	script_copyMarkdownToClip.__doc__ = _(
		"HTML to Markdown conversion. The result is copied to clipboard")

	def script_interactiveMode(self, gesture):
		text, err = getText()
		if err:
			return ui.message(err)
		from . import interactivemode
		gui.mainFrame._popupSettingsDialog(interactivemode.InteractiveModeDlg, text=text)
	script_interactiveMode.__doc__ = _("Interactive mode")

	__gestures = {
		"kb:nvda+alt+b": "md2htmlInBrowser",
		"kb:nvda+alt+n": "md2htmlInNVDA",
		"kb:nvda+alt+k": "html2md",
		"kb:nvda+alt+l": "md2htmlSrcInNVDA",
		"kb:nvda+Control+h": "copyHTMLSrcToClip",
		"kb:nvda+shift+h": "copyFormattedHTMLToClip",
		"kb:nvda+shift+g": "copyMarkdownToClip",
		"kb:nvda+Control+i": "interactiveMode",
	}


