#!/usr/bin/env ruby

url = ARGV[0].dup
url.sub!("trac/projects/browser","svn")
url.sub!("#","/")
puts url

