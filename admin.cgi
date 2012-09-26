#!/usr/bin/perl

# 2012/09/26
# ↓これ書くと500エラーになる
# use strict;
# use warnings;

# 2012/09/26
# あんちぽ先生に書いていただいた
# login_idが定義されている？
# - 「 Common::GetCookie();」したものを「%cookie」の中に入れている？
# %と$の違いを明確にしておく
# ---------------------------------------

require 'common.pl';
my %cookie = Common::GetCookie();
my $login_id = $cookie{login_id};

print "Content-type: text/html\n\n";

print << "END_OF_HTML";
<html>
<body>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />

<!--viewportの指定-->
<meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=0" />
<!--/viewportの指定-->
<!--メディアクエリでPC用・スマホ用CSSを振り分け-->
<link media="only screen and (min-device-width:481px)" href="style.css" type="text/css" rel="stylesheet" />
<link media="only screen and (max-device-width:480px)" href="istyle.css" type="text/css" rel="stylesheet" />
<!--/メディアクエリでPC用・スマホ用CSSを振り分け-->

<link href="style.css" type="text/css" rel="stylesheet" />
<title>管理画面 - nikki</title>
</head>
<html>
<body>
<div id="contents">
<div id ="wrapper">
<a href="admin.cgi"><img src="images/admin.gif" /></a><br>
<img src="images/line.gif" /><br><br>
</div>
<img src="images/write.gif" />
<form action="entry_post.cgi" method="post">
<input type="hidden" name="login_id" value="$login_id">
<br>
<textarea name="entry_text" value="$entry_text" id="entry_text_form" /></textarea>
<br><br>
<input type="submit" value="投稿" class="form_button"><br><br>
<img src="images/line.gif" /><br>
</form>
</div>

</div>
</body>
</html>
END_OF_HTML
exit;