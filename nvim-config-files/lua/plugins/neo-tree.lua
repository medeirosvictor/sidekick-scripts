return {
	"nvim-neo-tree/neo-tree.nvim",
	keys = {
      { "<C-b>", ":Neotree toggle left<CR>"},
      { "<leader>bf", ":Neotree buffers reveal float<CR>"},
  },
  branch = "v3.x",
	dependencies = {
		"nvim-lua/plenary.nvim",
		"nvim-tree/nvim-web-devicons",
		"MunifTanjim/nui.nvim",
	},
}
