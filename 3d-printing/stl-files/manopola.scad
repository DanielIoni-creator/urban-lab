// 🖐️ Manopola per Urban Lab Scooter
// Materiale: TPU

// Parametri
length = 120;
diameter = 35;
inner_diameter = 22;

module manopola() {
    difference() {
        // Corpo principale
        cylinder(h = length, r = diameter/2);
        
        // Foro interno per manubrio
        translate([0, 0, -1])
            cylinder(h = length + 2, r = inner_diameter/2);
        
        // Scanalature antiscivolo
        for (i = [0:10:length]) {
            translate([0, 0, i])
                cylinder(h = 1, r = diameter/2 + 1);
        }
    }
}

// Render
manopola();
