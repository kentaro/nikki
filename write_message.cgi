#!/usr/bin/perl
use utf8;

# CGI���W���[�����C���|�[�g

use CGI;
use lib "lib";

# CGI�C���X�^���X�̐���
$cgi = new CGI();

# CGI::Session���W���[�����C���|�[�g
use CGI::Session;


# �Z�b�V�����̐����i�����j
$session = new CGI::Session($cgi);


# �Z�b�V�����p�����[�^�ulogin_check�v�̒l��ϐ�login_check�ɑ��
$login_check = $session->param('login_check');


# �Z�b�V�����p�����[�^�uuser_name�v�̒l��ϐ�user_name�ɑ��
$user_name = $session->param('user_name');


# HTTP�w�b�_���o��
print $session->header(-type=>'text/html',-charset=>'Shift-JIS');

# HTML�w�b�_���o��
print $cgi->start_html(-title=>'�f����',-lang=>'ja');


# ���O�C���m�F
if ($login_check eq 'ok') {
	# �ڑ����[�U�[���{�����N�̕\��
	print 'Login: <b>' . $user_name . '</b>';
	print '<hr>';
	print '<a href="menu_message.pl">�y���j���[�z</a>';
	print '<a href="logout.pl">�y���O�A�E�g�z</a>';
	print '<hr>';

	# ���̓t�H�[���̕\��
	print '�����b�Z�[�W����͂��Ă��������B<br><br>';
	print '<form action="insert_message.pl" method="POST">';
	print '�^�C�g���F<br>';
	print '<input type="text" name="title" size="50">';
	print '<br><br>';
	print '���b�Z�[�W�F<br>';
	print '<textarea name="message" cols="40" rows="5"></textarea>';
	print '<br><br>';
	print '<input type="submit" value="���b�Z�[�W�̓o�^">';
	print '</form>';
} else {
	# ���b�Z�[�W�{�����N�̕\��
	print '�����O�C�����Ă��܂���B';
	print '<hr>';
	print '<a href="login.html">�y���O�C���z</a>';
}

# HTML�t�b�^���o��
print $cgi->end_html();