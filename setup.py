from distutils.core import setup
import os

try:
  import pandoc
  nopd = False
  if os.name != 'nt':
    pandoc.core.PANDOC_PATH = 'pandoc'
  else:
    if 'LOCALAPPDATA' in os.environ: app = os.getenv('LOCALAPPDATA')
    else: app = os.getenv('APPDATA')
    pandoc.core.PANDOC_PATH = '%s/Pandoc/pandoc' % (app, )
except (Exception, ), e:
  nopd = True

PKG_TITLE = 'make_GitHub_wiki_tree'
mdl = __import__(PKG_TITLE)
PKG_VER = mdl.__version__
PKG_URL = 'https://github.com/HatsuneMiku/make_GitHub_wiki_tree/wiki'
AUTHOR = '999hatsune'
AUTHOR_EMAIL = '999hatsune@gmail.com'
PKG_KWD = '''\
github wiki tree directory folder diary'''
PKG_DSC = '''\
make GitHub wiki tree'''

long_description = open('README.md', 'rb').read()
if not nopd:
  pd = pandoc.Document()
  pd.markdown = long_description
  long_description = pd.rst

kwargs = {
  'name'            : PKG_TITLE,
  'version'         : PKG_VER,
  'keywords'        : PKG_KWD,
  'description'     : (PKG_DSC),
  'long_description': long_description,
  'author'          : AUTHOR,
  'author_email'    : AUTHOR_EMAIL,
  'url'             : PKG_URL,
  'license'         : 'BSD License',
  'classifiers'     : [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 2 :: Only',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
  ]
}

setup(**kwargs)
