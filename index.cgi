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

<img src="images/logo.gif" />

<div id="login_form">

<img src="images/line.gif" /><br><br>

<form action="login.cgi" method="post">
ログイン名　<input type="text" name="login_name"><br>
パスワード　<input type="password" name="password"><br>
<br>
<input type="submit" value="ログイン" class="form_button">
</form>

</div>

<img src="images/line.gif" /><br><br>
<a href="signup.cgi">新規登録はこちら</a>
END_OF_HTML


print << "END_OF_HTML";
</form>

</div>

</div>

</body>
</html>
END_OF_HTML
exit;