use File::Spec;
use Plack::Builder;
use Plack::App::File;
use Plack::App::WrapCGI;

builder {
    enable "Plack::Middleware::Static",
        path => qr{^/(?:images/.+|.+\.html|.+\.css)$},
        root => ".";

    for my $file (glob "*.cgi") {
        mount "/$file" => Plack::App::WrapCGI->new(script => $file)->to_app;
    }

    mount "/" => Plack::App::File->new(file => "index.html");
};
