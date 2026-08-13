    }
    requestAnimationFrame(animateVortex);
}

// Avvia animazione vortex
animateVortex();

// Funzioni di utilità per la console
window.portal = {
    status: function() {
        console.log('🌀 Portale del Tempo Fisico');
        console.log('📊 Stato:', {
            timestamp: new Date().toLocaleTimeString(),
            mighty: mightyActive ? 'ONLINE' : 'STANDBY',
            events: eventCounter
        });
    },
    reset: function() {
        document.getElementById('timeline').innerHTML = '';
        eventCounter = 0;
        addTimelineEvent('🔄 Portale resettato');
        console.log('🔄 Portale resettato');
    }
};

console.log('📌 Comandi utili: portal.status() - portal.reset()');
