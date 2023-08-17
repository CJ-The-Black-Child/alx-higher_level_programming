set nu
colorscheme slate

map <F2> :bprev<CR>
map <F3> :bnext<CR>
map <F5> :source ~/.vimrc<CR>

set autoindent
set cindent
syntax enable

autocmd BufWritePre * %s/\s\+$//e

set formatoptions=tcqro
autocmd FileType c,cpp,java setlocal formatoptions+=ro

autocmd BufWritePre *.py :Autopep8

autocmd FileType c setlocal noexpandtab shiftwidth=8 tabstop=8
autocmd FileType python setlocal expandtab shiftwidth=4 softtabstop=4

autocmd BufRead,BufNewFile *.html setfiletype html
autocmd BufRead,BufNewFile *.js setfiletype javascript
autocmd BufRead,BufNewFile *.css setfiletype css

"This here helps in using the Copen command to fix errors appropriately
command! -nargs=0 CopenLint call RunLint()

function! RunLint()
    let filetype = &filetype

    if filetype ==# 'c'
        let linter_cmd = 'betty'
    elseif filetype ==# 'python'
        let linter_cmd = 'pythoncodestyle'
    elseif filetype ==# 'javascript'
        let linter_cmd = 'semistandard'
    else
        echo "Unsupported file type for linting"
        return
    endif

    let linter_output = system(linter_cmd . ' ' . expand('%:p'))
    cexpr linter_output
    copen
endfunction

"function to open the  my terminal within vim editor mode

function! VexploreAndTerminal()

  " Open nerdtree on the left
  NERDTree
endfunction

map <F8> :call VexploreAndTerminal()<CR>

function! OpenTerminal()
  if winnr("$") == 1
    rightbelow term
  else
    wincmd w
    term
  endif
endfunction

map <F9> :term<CR>

autocmd FileType javascript setlocal expandtab shiftwidth=2 softtabstop=2

let g:syntastic_javascript_checkers = ['semistandard']
let g:syntastic_javascript_standard_exec = 'semistandard'
let g:syntastic_javascript_errorformat = '%f:%l:%c: %m'

set statusline+=%#warningmsg#
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'jiangmiao/auto-pairs'
Plugin 'moll/vim-node'
Plugin 'scrooloose/nerdtree'
Plugin 'pangloss/vim-javascript'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-syntastic/syntastic'

call vundle#end()
filetype plugin indent on
