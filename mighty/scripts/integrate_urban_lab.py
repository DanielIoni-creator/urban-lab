#!/usr/bin/env python3
"""
🏭 Urban Lab - Integrazione MIGHTY
Collega MIGHTY con il sistema di controllo del monopattino
"""

import rospy
from geometry_msgs.msg import PoseStamped, Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan, Image
import numpy as np
import sys
import os

# Aggiungi MIGHTY al path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

class UrbanLabMightyBridge:
    """
    Ponte tra MIGHTY e Urban Lab
    """
    def __init__(self):
        rospy.init_node('urban_lab_mighty_bridge')
        
        # Publisher per comandi di movimento
        self.cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        
        # Subscriber per stato MIGHTY
        self.odom_sub = rospy.Subscriber('/odometry', Odometry, self.odom_callback)
        self.scan_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        
        # Stato
        self.current_pose = None
        self.obstacles = []
        self.goal = None
        
        rospy.loginfo("🏭 Urban Lab - MIGHTY Bridge avviato!")
    
    def odom_callback(self, msg):
        """Aggiorna la posizione corrente"""
        self.current_pose = msg.pose.pose
        
    def scan_callback(self, msg):
        """Aggiorna la mappa degli ostacoli"""
        self.obstacles = np.array(msg.ranges)
        
    def set_goal(self, x, y, z=0):
        """Imposta l'obiettivo per MIGHTY"""
        self.goal = (x, y, z)
        rospy.loginfo(f"🎯 Obiettivo impostato: ({x}, {y}, {z})")
        
    def send_command(self, linear, angular):
        """Invia comandi al monopattino"""
        cmd = Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        self.cmd_pub.publish(cmd)
        
    def run(self):
        """Loop principale"""
        rate = rospy.Rate(20)  # 20 Hz
        
        while not rospy.is_shutdown():
            if self.goal and self.current_pose:
                # Simula il calcolo della traiettoria
                self.compute_trajectory()
            rate.sleep()
    
    def compute_trajectory(self):
        """Calcola la traiettoria usando MIGHTY"""
        # Placeholder per MIGHTY integration
        rospy.loginfo("🧠 Calcolo traiettoria MIGHTY...")
        # Implementazione reale qui

def main():
    bridge = UrbanLabMightyBridge()
    
    # Esempio di utilizzo
    rospy.sleep(1)
    bridge.set_goal(10.0, 5.0, 0.0)
    
    try:
        bridge.run()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()
