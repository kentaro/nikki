#!/usr/bin/perl

require './common.pl';
use strict;
use DBI;

# データベース接続
my $conn = Common::ConnectDB();

# パラメータ取得
my %data = Common::GetPara();
my $login_id   = $data{"login_id"};
my $entry_text = $data{"entry_text"};

# 日記書き込み
my $sql = "
insert into entry (
login_id,
entry_text
) values (
" . Common::EscapeSQL($login_id) . ",
" . Common::EscapeSQL($entry_text) . "
)";

# データベース書き込み
my $select = $conn->prepare($sql);
my $rec = $select->execute;
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