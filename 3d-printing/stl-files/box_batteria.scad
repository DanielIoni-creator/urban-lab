// 🔋 Box Batteria per Urban Lab
// Materiale: PETG

// Parametri
width = 200;
depth = 150;
height = 80;
wall = 3;
mount_hole = 4.2; // M4

module box_batteria() {
    difference() {
        // Scatola esterna
        cube([width, depth, height]);
        
        // Cavità interna
        translate([wall, wall, wall])
            cube([width - 2*wall, depth - 2*wall, height - wall]);
        
        // Fori montaggio
        positions = [
            [20, 20],
            [width - 20, 20],
            [20, depth - 20],
            [width - 20, depth - 20]
        ];
        
        for (pos = positions) {
            translate([pos[0], pos[1], -1])
                cylinder(h = wall + 2, r = mount_hole/2);
        }
        
        // Aperture ventilazione
        for (x = [30:20:width-30]) {
            for (y = [30:20:depth-30]) {
                translate([x, y, height - wall])
                    cube([5, 5, wall + 1]);
            }
        }
    }
}

// Render
box_batteria();
