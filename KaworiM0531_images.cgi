#!/usr/bin/ruby

require 'rubygems'
require 'twitter'

print "Content-type: text/html\n\n"

Twitter.search("from:KaworiM0531 いってくるわね", :rpp => 5, :result_type => "recent", :include_entities => 1).map do |status|
  print '<img src="' + status['attrs']['entities']['urls'][0]['expanded_url'].gsub(/(p.twipple.jp)/, "p.twipple.jp/show/large") + '" />' if !status['attrs'].nil? and !status['attrs']['entities'].nil? and !status['attrs']['entities']['urls'].nil?
end
