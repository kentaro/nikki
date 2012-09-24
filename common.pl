package Common;
use DBI;

# ★これは一体何だろう。

# ------------------------------------------------------------------
# 関数 : ConnectDB
# 概要 : データベース接続処理
# 引数 : なし
# 戻値 : データベースコネクション
# ------------------------------------------------------------------

sub ConnectDB
{
my $dbn  = "******";
my $user = "******";
my $pswd = "******";
my $host = "mysql577.phy.lolipop.jp";

# sub ConnectDBっていうのは決まっているもの？
# パスワードが平文？だけど、いいのかな。

# データベース接続
my $conn = DBI->connect('DBI:mysql:' . $dbn . ':' . $host, $user, $pswd);
if(!$conn)
{
DspMsg("データベースの接続に失敗しました");
exit;
}
return $conn;
}

# returnってなんだ…

#------------------------------------------------------------------
# 関数 : CloseDB
# 概要 : データベース切断
# 引数 : データベースコネクション
# 戻値 : なし
#------------------------------------------------------------------
sub CloseDB()
{
my($conn) = @_[0];
$conn->disconnect;
}

# 自分では書けなさそう

#------------------------------------------------------------------
# 関数 : CheckCookie
# 説明 : クッキーによるログイン認証
# 引数 : データベースコネクション
# 戻値 : 1:認証成功、それ以外:認証失敗(エラー画面を表示して終了)
#------------------------------------------------------------------
sub CheckCookie
{
my($conn) = @_[0];

# クッキー取得
my %cook = GetCookie();
return CheckLogin($conn, $cook{"login_name"}, $cook{"password"});
}

#------------------------------------------------------------------
# 関数 : CheckLogin
# 説明 : ログイン認証
# 引数 : データベースコネクション、ログイン名、パスワード
# 戻値 : 1:認証成功、それ以外:認証失敗(エラー画面を表示して終了)
#------------------------------------------------------------------
sub CheckLogin
{
my($conn) = @_[0];
my $login_name = @_[1];
my $password = @_[2];

# データベース読み込み
my $sql = "
select
count(*) as cnt,
login_id
from
login_user
where
login_name = " . EscapeSQL($login_name) . "
and
password = " . EscapeSQL($password) . "
";
my $select = $conn->prepare($sql);
my $rec = $select->execute;
if(!$rec)
{
DspMsg("データベースエラー : " . $sql);
exit;
}

my @data = $select->fetchrow;
if ($data[0] > 0) {
return $data[1];
}

DspMsg("ログインに失敗しました。<br>\n<br>\n<br>\n<a href=\"index.cgi\">ログイン画面へ</a>");

exit;
}

#------------------------------------------------------------------
# 関数 : DspMsg
# 概要 : メッセージ表示
# 引数 : メッセージ文字列
# 戻値 : なし
#------------------------------------------------------------------
sub DspMsg
{
my($msg) = @_[0];

print << "END_OF_HTML";
Content-type: text/html;

<HTML>
<HEAD>
<TITLE>$title</TITLE>
</HEAD>
<BODY>
<P><FONT style="font-size=9pt">$msg</FONT></P>
</BODY>
</HTML>
END_OF_HTML

return;
}

#------------------------------------------------------------------
# 関数 : GetPara
# 概要 : パラメータ取得
# 引数 : なし
# 戻値 : パラメータハッシュ配列
#------------------------------------------------------------------
sub GetPara
{
my $self = shift;
my($query_string); #// エンコードされたパラメータ全体
my(@a, $a); #// エンコードされたパラメータを分解したもの
my($name, $value); #// デコードされたパラメータ
my(%in);

#// パラメータの読み込み
if ($ENV{"REQUEST_METHOD"} eq "POST")
{
#// POSTなら標準入力から読み込む
read(STDIN, $query_string, $ENV{"CONTENT_LENGTH"});
}
else
{
#// GETなら環境変数から読み込む
$query_string = $ENV{"QUERY_STRING"};
}

#// 「変数名1=値1&変数名2=値2」の形式をアンパサンド(&)で分解
@a = split(/&/, $query_string);

# パラメータの取得
foreach $a(@a)
{
#// =（イコール）で分解
($name, $value) = split(/=/, $a);
#// + や %8A などのデコード
$value =~ tr/+/ /;
$value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex( $1 ))/eg;
#// 後で使用するため，$in{'パラメータ名'} に代入しておく
$in{$name} = $value;
}

return %in;
}

#------------------------------------------------------------------
# 関数 : SetCookie
# 説明 : クッキー設定
# 引数 : 保存する文字列
# : クッキーの有効時間(秒)
# 戻値 : なし
#------------------------------------------------------------------
sub SetCookie
{
my($data, %data, $str_cookie, $cookie_time);
my($sec, $min, $hour, $mday, $mon, $year, $wday);
my(@mons, @week, $dt);

$str_cookie = @_[0];
$cookie_time = @_[1];

#// 文字列のエスケープ
$str_cookie =~ s/\,/%2C/g;
$str_cookie =~ s/;//g;
$str_cookie =~ s/([^\w\=\& ])/'%' . unpack("H2", $1)/eg;

#// 有効期限設定
($sec, $min, $hour, $mday, $mon, $year, $wday) = localtime(time + $cookie_time);
@mons = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec');
@week = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat');
$dt = sprintf("%s\, %02d-%s-%04d %02d:%02d:%02d GMT", $week[$wday], $mday, $mons[$mon], $year+1900, $hour, $min, $sec);

#// ヘッダ出力
print "Set-Cookie: $str_cookie expires=$dt;\n";
}

#------------------------------------------------------------------
# 関数 : GetCookie
# 概要 : クッキー取得
# 引数 : なし
# 戻値 : クッキーの値
#------------------------------------------------------------------
sub GetCookie
{
my($cookie) = $ENV{'HTTP_COOKIE'};
my($key, $val, %data);
my(@cookie);

#// クッキー取得
@cookie = split(/ /, $cookie);
foreach(@cookie)
{
($key, $val) = split(/=/);

#// 文字列をデコードする
$val =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C",hex($1))/eg;
$val =~ s/%2C/\,/g;
$val =~ s/%20/ /g;
$data{$key} = $val;
}

#// 戻り値セット
return %data;
}

#------------------------------------------------------------------
# 関数 : EscapeSQL
# 概要 : SQLエスケープ処理
# 引数 : 変換する文字列
# 戻値 : エスケープ処理後の文字列
#------------------------------------------------------------------
sub EscapeSQL
{
my $str = @_[0];
if ($str eq '')
{
return "null";
}

$str =~ s/'/''/g;
return "'" . $str . "'";
}

1;