local lsp = require('lsp-zero')

lsp.preset('recommended')
require('mason').setup()
lsp.setup()
