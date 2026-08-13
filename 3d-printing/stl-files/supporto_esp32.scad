// 📡 Supporto ESP32 DevKit
// Modello OpenSCAD

// Parametri
width = 60;
depth = 50;
height = 15;
wall = 2;
mount_hole = 3.2; // M3

module supporto_esp32() {
    difference() {
        // Base
        cube([width, depth, height]);
        
        // Fori montaggio (4 angoli)
        positions = [
            [5, 5],
            [width - 5, 5],
            [5, depth - 5],
            [width - 5, depth - 5]
        ];
        
        for (pos = positions) {
            translate([pos[0], pos[1], -1])
                cylinder(h = height + 2, r = mount_hole/2);
        }
        
        // Cavità per ESP32
        translate([wall, wall, wall])
            cube([width - 2*wall, depth - 2*wall, height]);
    }
}

// Render
supporto_esp32();
