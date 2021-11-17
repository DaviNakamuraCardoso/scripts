use Mojolicious::Lite;
use Mojolicious::Static;

my $percent = 100;

my $app = app;
my $static = $app->static;
push @{$static->paths}, ($ENV{PWD});


get '/percent' => sub {
    my $c = shift;

    $percent -= rand(10) / 100 ;
    return $c->render(
        json => { percent => $percent }
    );
};

get '/' => sub {
    my $c = shift;

    return $c->render(
        template => 'index'
    );
};

$app->start;
