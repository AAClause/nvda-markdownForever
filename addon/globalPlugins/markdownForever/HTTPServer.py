# Part of Markdown Forever Add-on for NVDA
# This file is covered by the GNU General Public License.
# See the file LICENSE for more details.
# Copyright 2019-2021 André-Abush Clause, Sof and other contributors. Released under GPL.
# <https://github.com/aaclause/nvda-markdownForever>

import codecs
import os
import os.path as osp
import re
import threading
import urllib.parse as urlParse
from http.server import BaseHTTPRequestHandler, HTTPServer
import addonHandler
import config
from .common import convertToHTML, extractMetadata, isPath, realpath

addonHandler.initTranslation()

HTMLTemplate = """<!DOCTYPE HTML>
<html>
	<head>
		<title>{title}</title>
		<meta charset="{encoding}" />
	</head>
	<body>
		{body}
	</body>
</html>"""


def mergeHTMLTemplate(
		title=_("No title"),
		body="<p>%s</p>" % _("No content"),
		encoding=None
):
	if not encoding:
		encoding = config.conf["markdownForever"]["HTTPServer"]["defaultEncoding"]
	return HTMLTemplate.format(
		title=title,
		body=body,
		encoding=encoding
	)


def indexOf(path):
	entries = sorted(os.listdir(path), key=lambda name: name.lower())
	out = "<h1>%s</h1><ul>" % _("Index of {path}").format(path=path)
	for entry in entries:
		full_entry = osp.join(path, entry)
		href = entry
		if isPath(full_entry):
			href += "/"
		elif not re.match(r"^.+\.(html?|md|txt)$", entry.lower()):
			continue
		out += f'<li><a href="{href}">{href}</a></li>'
	out += "</ul>"
	return out


def _resolve_request_path(request_path, base_dir):
	base_dir = osp.abspath(realpath(base_dir))
	relative_path = request_path.lstrip("/").replace("/", osp.sep)
	full_path = osp.abspath(osp.join(base_dir, relative_path))
	try:
		is_within_base = osp.commonpath([base_dir, full_path]) == base_dir
	except ValueError:
		is_within_base = False
	if not is_within_base:
		return None
	return full_path


def getFile(path, baseDir=None):
	if not baseDir:
		baseDir = config.conf["markdownForever"]["defaultPath"]
	encoding = config.conf["markdownForever"]["HTTPServer"]["defaultEncoding"]
	fullPath = _resolve_request_path(path, baseDir)
	if not fullPath:
		body = mergeHTMLTemplate(
			title=_("Error 403"),
			body="<p>%s.</p>" % _("Access denied")
		)
		return 403, body.encode(encoding)
	if not osp.exists(fullPath):
		body = mergeHTMLTemplate(
			title=_("Error 404"),
			body="<p>%s.</p>" % _("The requested URL “{path}” was not found").format(path=path)
		)
		return 404, body.encode(encoding)
	if isPath(fullPath):
		index_md = osp.join(fullPath, "index.md")
		index_html = osp.join(fullPath, "index.html")
		if osp.exists(index_md):
			fullPath = index_md
		elif osp.exists(index_html):
			fullPath = index_html
		else:
			body = mergeHTMLTemplate(
				title=_("Index of {path}").format(path=path),
				body=indexOf(fullPath)
			)
			return 200, body.encode(encoding)
	with codecs.open(fullPath, encoding=encoding) as f:
		text = f.read()
	if fullPath.lower().endswith((".html", ".htm")):
		body = text
	else:
		metadata, text = extractMetadata(text)
		body = convertToHTML(text, metadata, display=False)
		body = mergeHTMLTemplate(title=metadata["title"], body=body)
	return 200, body.encode(encoding)


class Server(BaseHTTPRequestHandler):

	def log_request(self, code='-', size='-'):
		return

	def _set_response(self, status_code=200):
		self.send_response(status_code)
		self.send_header("Content-type", "text/html; charset=%s" %
						 config.conf["markdownForever"]["HTTPServer"]["defaultEncoding"])
		self.end_headers()

	def do_GET(self):
		path = urlParse.unquote(self.path)
		if '?' in path:
			splitPath = path.split('?')
			path = splitPath[0]
		status_code, body = getFile(path)
		self._set_response(status_code)
		self.wfile.write(body)

	def do_POST(self):
		self._set_response(405)
		self.wfile.write(b"Method Not Allowed")


class CreateHTTPServer(threading.Thread):

	httpd = None

	def run(self):
		server_class = HTTPServer
		handler_class = Server
		host = config.conf["markdownForever"]["HTTPServer"]["host"]
		port = config.conf["markdownForever"]["HTTPServer"]["port"]
		server_address = (host, port)
		self.httpd = server_class(server_address, handler_class)
		self.httpd.serve_forever()


httpdThread = None


def run():
	global httpdThread
	if httpdThread:
		return
	httpdThread = CreateHTTPServer()
	httpdThread.daemon = True
	httpdThread.start()


def stop():
	global httpdThread
	if not httpdThread:
		return
	if httpdThread.httpd:
		httpdThread.httpd.shutdown()
		httpdThread.httpd.socket.close()
	httpdThread.join()
	httpdThread = None


def isRun():
	if httpdThread:
		return True
	return False
