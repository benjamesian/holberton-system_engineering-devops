#!/usr/bin/env ruby
a = ARGV[0].scan(/(?<=\[from:)(?:(?!\]).)*(?=\])/).join
b = ARGV[0].scan(/(?<=\[to:)(?:(?!\]).)*(?=\])/).join
c = ARGV[0].scan(/(?<=\[flags:)(?:(?!\]).)*(?=\])/).join
puts a+','+b+','+c
