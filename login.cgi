#!/usr/bin/perl

#ログインの時につかう処理です
#2012/09/26 おそらく動いていません

# 呼び出している

require './common.pl';
use strict;
use warnings;
use DBI;

# ログイン画面で入力したものをもらっている
# ログイン認証処理あたりが多分間違っている気がします

# パラメータ取得
my %data = Common::GetPara();
my $login_name = $data{"login_name"};
my $password = $data{"password"};

# データベース接続
my $conn = Common::ConnectDB();

# ログイン認証処理
my $login_id = Common::CheckLogin($conn, $login_name, $password);

# データベースクローズ
Common::CloseDB($conn);

# データエスケープ
$login_name =~ s/ /%20/g;
$password =~ s/ /%20/g;

# クッキーセット処理
my $strCookie = "login_name=" . $login_name . " password=" . $password " login_id=" . $login_id;
Common::SetCookie($strCookie, 3*60*60);

print "Content-type: text/html\n\n";

# 管理画面に移動させる
print << "END_OF_HTML";
<html>
<head>
<meta http-equiv="refresh" content="0;url=admin.cgi">
</head>
</html>
END_OF_HTML

exit;