
if exists("g:loaded_laravel")
  finish
endif
let g:loaded_laravel = 1

let s:save_cpo = &cpo
set cpo&vim

command! -nargs=* LAc call laravel#controller(<f-args>)
command! -nargs=* LAv call laravel#view(<f-args>)
command! -nargs=* LAm call laravel#model(<f-args>)
command! -nargs=* LAt call laravel#test(<f-args>)
command! -nargs=* LUse call laravel#use(<f-args>)

let &cpo = s:save_cpo
unlet s:save_cpo
