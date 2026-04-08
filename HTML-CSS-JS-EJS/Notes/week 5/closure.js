function grandParent() {
    var house = 'White-House';
   
    function parent() {   
        var car = 'Audi';
        house = 'Green House';
        function child() {   
            var bike = 'BMW ';
            console.log('I have:', house + ', ' + car + ' Car and ' + bike + 'Bike');
        }
        return child;
    }
    return parent;
}
var FirstGeneration = grandParent();
console.log(typeof(FirstGeneration)); //FirstGeneration is of type function
var SecondGeneration = FirstGeneration();
console.log(typeof(SecondGeneration)); //legacyGenY is of type function
SecondGeneration(); // I have: YellowHouse Tesla Vespa