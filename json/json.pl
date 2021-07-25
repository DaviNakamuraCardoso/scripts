
use JSON;
use Data::Dumper; 

my $filename = "test.json"; 
my $data; 
open($data, "<", $filename); 
my $decoded = decode_json($data);

print Dumper($decoded); 

