return {
    "stevearc/oil.nvim",
    event = "VeryLazy",
    config = function()
        require("oil").setup({
            columns = {
                "icon",
                "permissions",
                "size",
                "mtime",
            },
            skip_confirm_for_simple_edits = false,
        })
        vim.keymap.set("n", "-", "<CMD>Oil<CR>", { desc = "Open parent directory" })
    end,
}
