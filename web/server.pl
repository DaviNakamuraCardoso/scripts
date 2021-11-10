use Mojolicious::Lite;

get "/" => sub {
    my $c = shift;

    $c->render(
        template => 'index'
    );

};

app->start;


__DATA__
@@ index.html.ep
<h1>Hello, Perl!</h1>
