#!/usr/bin/perl
use utf8;

# CGIモジュールをインポート

use CGI;
use lib "lib";

# CGIインスタンスの生成
$cgi = new CGI();

# CGI::Sessionモジュールをインポート
use CGI::Session;


# セッションの生成（復元）
$session = new CGI::Session($cgi);


# セッションパラメータ「login_check」の値を変数login_checkに代入
$login_check = $session->param('login_check');


# セッションパラメータ「user_name」の値を変数user_nameに代入
$user_name = $session->param('user_name');


# HTTPヘッダを出力
print $session->header(-type=>'text/html',-charset=>'Shift-JIS');

# HTMLヘッダを出力
print $cgi->start_html(-title=>'掲示板',-lang=>'ja');


# ログイン確認
if ($login_check eq 'ok') {
	# 接続ユーザー名＋リンクの表示
	print 'Login: <b>' . $user_name . '</b>';
	print '<hr>';
	print '<a href="menu_message.pl">【メニュー】</a>';
	print '<a href="logout.pl">【ログアウト】</a>';
	print '<hr>';

	# 入力フォームの表示
	print '■メッセージを入力してください。<br><br>';
	print '<form action="insert_message.pl" method="POST">';
	print 'タイトル：<br>';
	print '<input type="text" name="title" size="50">';
	print '<br><br>';
	print 'メッセージ：<br>';
	print '<textarea name="message" cols="40" rows="5"></textarea>';
	print '<br><br>';
	print '<input type="submit" value="メッセージの登録">';
	print '</form>';
} else {
	# メッセージ＋リンクの表示
	print '■ログインしていません。';
	print '<hr>';
	print '<a href="login.html">【ログイン】</a>';
}

# HTMLフッタを出力
print $cgi->end_html();