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
    line = vim.current.line
    name = vim.current.buffer.name
    path = getComposerPath(name)
    v = '/resources/views'
    if re.search("@extends\(\'(.*)\'\)", line):
        m = re.search("@extends\(\'(.*)\'", line)
    else:
        m = re.search("view\(\'(.*)\'", line)

    if m:
        f = m.group(1)
        f = f.replace('.', '/')
        dir = path + '/' + v

        for d in f.split('/')[:-1]:
            path = "%s/%s" % (dir, d)
            if not os.path.isdir(dir):
                os.mkdir(path)
        vv = "%s/%s/%s.blade.php" % (path, v, f)
        vim.command(':e %s' % vv)
    else:
        path += v
        vim.command('CtrlP %s' % path)
