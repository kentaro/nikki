#!/usr/bin/perl

# 日記の表示画面です

require './common.pl';
use strict;
use DBI;

my %cookie = Common::GetCookie();
my $login_id = $cookie{login_id};

# データベース接続
my $conn = Common::ConnectDB();

my $sql = "
select
entry_text,
entry_time,
login_id
from
entry
where login_id=
" . Common::EscapeSQL($login_id) .
" order by entry_time desc";

# データベース読み込み
my $select = $conn->prepare($sql);
my $rec = $select->execute;
if(!$rec)
{
Common::DspMsg("データベースエラー : " . $sql);
exit;
}

# データベースクローズ
Common::CloseDB($conn);

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
<div id="contents">

<div id ="wrapper">

<img src="images/line.gif" /><br><br>
<div id="entry_contents">
<br>
END_OF_HTML
my (@user);
while (@user = $select->fetchrow) {
print $user[0] . "<br><br>" . $user[1] . "<br>" ;
}
print << "END_OF_HTML";
<img src="images/line.gif" /><br><br>
</div>
</div>
</div>



</body>
</html>
END_OF_HTML

exit;