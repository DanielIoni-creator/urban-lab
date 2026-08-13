// 🛴 Urban Lab Scooter - Telaio
// Modello OpenSCAD per stampa 3D

// Parametri
length = 1200;  // mm
width = 400;    // mm
thickness = 8;  // mm
hole_diameter = 8; // mm per bulloni

// Telaio principale
module telaio() {
    difference() {
        // Piattaforma principale
        cube([length, width, thickness]);
        
        // Fori per bulloni (8 posizioni)
        for (x = [50, 200, 400, 600, 800, 1000, 1150]) {
            for (y = [50, 350]) {
                translate([x, y, -1])
                    cylinder(h = thickness + 2, r = hole_diameter/2);
            }
        }
        
        // Alleggerimento centrale
        translate([200, 50, 1])
            cube([800, 300, thickness - 2]);
    }
}

// Render
telaio();
