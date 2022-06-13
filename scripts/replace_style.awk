#!/bin/awk
BEGIN{style_flag=0}

/<style>/{
	style_flag=1
}

//{
	if(style_flag == 0) print $0
}

/<\/style>/{
	style_flag=0
	print f1
}
