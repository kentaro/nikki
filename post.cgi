#!/usr/bin/perl

require './common.pl';
use strict;
use DBI;

# パラメータ取得
my %data = Common::GetPara();
my $login_id = $data{"login_id"};
my $login_name = $data{"login_name"};
my $password = $data{"password"};
my $email = $data{"email"};

# データベース接続
my $conn = Common::ConnectDB();

# トランザクション開始
my $select = $conn->prepare("begin");
my $rec = $select->execute;
if(!$rec)
{
Common::DspMsg("トランザクション開始処理に失敗しました");
exit;
}

# エラーチェック
if (!$login_name) {
Common::DspMsg("ユーザ名を入力してください。");
# データベースクローズ
Common::CloseDB($conn);
exit;
}
elsif ($login_name !~ /^[0-9a-zA-Z]/) {
Common::DspMsg("ユーザ名は半角英数字で入力してください。");
# データベースクローズ
Common::CloseDB($conn);
exit;
}

if (!$password) {
Common::DspMsg("パスワードを入力してください。");
# データベースクローズ
Common::CloseDB($conn);
exit;
}
elsif ($password !~ /^[0-9a-zA-Z]/) {
Common::DspMsg("パスワードは半角英数字で入力してください。");
# データベースクローズ
Common::CloseDB($conn);
exit;
}

if ($email !~ /^.*@.*\./) {
Common::DspMsg("メールアドレスを正しく入力してください。");
# データベースクローズ
Common::CloseDB($conn);
exit;
}

my $sql;
if ($data{"del"})
{
# ユーザ削除処理の場合
$sql = "
delete from
login_user
where
login_id = " . Common::EscapeSQL($login_id) . "
";
}
elsif ($data{"login_id"})
{
# ユーザ更新処理の場合
$sql = "
update
login_user
set
login_name = " . Common::EscapeSQL($login_name) . ",
password = " . Common::EscapeSQL($password) . ",
email = " . Common::EscapeSQL($email) . "
where
login_id = " . Common::EscapeSQL($login_id) . "
";
}
else {
# ユーザ新規登録の場合
$sql = "
insert into login_user (
login_name,
password,
email
) values (
" . Common::EscapeSQL($login_name) . ",
" . Common::EscapeSQL($password) . ",
" . Common::EscapeSQL($email) . "
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
<meta http-equiv="refresh" content="0;url=signup_finish.html">
</head>
</html>
END_OF_HTML

exit;