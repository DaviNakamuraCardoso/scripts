

class Dog {

    has $.name;
    has $.weight;
    
    method bark() 
    {
        given ($.weight)
        {
            when $_ > 20 {
                say "$.name says WOOF, WOOF!";
            }
            default { 
                say "$.name says woof, woof.";
            }
        }
    }
}


my Dog $codie = Dog.new(name => "Codie", weight => 42);
my Dog $fido = Dog.new(name => "Fido", weight => 10);

$codie.bark();
$fido.bark();

