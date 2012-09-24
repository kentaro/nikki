#!/usr/bin/perl

require './common.pl';
use strict;
use DBI;

# データベース接続
my $conn = Common::ConnectDB();

# 日記書き込み
$sql = "
insert into entry (
entry_title,
entry_text,
) values (
" . Common::EscapeSQL($login_title) . ",
" . Common::EscapeSQL($text) . ",
)";
}

# データベース書き込み
$select = $conn->prepare($sql);
$rec = $select->execute;
if(!$rec)
{
Common::DspMsg("データベースエラー : " . $sql);
exit;
}

# トランザクション終了
$select = $conn->prepare("commit");
$rec = $select->execute;
if(!$rec)
{
Common::DspMsg("コミット処理に失敗しました");
exit;
}

# データベースクローズ
Common::CloseDB($conn);

print "Content-type: text/html\n\n";

# ユーザ一覧画面へ遷移させる
print << "END_OF_HTML";
<html>
<head>
<meta http-equiv="refresh" content="0;url=admin.cgi">
</head>
</html>
END_OF_HTML

exit;