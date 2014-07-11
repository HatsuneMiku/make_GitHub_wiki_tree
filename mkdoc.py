#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''mkdoc.py
'''

import sys, os
import re
import pydoc
import pandoc

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONFFILE = u'mktree.cf'

if os.name != 'nt':
  pandoc.core.PANDOC_PATH = 'pandoc'
else:
  if 'LOCALAPPDATA' in os.environ: app = os.getenv('LOCALAPPDATA')
  else: app = os.getenv('APPDATA')
  pandoc.core.PANDOC_PATH = '%s/Pandoc/pandoc' % (app, )

def mkdoc(mdlname):
  r = re.compile(r'''(https://[^\s\']+)''', re.I)
  fn = 'module_%s' % mdlname
  txt = pydoc.TextDoc().docmodule(__import__(mdlname))
  md = []
  flg = False
  for line in txt.splitlines():
    if flg:
      flg = False
      continue
    outl = []
    f = False
    for i, l in enumerate(line):
      if l == '\x08':
        if i <= 1: f = True
        outl = outl[:-1]
      else:
        outl += [l]
    outline = ''.join(outl)
    if outline == 'FILE':
      flg = True
    else:
      #outline = r.sub(lambda m: '[%s](%s)' % (m.group(1), m.group(1)), outline)
      md += ['%s%s' % ('# ' if f else '', outline)]
  open(os.path.join(BASE_DIR, '%s.md' % fn), 'wb').write('\x0A'.join(md))

  # Do not use output of pydoc.HTMLDoc() because of poor design.
  # So convert to html from markdown created above.
  pd = pandoc.Document()
  pd.markdown = '\x0A'.join(md)
  open(os.path.join(BASE_DIR, '%s.html' % fn), 'wb').write(pd.html)

def main():
  cf = os.path.join(BASE_DIR, CONFFILE)
  ifp = open(cf, 'rb')
  if ifp is None:
    print u'cannot open %s' % cf
    return
  act, rep = map(lambda s: s.rstrip(), ifp.readlines())
  ifp.close()
  mkdoc(rep)

if __name__ == '__main__':
  main()
