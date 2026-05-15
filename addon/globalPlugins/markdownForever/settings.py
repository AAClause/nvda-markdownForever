# Part of Markdown Forever Add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file LICENSE for more details.
# Copyright 2019-2021 André-Abush Clause, Sof and other contributors. Released under GPL.
# <https://github.com/aaclause/nvda-markdownForever>

import json
import os
import random
import re
import gui
import wx

import addonHandler
import config

from . import HTTPServer
from .common import (addonSummary, configDir,
	IM_actionLabels, IM_actions,
	markdownEngines, markdownEngineLabels,
	EXTRAS, getMarkdownExtensions, getMarkdownExtensionsFromIndexes,
	getHTMLTemplates, getHTMLTemplate,
	getDefaultHTMLTemplateID, getHTMLTemplateFromID,
	clearHTMLTemplateCache,
	realpath, minCharTemplateName, maxCharTemplateName,
	translate_back_toc)

addonHandler.initTranslation()

class GeneralDlg(gui.settingsDialogs.SettingsPanel):
	title = _("General")
	updateChannels = ["stable", "dev"]

	def makeSettings(self, settingsSizer):
		sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		bHelper = gui.guiHelper.ButtonHelper(orientation=wx.HORIZONTAL)

		# Translators: label of a dialog.
		choices = [
			_("stable channel, automatic check"),
			_("dev channel, automatic check"),
			_("stable channel, manual check"),
			_("dev channel, manual check"),
		]
		self.updateCheck = sHelper.addLabeledControl(_("Check for &updates:"), wx.Choice, choices=choices)
		if config.conf["markdownForever"]["updateChannel"] in self.updateChannels:
			itemToSelect = self.updateChannels.index(config.conf["markdownForever"]["updateChannel"])
		else:
			itemToSelect = self.updateChannels.index("stable")
		if not config.conf["markdownForever"]["autoCheckUpdate"]: itemToSelect += len(self.updateChannels)
		self.updateCheck.SetSelection(itemToSelect)


		tableOfContentsText = _("&Generate a table of contents")
		markdownEngine = config.conf["markdownForever"]["markdownEngine"]
		self.tableOfContentsCheckBox = sHelper.addItem(
			wx.CheckBox(self, label=tableOfContentsText))
		self.tableOfContentsCheckBox.SetValue(config.conf["markdownForever"]["toc"])

		tableOfContentsBackText = _('Choose where add "Bac&k to Table of Contents" links')
		choices = []
		for i in range(1, 7):
			choices.append(_("Before level %d headings") % i)
			choices.append(_("After level %d headings") % i)
		self.tableOfContentsBackList = sHelper.addLabeledControl(tableOfContentsBackText, gui.nvdaControls.CustomCheckListBox, choices=choices)
		checked_items = translate_back_toc(config.conf["markdownForever"]["toc-back"], True)
		self.tableOfContentsBackList.CheckedItems = checked_items

		numberHeadingsText = _("Try to automatically &number headings")
		self.numberHeadingsCheckBox = sHelper.addItem(
			wx.CheckBox(self, label=numberHeadingsText))
		self.numberHeadingsCheckBox.SetValue(
			config.conf["markdownForever"]["autonumber-headings"])

		extratagsText = _("Enable e&xtra tags")
		self.extratagsCheckBox = sHelper.addItem(
			wx.CheckBox(self, label=extratagsText))
		self.extratagsCheckBox.SetValue(
			config.conf["markdownForever"]["extratags"])

		genMetadataText = _(
			"Generate corresponding &metadata from HTML source")
		self.genMetadataCheckBox = sHelper.addItem(
			wx.CheckBox(self, label=genMetadataText))
		self.genMetadataCheckBox.SetValue(
			config.conf["markdownForever"]["genMetadata"])

		defaultActionIMText = _("Default &action in interactive mode:")
		self.defaultActionListBox = sHelper.addLabeledControl(
			defaultActionIMText, wx.Choice, choices=IM_actionLabels)
		self.defaultActionListBox.SetSelection(list(IM_actions.values()).index(
			config.conf["markdownForever"]["IM_defaultAction"]))
		idEngine = markdownEngines.index(markdownEngine)
		markdownEngineText = _("Markdown Engi&ne:")
		self.markdownEngineListBox = sHelper.addLabeledControl(
			markdownEngineText, wx.Choice, choices=markdownEngineLabels)
		self.markdownEngineListBox.SetSelection(idEngine)
		label = _("Markdo&wn extensions:")
		choices = [f"{k}. {v}" for k, v in EXTRAS.items()]
		self.markdownExtensions = sHelper.addLabeledControl(
			label, gui.nvdaControls.CustomCheckListBox, choices=choices)
		self.markdownExtensions.CheckedItems = getMarkdownExtensions(True)
		self.markdownExtensions.Select(0)
		self.defaultPath = sHelper.addLabeledControl(
			_("Pat&h:"), wx.TextCtrl, value=config.conf["markdownForever"]["defaultPath"])

		self.choose_path_btn = bHelper.addButton(
			self, label=_("&Browse..."))
		self.choose_path_btn.Bind(wx.EVT_BUTTON, self.onChoosePath)
		sHelper.addItem(bHelper)

		fileNameText = _("&File name:")
		self.fileNameTextCtrl = sHelper.addLabeledControl(
			fileNameText, wx.TextCtrl)
		self.fileNameTextCtrl.SetValue(config.conf["markdownForever"]["defaultFileName"])

	def onChoosePath(self, evt):
		dlg = wx.DirDialog(self, message=_("Choose a folder"),
						   defaultPath=realpath(self.defaultPath.GetValue()),
						   style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		if dlg.ShowModal() == wx.ID_OK:
			self.defaultPath.SetValue(dlg.GetPath())
		self.defaultPath.SetFocus()
		dlg.Destroy()

	def onSave(self):
		updateCheckChoice = self.updateCheck.GetSelection()
		size = len(self.updateChannels)
		config.conf["markdownForever"]["autoCheckUpdate"] = updateCheckChoice < size
		config.conf["markdownForever"]["updateChannel"] = self.updateChannels[updateCheckChoice % size]

		tableOfContentsBackList = self.tableOfContentsBackList.CheckedItems
		tableOfContentsBackList = translate_back_toc(tableOfContentsBackList)
		config.conf["markdownForever"]["toc-back"] = tableOfContentsBackList

		defaultPath = self.defaultPath.GetValue()
		if not os.path.exists(realpath(defaultPath)):
			gui.messageBox(
				_("Invalid folder path."),
				addonSummary,
				wx.OK | wx.ICON_ERROR
			)
			return self.defaultPath.SetFocus()
		config.conf["markdownForever"]["toc"] = self.tableOfContentsCheckBox.IsChecked()
		config.conf["markdownForever"]["autonumber-headings"] = self.numberHeadingsCheckBox.IsChecked()
		config.conf["markdownForever"]["extratags"] = self.extratagsCheckBox.IsChecked()
		config.conf["markdownForever"]["genMetadata"] = self.genMetadataCheckBox.IsChecked()
		config.conf["markdownForever"]["IM_defaultAction"] = list(
			IM_actions.values())[self.defaultActionListBox.GetSelection()]
		config.conf["markdownForever"]["markdownEngine"] = markdownEngines[self.markdownEngineListBox.GetSelection()]
		if defaultPath:
			config.conf["markdownForever"]["defaultPath"] = defaultPath
			config.conf["markdownForever"]["defaultFileName"] = ''.join([c for c in self.fileNameTextCtrl.GetValue() if c not in '\r\n\t\\/:*?"<>|']).strip()
		config.conf["markdownForever"]["markdownExtensions"] = ",".join(
			getMarkdownExtensionsFromIndexes(self.markdownExtensions.CheckedItems))
		config.conf["markdownForever"]["markdown2Extras"] = ""


class ManageHTMLTemplatesDlg(gui.settingsDialogs.SettingsPanel):

	title = _("HTML Templates")

	def makeSettings(self, settingsSizer):
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		bHelper = gui.guiHelper.ButtonHelper(orientation=wx.HORIZONTAL)

		HTMLTemplatesText = _("HTML templates &list:")
		self.HTMLTemplatesListBox = sHelper.addLabeledControl(
			HTMLTemplatesText, wx.Choice, choices=getHTMLTemplates())
		self.HTMLTemplatesListBox.SetSelection(getDefaultHTMLTemplateID())
		self.HTMLTemplatesListBox.Bind(
			wx.EVT_CHOICE, self.onHTMLTemplatesListBox)

		self.defaultTemplateBtn = bHelper.addButton(
			self, label="%s..." % _("Set as &default template"))
		self.defaultTemplateBtn.Bind(
			wx.EVT_BUTTON, self.onSetDefaultTemplateBtn)
		bHelper.addButton(parent=self, label="%s..." %
						  _("&Edit")).Bind(wx.EVT_BUTTON, self.onEditClick)
		bHelper.addButton(parent=self, label="%s..." %
						  _("&Add")).Bind(wx.EVT_BUTTON, self.onAddClick)
		self.removeBtn = bHelper.addButton(parent=self, label=_("&Remove"))
		self.removeBtn.Bind(wx.EVT_BUTTON, self.onRemoveClick)
		self.onHTMLTemplatesListBox()

		sHelper.addItem(bHelper)

	def refreshTemplatesList(self, name=None):
		self.HTMLTemplatesListBox.Set(getHTMLTemplates())
		self.HTMLTemplatesListBox.SetSelection(getDefaultHTMLTemplateID(name))

	def onHTMLTemplatesListBox(self, evt=None):
		templateID = self.HTMLTemplatesListBox.GetSelection()
		HTMLTemplate = getHTMLTemplateFromID(templateID)
		if templateID in [0, 1]:
			self.removeBtn.Disable()
		else:
			self.removeBtn.Enable()
		if HTMLTemplate != config.conf["markdownForever"]["HTMLTemplate"]:
			self.defaultTemplateBtn.Enable()
		else:
			self.defaultTemplateBtn.Disable()

	def onSetDefaultTemplateBtn(self, evt=None):
		templateID = self.HTMLTemplatesListBox.GetSelection()
		HTMLTemplate = getHTMLTemplateFromID(templateID)
		config.conf["markdownForever"]["HTMLTemplate"] = HTMLTemplate
		self.onHTMLTemplatesListBox()
		self.HTMLTemplatesListBox.SetFocus()

	def onEditClick(self, gesture):
		editIndex = self.HTMLTemplatesListBox.GetSelection()
		if editIndex < 0:
			return
		entryDialog = TemplateEntryDlg(self)
		templateName = getHTMLTemplates()[editIndex]
		entryDialog.templateName.SetValue(
			templateName if editIndex else "default")
		templateEntry = None
		try:
			templateEntry = getHTMLTemplate(		templateName if editIndex else "default")
		except json.decoder.JSONDecodeError:
			templateEntry = getHTMLTemplate("default")
		entryDialog.templateDescription.SetValue(templateEntry["description"])
		entryDialog.templateContent.SetValue(templateEntry["content"])
		if entryDialog.ShowModal() == wx.ID_OK:
			templateName = entryDialog.templateEntry["name"]
			templateDescription = entryDialog.templateEntry["description"]
			fp = "%s/%s.tpl" % (configDir, templateName)
			config.conf["markdownForever"]["HTMLTemplates"][templateName] = templateDescription
			with open(fp, "w") as writeFile:
				json.dump(entryDialog.templateEntry, writeFile, indent=4)
			clearHTMLTemplateCache()
			self.refreshTemplatesList(templateName)
		entryDialog.Destroy()

	def onRemoveClick(self, gesture):
		removeIndex = self.HTMLTemplatesListBox.GetSelection()
		if removeIndex < 1:
			return
		templateName = getHTMLTemplates()[removeIndex]
		choice = gui.messageBox(_("Are you sure to want to delete the '%s' template?") % templateName, '%s – %s' % (
			addonSummary, _("Confirmation")), wx.YES_NO | wx.ICON_QUESTION)
		if choice == wx.NO:
			return
		if config.conf["markdownForever"]["HTMLTemplate"] == templateName:
			config.conf["markdownForever"]["HTMLTemplate"] = "default"
		config.conf["markdownForever"]["HTMLTemplates"] = {
			k: v for k, v in config.conf["markdownForever"]["HTMLTemplates"].copy().items() if k != templateName}
		fp = "%s/%s.tpl" % (configDir, templateName)
		if os.path.exists(fp):
			os.remove(fp)
		clearHTMLTemplateCache()
		self.refreshTemplatesList()
		self.HTMLTemplatesListBox.SetSelection(removeIndex-1)
		self.HTMLTemplatesListBox.SetFocus()

	def onAddClick(self, gesture):
		entryDialog = TemplateEntryDlg(self, title=_("Add template"))
		entryDialog.templateContent.SetValue(
			getHTMLTemplate("default")["content"])
		if entryDialog.ShowModal() == wx.ID_OK:
			templateName = entryDialog.templateEntry["name"]
			if templateName in getHTMLTemplates():
				gui.messageBox(
					_("A template with this name already exists."),
					addonSummary,
					wx.OK | wx.ICON_ERROR
				)
				entryDialog.Destroy()
				self.HTMLTemplatesListBox.SetFocus()
				return
			templateDescription = entryDialog.templateEntry["description"]
			fp = "%s/%s.tpl" % (configDir, templateName)
			config.conf["markdownForever"]["HTMLTemplates"][templateName] = templateDescription
			with open(fp, "w") as writeFile:
				json.dump(entryDialog.templateEntry, writeFile, indent=4)
			clearHTMLTemplateCache()
			self.refreshTemplatesList(templateName)
		entryDialog.Destroy()

	def onSave(self):
		pass


class TemplateEntryDlg(wx.Dialog):
	# Translators: This is the label for the edit template entry dialog.
	def __init__(self, parent=None, title=_("Edit template")):
		super().__init__(parent, title=title)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		templateNameText = _("&Name:")
		self.templateName = sHelper.addLabeledControl(
			templateNameText, wx.TextCtrl)
		templateDescriptionText = _("&Description:")
		self.templateDescription = sHelper.addLabeledControl(
			templateDescriptionText, wx.TextCtrl, style=wx.TE_MULTILINE, size=(700, -1))
		templateContentText = _("&Content:")
		self.templateContent = sHelper.addLabeledControl(
			templateContentText, wx.TextCtrl, style=wx.TE_MULTILINE, size=(700, -1))
		sHelper.addDialogDismissButtons(
			self.CreateButtonSizer(wx.OK | wx.CANCEL))
		mainSizer.Add(sHelper.sizer, border=20, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
		self.templateName.SetFocus()

	def onOk(self, evt):
		templateName = self.templateName.GetValue()
		templateDescription = self.templateDescription.GetValue()
		templateContent = self.templateContent.GetValue()
		pattern = "^[a-z0-9_-]{%d,%d}$" % (minCharTemplateName,
										   maxCharTemplateName)
		if templateName == "default" or not re.match(pattern, templateName):
			letters = "a-z"
			digits = "0-9"
			hyphen = '-'
			underscore = '_'
			msg = _("Wrong value for template name field. Field must contain only letters in lowercase ({letters}), digits ({digits}), hyphen ({hyphen}) or underscore ({underscore}). A maximum of {maxCharTemplateName} characters. The following name is not allowed: \"default\".").format(
				letters=letters,
				digits=digits,
				hyphen=hyphen,
				underscore=underscore,
				maxCharTemplateName=maxCharTemplateName
			)
			gui.messageBox(msg, addonSummary, wx.OK | wx.ICON_ERROR)
			self.templateName.SetFocus()
			return
		if not templateContent.strip():
			msg = _("Content field empty.")
			gui.messageBox(msg, addonSummary, wx.OK | wx.ICON_ERROR)
			self.templateContent.SetFocus()
			return

		mustPresent = ["lang", "head", "header", "body"]
		notPresent = [
			tag for tag in mustPresent if "{%s}" % tag not in templateContent]
		if notPresent:
			missingFields = ", ".join(mustPresent)
			eg = "{%s}" % random.choice(mustPresent)
			msg = _("Content field invalid. The following required tags are missing: {missingFields}. Each tag must be surrounded by braces. E.g.: {eg}.").format(
				missingFields=missingFields,
				eg=eg
			)
			gui.messageBox(msg, addonSummary, wx.OK | wx.ICON_ERROR)
			self.templateContent.SetFocus()
			return
		self.templateEntry = {
			"name": templateName,
			"description": templateDescription,
			"content": templateContent
		}
		evt.Skip()


class WebServerDlg(gui.settingsDialogs.SettingsPanel):

	title = _("Web server")

	def getRootFolders(self):
		out = []
		for _, v in config.conf["markdownForever"]["HTTPServer"]["rootDirs"].copy().items():
			if v:
				out.append(v)
		if not out:
			out.append(config.conf["markdownForever"]["defaultPath"])
		return out

	def makeSettings(self, settingsSizer):
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		bHelper = gui.guiHelper.ButtonHelper(orientation=wx.HORIZONTAL)
		self.host = sHelper.addLabeledControl(
			_("&Host:"), wx.TextCtrl, value=config.conf["markdownForever"]["HTTPServer"]["host"])
		self.port = sHelper.addLabeledControl(_("&Port:"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=1, max=65535, initial=int(
			config.conf["markdownForever"]["HTTPServer"]["port"]))
		self.defaultEncoding = sHelper.addLabeledControl(
			_("Default &encoding:"), wx.TextCtrl, value=config.conf["markdownForever"]["HTTPServer"]["defaultEncoding"])
		rootFoldersText = _("Root &folders:")
		choices = self.getRootFolders()
		self.rootFoldersListBox = sHelper.addLabeledControl(
			rootFoldersText, wx.Choice, choices=choices)
		active = str(config.conf["markdownForever"]["HTTPServer"]["activeWebRoot"] or "").strip()
		if active and active in choices:
			self.rootFoldersListBox.SetSelection(choices.index(active))
		elif choices:
			self.rootFoldersListBox.SetSelection(0)
		HTTPServer.stop()

	def onSave(self):
		host = self.host.GetValue().strip()
		port = self.port.GetValue()
		defaultEncoding = self.defaultEncoding.GetValue().strip()
		if host:
			config.conf["markdownForever"]["HTTPServer"]["host"] = host
		if port:
			config.conf["markdownForever"]["HTTPServer"]["port"] = port
		if defaultEncoding:
			try:
				"test".encode(defaultEncoding)
			except LookupError:
				gui.messageBox(
					_("Invalid text encoding."),
					addonSummary,
					wx.OK | wx.ICON_ERROR
				)
				return self.defaultEncoding.SetFocus()
			config.conf["markdownForever"]["HTTPServer"]["defaultEncoding"] = defaultEncoding
		choices = self.getRootFolders()
		sel = self.rootFoldersListBox.GetSelection()
		if 0 <= sel < len(choices):
			config.conf["markdownForever"]["HTTPServer"]["activeWebRoot"] = choices[sel]


class AddonSettingsDialog(gui.settingsDialogs.MultiCategorySettingsDialog):
	categoryClasses = [
		GeneralDlg,
		ManageHTMLTemplatesDlg,
		WebServerDlg,
	]

	def __init__(self, parent, initialCategory=None):
		# Translators: title of add-on parameters dialog.
		dialogTitle = _("Settings")
		self.title = "%s - %s" % (addonSummary, dialogTitle)
		super().__init__(parent, initialCategory)
