#!/usr/bin/perl

# 2012/09/25：2012/09/24の遅くに編集してこっちを使っていました

require './common.pl';
use strict;
use DBI;

# パラメータ取得
my %data = Common::GetPara();
my $entry_title  = $data{"entry_title"};
my $entry_text  = $data{"entry_text"};
my $login_id = $data{"login_id"};

# 2012/09/25 「entry_title」をコメントにしたらエラーになってしまった…
# 2012/09/26 コメントにしなかったら動いた

# データベース接続
my $conn = Common::ConnectDB();

# 日記投稿
my $sql = <<"....";
INSERT INTO 
    entry ( entry_title, entry_time, entry_text, login_id) 
VALUES 
    ( ?, now(), ?,  ? );
....

my $select = $conn->prepare($sql);
$select->execute($entry_title, $entry_text, $login_id);

# データベースクローズ
Common::CloseDB($conn);


print "Content-type: text/html\n\n";

# 書きこみ完了画面へ遷移させる
print << "END_OF_HTML";
<html>
<head>
<meta http-equiv="refresh" content="0;url=entry_finish.html">
</head>
</html>
END_OF_HTML

exit;