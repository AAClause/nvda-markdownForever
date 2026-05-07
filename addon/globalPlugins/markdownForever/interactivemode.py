# Part of Markdown Forever Add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file LICENSE for more details.
# Copyright 2019-2022 André-Abush Clause, Sof and other contributors. Released under GPL.
# <https://github.com/aaclause/nvda-markdownForever>

import re
import os

import gui
import wx
import ui

import addonHandler
import api
import config
from logHandler import log

from .common import (
	getHTMLTemplates, getHTMLTemplateFromID, getDefaultHTMLTemplateID,
	getMetadataBlock, extractMetadata,
	convertToHTML, convertToMD, copyToClipAsHTML,
	getReplacements, writeFile,
	addonSummary, IM_actions,
	translate_back_toc
)

addonHandler.initTranslation()

class InteractiveModeDlg(wx.Dialog):
	destFormatChoices = ["HTML", _("HTML source"), "Markdown"]
	destFormatChoices_ = ["HTML", "HTMLSrc", "md"]

	def __init__(self,
		parent=None, 
		# Translators: This is the label for the interactive mode dialog.
		title=_("Interactive mode") + f" — {addonSummary}",
		text=''
	):
		self.metadata, self.text = extractMetadata(text)
		metadata = self.metadata
		defaultAction = config.conf["markdownForever"]["IM_defaultAction"]
		super().__init__(parent, title=title)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		b_helper_path = gui.guiHelper.ButtonHelper(orientation=wx.HORIZONTAL)
		isHTMLPattern = re.search("(?:</html>|</p>)", self.text, re.IGNORECASE)
		guessDestFormat = 2 if isHTMLPattern else 0
		destFormatText = _("C&onvert to:")
		self.destFormatListBox = sHelper.addLabeledControl(
			destFormatText, wx.Choice, choices=self.destFormatChoices)
		self.destFormatListBox.Bind(wx.EVT_CHOICE, self.onDestFormatListBox)
		self.destFormatListBox.SetSelection(guessDestFormat)

		genMetadataText = _(
			"Generate corresponding &metadata from HTML source")
		self.genMetadataCheckBox = sHelper.addItem(
			wx.CheckBox(self, label=genMetadataText))
		self.genMetadataCheckBox.SetValue(metadata["genMetadata"])
		self.genMetadataCheckBox.Bind(
			wx.EVT_CHECKBOX, self.onDestFormatListBox)

		tableOfContentsText = _("&Generate a table of contents")
		self.tableOfContentsCheckBox = sHelper.addItem(
			wx.CheckBox(self, label=tableOfContentsText))
		self.tableOfContentsCheckBox.SetValue(metadata["toc"])

		tableOfContentsBackText = _('Choose where add "Bac&k to Table of Contents" links')
		choices = []
		for i in range(1, 7):
			choices.append(_("Before level %d headings") % i)
			choices.append(_("After level %d headings") % i)
		self.tableOfContentsBackList = sHelper.addLabeledControl(tableOfContentsBackText, gui.nvdaControls.CustomCheckListBox, choices=choices)
		checked_items = translate_back_toc(metadata["toc-back"], True)
		self.tableOfContentsBackList.CheckedItems = checked_items
		self.tableOfContentsBackList.Bind(wx.EVT_CHECKLISTBOX, self.onUpdateMetadata2)

		numberHeadingsText = _("Try to automatically &number headings")
		self.numberHeadingsCheckBox = sHelper.addItem(
			wx.CheckBox(self, label=numberHeadingsText))
		self.numberHeadingsCheckBox.SetValue(metadata["autonumber-headings"])

		extratagsText = _("Enable e&xtra tags")
		self.extratagsCheckBox = sHelper.addItem(
			wx.CheckBox(self, label=extratagsText))
		self.extratagsCheckBox.SetValue(metadata["extratags"])

		backTranslateExtraTagsText = _("Allow extratags bac&k translation")
		self.backTranslateExtraTagsCheckBox = sHelper.addItem(
			wx.CheckBox(self, label=backTranslateExtraTagsText))
		self.backTranslateExtraTagsCheckBox.SetValue(metadata["extratags-back"])

		detectExtratagsText = _("&Detect extratags if possible")
		self.detectExtratagsCheckBox = sHelper.addItem(
			wx.CheckBox(self, label=detectExtratagsText))
		self.detectExtratagsCheckBox.SetValue(metadata["detectExtratags"])

		titleLabelText = _("&Title:")
		self.titleTextCtrl = sHelper.addLabeledControl(
			titleLabelText, wx.TextCtrl)
		self.titleTextCtrl.SetValue(metadata["title"])
		self.titleTextCtrl.Bind(wx.EVT_TEXT, self.onUpdateMetadata)

		subtitleText = _("S&ubtitle:")
		self.subtitleTextCtrl = sHelper.addLabeledControl(
			subtitleText, wx.TextCtrl)
		self.subtitleTextCtrl.SetValue(metadata["subtitle"])
		self.subtitleTextCtrl.Bind(wx.EVT_TEXT, self.onUpdateMetadata)

		pathText = _("Pat&h:")
		self.pathTextCtrl = sHelper.addLabeledControl(
			pathText, wx.TextCtrl)
		self.pathTextCtrl.SetValue(metadata["path"])
		self.pathTextCtrl.Bind(wx.EVT_TEXT, self.onUpdateMetadata)

		self.choose_path_btn = b_helper_path.addButton(
			self, label=_("Bro&wse..."))
		self.choose_path_btn.Bind(wx.EVT_BUTTON, self.onChoosePath)
		sHelper.addItem(b_helper_path)

		fileNameText = _("&File name:")
		self.fileNameTextCtrl = sHelper.addLabeledControl(
			fileNameText, wx.TextCtrl)
		self.fileNameTextCtrl.SetValue(metadata["filename"])
		self.fileNameTextCtrl.Bind(wx.EVT_TEXT, self.onUpdateMetadata)

		HTMLTemplatesText = _("HTML temp&late to use:")
		self.HTMLTemplatesListBox = sHelper.addLabeledControl(
			HTMLTemplatesText, wx.Choice, choices=getHTMLTemplates())
		self.HTMLTemplatesListBox.SetSelection(
			getDefaultHTMLTemplateID(metadata["template"]))
		self.HTMLTemplatesListBox.Bind(wx.EVT_CHOICE, self.onUpdateMetadata)

		correspondingMetadataBlockText = _("Corres&ponding metadata block")
		self.correspondingMetadataBlock = sHelper.addLabeledControl(
			correspondingMetadataBlockText, wx.TextCtrl, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_PROCESS_TAB, size=(700, -1))
		self.correspondingMetadataBlock.SetValue(getMetadataBlock(metadata))

		checkboxesToBind = [
			self.tableOfContentsCheckBox,
			self.numberHeadingsCheckBox,
			self.extratagsCheckBox,
			self.backTranslateExtraTagsCheckBox
		]
		for checkbox in checkboxesToBind:
			checkbox.Bind(wx.EVT_CHECKBOX, self.onUpdateMetadata)
		if self.text is not None and self.text.strip():
			bHelper = gui.guiHelper.ButtonHelper(orientation=wx.HORIZONTAL)
			self.virtualBufferBtn = bHelper.addButton(
				self, label=_("Show in &virtual buffer"))
			self.virtualBufferBtn.Bind(wx.EVT_BUTTON, self.onVB)
			if defaultAction == IM_actions["virtualBuffer"]:
				self.virtualBufferBtn.SetDefault()
			self.browserBtn = bHelper.addButton(self, label=_("Show in &browser"))
			self.browserBtn.Bind(wx.EVT_BUTTON, self.onBrowser)
			if defaultAction == IM_actions["browser"]:
				self.browserBtn.SetDefault()
			self.copyToClipBtn = bHelper.addButton(
				self, label=_("&Copy to clipboard"))
			self.copyToClipBtn.Bind(wx.EVT_BUTTON, self.onCopyToClipBtn)
			if defaultAction == IM_actions["copyToClip"]:
				self.copyToClipBtn.SetDefault()
			saveResultBtn = bHelper.addButton(
				self, label=_("&Save the result as..."))
			saveResultBtn.Bind(wx.EVT_BUTTON, self.onSave)
			if defaultAction == IM_actions["saveResultAs"]:
				saveResultBtn.SetDefault()
			saveSourceBtn = bHelper.addButton(
				self, label=_("Save the sou&rce as..."))
			saveSourceBtn.Bind(
				wx.EVT_BUTTON, lambda evt: self.onSave(evt, source=True))
			if defaultAction == IM_actions["saveSourceAs"]:
				saveSourceBtn.SetDefault()
			sHelper.addItem(bHelper)
		sHelper.addDialogDismissButtons(self.CreateButtonSizer(wx.CANCEL))

		mainSizer.Add(sHelper.sizer, border=20, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		self.destFormatListBox.SetFocus()
		self.onDestFormatListBox(None)

	def onUpdateMetadata(self, evt=None):
		self.updateMetadata()
		self.correspondingMetadataBlock.SetValue(
			getMetadataBlock(self.metadata)
		)

	def onUpdateMetadata2(self, evt=None):
		self.onUpdateMetadata()
		self.tableOfContentsBackList.notifyIAccessible(evt)

	def onDestFormatListBox(self, evt):
		destFormatChoices_ = self.destFormatListBox.GetSelection()
		if self.text is not None and self.text.strip():
			if destFormatChoices_ > 0:
				self.browserBtn.Disable()
			else:
				self.browserBtn.Enable()
		if destFormatChoices_ != 2:
			self.tableOfContentsCheckBox.Enable()
			self.tableOfContentsBackList.Enable()
			self.detectExtratagsCheckBox.Disable()
			self.genMetadataCheckBox.Disable()
			self.backTranslateExtraTagsCheckBox.Enable()
			self.correspondingMetadataBlock.Enable()
			self.extratagsCheckBox.Enable()
			self.numberHeadingsCheckBox.Enable()
			self.titleTextCtrl.Enable()
			self.subtitleTextCtrl.Enable()
			self.pathTextCtrl.Enable()
			self.choose_path_btn.Enable()
			self.fileNameTextCtrl.Enable()
			self.HTMLTemplatesListBox.Enable()
		else:
			self.tableOfContentsCheckBox.Disable()
			self.tableOfContentsBackList.Disable()
			self.detectExtratagsCheckBox.Enable()
			self.genMetadataCheckBox.Enable()
			self.backTranslateExtraTagsCheckBox.Disable()
			self.correspondingMetadataBlock.Disable()
			self.extratagsCheckBox.Disable()
			self.numberHeadingsCheckBox.Disable()
			self.titleTextCtrl.Disable()
			self.subtitleTextCtrl.Disable()
			self.pathTextCtrl.Disable()
			self.choose_path_btn.Disable()
			self.fileNameTextCtrl.Disable()
			self.HTMLTemplatesListBox.Disable()

	def onChoosePath(self, evt):
		dlg = wx.DirDialog(self, message=_("Choose a folder"),
						   defaultPath=realpath(self.metadata["path"]),
						   style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
		if dlg.ShowModal() == wx.ID_OK:
			self.pathTextCtrl.SetValue(dlg.GetPath())
		self.pathTextCtrl.SetFocus()
		dlg.Destroy()

	def onBrowser(self, evt): self.onExecute(False)

	def onVB(self, evt): self.onExecute(True)

	def updateMetadata(self):
		metadata = self.metadata

		metadata["toc"] = self.tableOfContentsCheckBox.IsChecked()
		log.info(self.tableOfContentsBackList.CheckedItems)
		tableOfContentsBackList = self.tableOfContentsBackList.CheckedItems
		tableOfContentsBackList = translate_back_toc(tableOfContentsBackList)
		metadata["toc-back"] = tableOfContentsBackList

		metadata["extratags"] = self.extratagsCheckBox.IsChecked()
		metadata["extratags-back"] = self.backTranslateExtraTagsCheckBox.IsChecked()
		metadata["genMetadata"] = self.genMetadataCheckBox.IsChecked()
		metadata["autonumber-headings"] = self.numberHeadingsCheckBox.IsChecked()
		metadata["detectExtratags"] = self.detectExtratagsCheckBox.IsChecked()
		metadata["title"] = self.titleTextCtrl.GetValue()
		metadata["subtitle"] = self.subtitleTextCtrl.GetValue()
		metadata["path"] = self.pathTextCtrl.GetValue()
		metadata["filename"] = ''.join([c for c in self.fileNameTextCtrl.GetValue() if c not in '\r\n\t\\/:*?"<>|']).strip()
		templateID = self.HTMLTemplatesListBox.GetSelection()
		metadata["template"] = getHTMLTemplateFromID(templateID)

	def onExecute(self, vb=False):
		self.updateMetadata()
		metadata = self.metadata
		destFormatChoices_ = self.destFormatListBox.GetSelection()
		if destFormatChoices_ == 0:
			convertToHTML(self.text, metadata,
						  useTemplateHTML=True, save=not vb)
		elif destFormatChoices_ == 1:
			convertToHTML(self.text, metadata, save=False, src=True)
		elif destFormatChoices_ == 2:
			convertToMD(self.text, metadata)
		self.Destroy()

	def onCopyToClipBtn(self, event):
		self.updateMetadata()
		metadata = self.metadata
		destFormatChoices_ = self.destFormatListBox.GetSelection()
		if destFormatChoices_ == 0:
			if copyToClipAsHTML(convertToHTML(self.text, metadata, display=False)):
				ui.message(_("Formatted HTML copied to clipboard"))
			else:
				return ui.message(_("Unable to copy formatted HTML to clipboard"))
		elif destFormatChoices_ == 1:
			api.copyToClip(convertToHTML(
				self.text, metadata, src=True, display=False))
		else:
			api.copyToClip(convertToMD(self.text, metadata, display=False))
		self.Destroy()

	def onSave(self, event, source=False):
		self.updateMetadata()
		metadata = self.metadata
		destFormatChoices_ = self.destFormatListBox.GetSelection()
		formats = [
			"HTML format (*.htm, *.html)|*.htm;*.html",
			"Text file (*.txt)|*.txt",
			"Markdown file (*.md)|*.md"
		]
		format = formats[1] if source else formats[destFormatChoices_]
		dlg = wx.FileDialog(None, _("Select the location"),
							metadata["path"], metadata["filename"], format, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
		if dlg.ShowModal() == wx.ID_OK:
			fp = os.path.join(dlg.GetDirectory(), dlg.GetFilename())
			if source and destFormatChoices_ != 2:
				text = self.text
				conserveExtraTags = gui.messageBox(
					_("Do you want to conserve extra-tags? If you select No, extra-tags will be interpreted before saving."),
					"Markdown Forever",
					wx.YES_NO
				)
				if conserveExtraTags == wx.NO:
					lang = metadata["langd"] if "langd" in metadata.keys(
					) else None
					replacements = getReplacements(lang)
					for toSearch, replaceBy, replaceAlways in replacements:
						if replaceAlways:
							text = re.sub(
								r"(^|[^~`])%s([^~`]|$)" % re.escape(toSearch),
								fr"\g<1>{replaceBy}\g<2>",
								text,
								flags=re.MULTILINE)
			else:
				text = ''
				if destFormatChoices_ == 0:
					convertToHTML(self.text, metadata,
								  useTemplateHTML=True, save=True, fp=fp)
				elif destFormatChoices_ == 1:
					text = convertToHTML(
						self.text, metadata, src=True, display=False)
				else:
					text = convertToMD(self.text, metadata, display=False)
			if text:
				writeFile(fp, text)
				os.startfile(fp)
			dlg.Destroy()
			self.Destroy()
			return
		else:
			dlg.Destroy()
			self.destFormatListBox.SetFocus()

	def onOk(self, evt):
		self.Destroy()
