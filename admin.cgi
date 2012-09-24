#!/usr/bin/perl
use utf8;
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

</head>
<html>
<body>
<div id="contents">

<div id ="wrapper">
<img src="images/admin.gif" /><br>
<img src="images/line.gif" /><br>

<div id="information">

登録情報<br>
ログイン名：<br>
URL：<br>
</div>
日記投稿<br>
<br>
<form action="post2.cgi" method="post">
<input type="hidden" name="login_id" value="1">
題名<br>
<input type="text" name="entry_title" value="$entry_title" size="20"></td>
記事<br>
<textarea name="entry_text" value="$entry_text" id="entry_text_form" /></textarea>
<br>
<input type="submit" value="投稿">
END_OF_HTML


print << "END_OF_HTML";
</form>
</div>

</div>
</body>
</html>
END_OF_HTML
exit;