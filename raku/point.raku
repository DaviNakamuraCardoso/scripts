
class Point {
    has Rat $.x;
    has Rat $.y;
    
    method say() {
        return "$.x, $.y";
    }
}

my Point $p1 = Point.new(x => 2.0, y => 4.0);
my Point $p2 = Point.new(x => 3.0, y => 6.0);

say $p1; 
say $p2; 
