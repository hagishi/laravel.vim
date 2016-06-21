pyfile <sfile>:h:h/src/laravel.py
python import vim

function! laravel#controller(...)
python laravel_controller(vim.current.buffer.name, vim.eval("a:000"))
endfunction


function! laravel#view(...)
python laravel_view()
endfunction

function! laravel#use()
python laravel_use()
endfunction
