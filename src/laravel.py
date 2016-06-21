import vim
import re
import os
import commands


def getComposerPath(name):
    paths = os.path.dirname(name).split('/')
    dir = ''
    for i, path in enumerate(paths):
        p = '/'.join(paths[:i + 1])
        artisan = p + '/artisan'
        if os.path.exists(artisan):
            dir = p
            break
    return dir


def laravel_controller():
    name = vim.current.buffer.name
    path = getComposerPath(name)
    controller = vim.eval('a:000')
    cpath = '/app/Http/Controllers'
    if len(controller):
        cname = controller[0]
        fname = "%sController" % cname.capitalize()
        cmd = 'php %s/artisan make:controller %s' % (path, fname)
        if not os.path.isfile(cpath + '/' + fname):
            f = commands.getoutput(cmd)
        path = '%s/app/Http/Controllers/%s.php' % (path, fname)
        vim.command(':e %s' % path)
    else:
        path += cpath
        vim.command('CtrlP %s' % path)


def laravel_view():
    cfile = vim.eval('expand("<cfile>")')
    line = vim.current.line
    name = vim.current.buffer.name
    path = getComposerPath(name)
    v = '/resources/views'
    if re.search("@extends|@include|view", line):
        f = cfile.replace('.', '/')
        dir = path + v
        for d in f.split('/')[:-1]:
            dir = "%s/%s" % (dir, d)
            if not os.path.isdir(dir):
                os.mkdir(dir)
        vv = "%s%s/%s.blade.php" % (path, v, f)
        vim.command(':e %s' % vv)
    else:
        path += v
        num = int(vim.eval('exists(":CtrlP")'))
        if num > 0:
            vim.command('CtrlP %s' % path)
        else:
            vim.command('e %s' % path)


def laravel_use():
    line = str(vim.current.line)
    x = re.search(r'\s([\w\\]+)\s?', line)
    if x:
        sr = x.group(1)
        name = sr.split('\\')[-1]
        n = int(vim.eval("line('.')"))
        vim.current.buffer[n - 1] = line.replace(sr, name)
        vim.current.buffer.append('use %s;' % x.group(1), 2)
